from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NoteForm(FlaskForm):
    note_content = StringField('What to note...', validators=[DataRequired()])
    submit = SubmitField('Add Note')
