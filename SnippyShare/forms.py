from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class ContentForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

    content = StringField("Content", validators=[DataRequired()], widget=TextArea())

    submit = SubmitField("Generate URL")
