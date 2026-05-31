from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from hangman import Hangman



app = Flask(__name__)
app.debug = True
app.secret_key = "SupersEcretkeYForPLAyingHanGMan"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #avoids a warning
db = SQLAlchemy()  #creates db instance
db.init_app(app)


class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(), nullable=False)


@app.route("/", methods=["GET", "POST"])
def index():

    notes = Notes.query.all()

    editing_id = request.args.get('edit')
    return render_template("index.html", notes=notes, editing_id=editing_id)


@app.route('/add', methods=['GET', 'POST'])
def add_note():
    content = request.form["content"]

    if content != '':
        n = Notes(content=content)
        db.session.add(n)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

@app.route('/save', methods=['GET', 'POST'])
def edit_note():

    # update logic to rollback if cancel or commit if save
    button_val = request.form.get("submit")
    if button_val == "Save":
        note_id = int(request.form.get('note_id'))
        content = request.form["content"]
        note = Notes.query.filter_by(id=note_id).first_or_404()
        note.content = content
        db.session.commit()
    else:
        db.session.rollback()
    return redirect('/')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_note(id):
    # raises 404 if ID note found, otherwise returns result
    note = Notes.query.filter_by(id=id).first_or_404()

    # deletes the note or if can't find returns to previous state
    try:
        db.session.delete(note)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    return redirect('/')

# Routes for Hangman game - uses game.html template page
@app.route("/game_page", methods=['GET', 'POST'])
def game_page():
    if "guess_word" in session:
        guess_word = session['guess_word']
        wrong_guesses = session['wrong_guesses']
        guess_letters = session['guess_letters']
    else:
        guess_word = None
        wrong_guesses = 0
        guess_letters = []
    return render_template("game.html", guess_word=guess_word, wrong_guesses=wrong_guesses, guess_letters=guess_letters)

@app.route("/new_game", methods=['GET', 'POST'])
def new_game():
    #starts new game of hangman
    game = Hangman()
    #start sessions with variables needed for duration of game

    rand_word, guess_word, wrong_guesses, guess_letters = game.gameStart()
    session['rand_word'] = rand_word
    session['guess_word'] = guess_word
    session['wrong_guesses'] = wrong_guesses
    session['guess_letters'] = guess_letters

    return render_template("game.html", guess_word=guess_word, wrong_guesses=wrong_guesses, guess_letters=guess_letters)

# Receives guess from user, passes to hangman game to update
# game components, stores sessoins, updates status to user
@app.route("/guess", methods=['GET', 'POST'])
def guess_letter():
    # initialize gamestate in new route
    game = Hangman()
    # Get guess from user
    letter = request.form["letter"]

    # Pull variables from session
    rand_word = session['rand_word']
    guess_word = session['guess_word']
    wrong_guesses = session['wrong_guesses']
    guess_letters = session['guess_letters']

    # status will be used to determine msg sent to user
    status = None

    # send components to Hangman to compare / update
    rand_word, guess_word, wrong_guesses, guess_letters, status = game.playGame(letter, rand_word, guess_word, wrong_guesses, guess_letters)

    # update session variables
    #session['rand_word'] = rand_word
    session['guess_word'] = guess_word
    session['wrong_guesses'] = wrong_guesses
    session['guess_letters'] = guess_letters

    return render_template("game.html", rand_word=rand_word, guess_word=guess_word, wrong_guesses=wrong_guesses, guess_letters=guess_letters, status=status)

if __name__ == "__main__":
    app.run(debug=True)
