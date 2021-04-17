from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from io import BytesIO
from form import DataInput, StockConfigForm
import pandas as pd
from rebalance import rebalance, current_allocation

app = Flask(__name__)
app.config["SECRET_KEY"] = "boop"
csrf = CSRFProtect(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = DataInput(meta={"csrf": False})
    # TODO: stage input
    # If form part 1 is filled, introduce dynamic form 2 asking for target alloc
    # Example: user submits order data for stock A, B. question should follow: what's your  desired allocation for A, and for B?
    # Outcome: rebalancing calc

    if form.validate_on_submit():
        buffer = BytesIO(form.csv.data.read())
        df = pd.read_csv(buffer)
        # TODO: replace this with user input
        target_allocation = {"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25}

        rebalance_df = rebalance(
            current_allocation=current_allocation(df),
            target_allocation=target_allocation,
        )

        return render_template(
            "form.html",
            form=form,
            df=rebalance_df.to_html(),
        )

    return render_template("form.html", form=form)


@app.route("/dynamic", methods=("GET", "POST"))
@csrf.exempt
def testform():
    user_addresses = [
        {"name": "First Address", "proportion": "test"},
        {"name": "First Address", "proportion": "test"},
    ]
    form = StockConfigForm(configuration=user_addresses)
    return render_template("dynamic.html", form=form)
