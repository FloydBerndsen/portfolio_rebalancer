from flask import Flask, render_template
from io import BytesIO
from form import MyForm
import pandas as pd
from rebalance import rebalance, current_allocation

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = MyForm(meta={"csrf": False})
    # TODO: stage input
    # If form part 1 is filled, introduce dynamic form 2 asking for target alloc
    # Example: user submits order data for stock A, B. question should follow: what's your  desired allocation for A, and for B?
    # Outcome: rebalancing calc

    if form.validate_on_submit():
        name = form.name.data
        buffer = BytesIO(form.csv.data.read())
        df = pd.read_csv(buffer)
        # TODO: replace this with user input
        target_allocation = {"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25}

        rebalance_df = rebalance(
            current_allocation=current_allocation(df),
            target_allocation=target_allocation,
        )

        return render_template(
            # TODO: replace to_html with secure iteration of output
            "form.html",
            form=form,
            name=name,
            df=rebalance_df.to_html(),
        )

    return render_template("form.html", form=form)
