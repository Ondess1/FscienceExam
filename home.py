from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    actors = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

@app.route('/movies')
def movies():
    all_movies = Movie.query.all()
    return render_template('movie.html', movies=all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_movie = Movie(
            title=request.form['title'],
            genre=request.form['genre'],
            actors=request.form['actors'],
            publication_year=request.form['publication_year']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('movies'))
    return render_template('add.html')

def addcontext():
    with app.app_context():
        db.create_all()

if _name_ == '_main_':
    addcontext()
    app.run(port=5000, debug=True