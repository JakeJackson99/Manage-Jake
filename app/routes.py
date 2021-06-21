from flask import render_template, url_for, redirect

from app import app
from app.forms import NoteForm


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
        return redirect('/notes')

    return render_template('note_form.html', form=form)
