from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
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


if __name__ == "__main__":
    app.run(debug=True)
