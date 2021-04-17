from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import FieldList, FormField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


class DataInput(FlaskForm):
    csv = FileField("csv", validators=[FileRequired()])


class StockConfigEntry(FlaskForm):
    name = StringField()
    proportion = StringField()  # TODO: replace with float/decimal


class StockConfigForm(FlaskForm):
    configuration = FieldList(FormField(StockConfigEntry), min_entries=1)
