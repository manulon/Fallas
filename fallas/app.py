from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import send_from_directory
from MovieEngine import MovieEngine
import os
import json


app = Flask(__name__, template_folder='')

movies = {}
with open('static/peliculas.json') as json_data:
    movies = json.load(json_data)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def home():
    return render_template('fallas.html')


class MovieSelector():
    def _init_(self):
        self.engine = MovieEngine()

    def run(self, g, d, y, c):
        years = y.split(' ')
        year_range = range(int(years[0]), int(years[-1]))
        self.set_answers(g, d, year_range, c)
        self.set_movie()

    def set_answers(self, g, d, y, c):
        self.genre = g
        self.duration = d
        self.year = y
        self.country = c

    def set_movie(self):
        # tags = self.genre + ' ' + self.duration + ' ' + self.year + ' ' + self.country
        # print("###############################################")
        # print(tags)
        engine = MovieEngine()
        self.movie_name = engine.get_movie(
            self.year, self.genre, self.duration, self.country)
        print(self.movie_name)

    def get_movie(self):
        return self.movie_name


@app.route("/result", methods=['POST'])
def result():
    body = request.get_json()
    engine = MovieSelector()
    engine.run(body["genre"], body["duration"], body["year"], body["country"])
    movie_name = engine.get_movie()

    print("------------------")
    print(movie_name)
    print("------------------")

    movie_data = {"name": movie_name,
                  "img": movies[movie_name]['img'],
                  "link": movies[movie_name]['link']
                  }

    return jsonify(movie_data), 200


@app.route("/result2", methods=['POST'])
def result2():
    body = request.get_json()
    answers = body['answers']
