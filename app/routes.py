from flask import render_template, url_for, redirect

from app import app, db
from app.forms import NoteForm
from app.models import Note


"""
TODO
check that the note_content is less than 280
"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')


@app.route('/note_form', methods=['GET', 'POST'])
def note_form():
    form = NoteForm()

    if form.validate_on_submit():
        note = Note(note_content=form.note_content.data)
        db.session.add(note)
        db.session.commit()
        return redirect('/notes')

    return render_template('note_form.html', form=form)
