from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import send_from_directory
import os
import json


app = Flask(__name__, template_folder='')

movies = {}
with open('static/aperturas.json') as json_data:
    movies = json.load(json_data)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template('fallas.html')

class MovieSelector():
    movies = dict()
    genre = 'None'
    duration = 'None'
    year = 'None'
    country = 'None'
    movie = ''

    def run(self, g, d, y, c):
        self.get_answers()
        self.set_answers(g, d, y, c)
        self.set_movie()
        
    def get_answers(self):               
        self.movies['comedy short 2022 - 2008 international'] = 'Perfect Strangers (2017) Alex de la Iglesia'
        self.movies['comedy short 2008 - 1998 international'] = 'The Simpsons Movie (2007) David Silverman'
        self.movies['comedy short 1998 - 1990 international'] = 'When Harry Met Sally (1989) Rob Reiner'
        self.movies['comedy short 1989 - 1970 international'] = 'Annie Hall (1977) Woody Allen'
        self.movies['comedy short 2022 - 2008 argentina'] = 'El futbol o yo (2017) Marcos Carnevale'
        self.movies['comedy short 2008 - 1998 argentina'] = 'Baneros III todopoderosos (2006) Rodolfo Ledo'
        self.movies['comedy short 1998 - 1990 argentina'] = '100 veces no debo (1990) Alejandro Doria'
        self.movies['comedy short 1989 - 1970 argentina'] = 'Esperando la carroza (1985) Alejandro Doria'
        self.movies['comedy medium 2022 - 2008 international'] = 'Parasite (2019) Bong Joon-Ho'
        self.movies['comedy medium 2008 - 1998 international'] = 'Anything Else (2003) Woody Allen'
        self.movies['comedy medium 1998 - 1990 international'] = 'The Truman Show (1998) Peter Wair'
        self.movies['comedy medium 1989 - 1970 international'] = 'Hannah and her sisters (1986) Woody Allen'
        self.movies['comedy medium 2022 - 2008 argentina'] = 'Relatos Salvajes (2014) Damian Szifron'
        self.movies['comedy medium 2008 - 1998 argentina'] = 'Papa es un idolo (2000) Juan Jose Jusid'
        self.movies['comedy medium 1998 - 1990 argentina'] = 'Enfermero de dia, camarero de noche (1990) Anibal di Salvo'
        self.movies['comedy medium 1989 - 1970 argentina'] = 'El profesor patagonico (1970) Fernando Ayala'   
        self.movies['comedy long 2022 - 2008 international'] = 'The Wolf of Wall Street (2013) Martin Scorsese'
        self.movies['comedy long 2008 - 1998 international'] = 'Love Actually (2003) Richard Curtis'
        self.movies['comedy long 1998 - 1990 international'] = 'Forrest Gump (1994) Robert Zemeckis'
        self.movies['comedy long 1989 - 1970 international'] = 'The World According to Garp (1982) George Roy Hill'
        self.movies['comedy long 2022 - 2008 argentina'] = 'Igualita a mi (2010) Diego Kaplan'
        self.movies['comedy long 2008 - 1998 argentina'] = 'Nueve reinas (2000) Fabian Bielinsky'
        self.movies['comedy long 1998 - 1990 argentina'] = 'Enfermero de dia, camarero de noche (1990) Anibal di Salvo'
        self.movies['comedy long 1989 - 1970 argentina'] = 'El profesor patagonico (1970) Fernando Ayala'
        self.movies['crime short 2022 - 2008 international'] = 'Drive (2011) Nicholas Winding Refn'
        self.movies['crime short 2008 - 1998 international'] = 'American Psycho (2000) Mary Harron'
        self.movies['crime short 1998 - 1990 international'] = 'Reservoir Dogs (1992) Quentin Tarantino'
        self.movies['crime short 1989 - 1970 international'] = 'Blood Simple (1984) Joel Coen'
        self.movies['crime short 2022 - 2008 argentina'] = 'Muerte en Buenos Aires (2014) Natalia Meta'
        self.movies['crime short 2008 - 1998 argentina'] = 'Tiempo de valientes (2005) Damian Szifron'
        self.movies['crime short 1998 - 1990 argentina'] = 'El caso de Maria Soledad (1993) Hector Olivera'
        self.movies['crime short 1989 - 1970 argentina'] = 'Ultimos dias de la victima (1982) Adolfo Aristarain'
        self.movies['crime medium 2022 - 2008 international'] = 'The Mule (2018) Clint Eastwood'
        self.movies['crime medium 2008 - 1998 international'] = 'Catch me if you can (2002) Steven Spielberg'
        self.movies['crime medium 1998 - 1990 international'] = 'Leon: The Professional (1994) Leon Besson'
        self.movies['crime medium 1989 - 1970 international'] = 'Blow Out (1981) Brian de Palma'
        self.movies['crime medium 2022 - 2008 argentina'] = 'Muerte en Buenos Aires (2014) Natalia Meta'
        self.movies['crime medium 2008 - 1998 argentina'] = 'Tiempo de valientes (2005) Damian Szifron'
        self.movies['crime medium 1998 - 1990 argentina'] = 'El caso de Maria Soledad (1993) Hector Olivera'
        self.movies['crime medium 1989 - 1970 argentina'] = 'Ultimos dias de la victima (1982) Adolfo Aristarain'   
        self.movies['crime long 2022 - 2008 international'] = 'The Irishman (2019) Martin Scorsese'
        self.movies['crime long 2008 - 1998 international'] = 'The departed (2006) Martin Scorsese'
        self.movies['crime long 1998 - 1990 international'] = 'Pulp Fiction (1994) Quentin Tarantino'
        self.movies['crime long 1989 - 1970 international'] = 'The Godfather (1972) Francis Ford Coppola'
        self.movies['crime long 2022 - 2008 argentina'] = 'Muerte en Buenos Aires (2014) Natalia Meta'
        self.movies['crime long 2008 - 1998 argentina'] = 'Tiempo de valientes (2005) Damian Szifron'
        self.movies['crime long 1998 - 1990 argentina'] = 'El caso de Maria Soledad (1993) Hector Olivera'
        self.movies['crime long 1989 - 1970 argentina'] = 'Ultimos dias de la victima (1982) Adolfo Aristarain'
        self.movies['horror short 2022 - 2008 international'] = 'The Boy (2016) William Brent Eln'
        self.movies['horror short 2008 - 1998 international'] = 'House of 1000 Corpses (2003) Rob Zombie'
        self.movies['horror short 1998 - 1990 international'] = 'The Blair Witch Project (1998) Daniel Myrick'
        self.movies['horror short 1989 - 1970 international'] = 'A Nightmare on Elm Street (1984) Wes Craven'
        self.movies['horror short 2022 - 2008 argentina'] = 'Juan de los Muertos (2011) Alejandro Brugues'
        self.movies['horror short 2008 - 1998 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror short 1998 - 1990 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror short 1989 - 1970 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror medium 2022 - 2008 international'] = 'Split (2016)  M. Night Shyamalan'
        self.movies['horror medium 2008 - 1998 international'] = 'Saw (2004) James Wan'
        self.movies['horror medium 1998 - 1990 international'] = 'Scream (1996) Wes Craven'
        self.movies['horror medium 1989 - 1970 international'] = 'The thing (1982) John Carpenter'
        self.movies['horror medium 2022 - 2008 argentina'] = 'Juan de los Muertos (2011) Alejandro Brugues'
        self.movies['horror medium 2008 - 1998 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror medium 1998 - 1990 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror medium 1989 - 1970 argentina'] = 'El Nino de Barro (2007) Jorge Algora'   
        self.movies['horror long 2022 - 2008 international'] = 'The House That Jack Built (2018) Lars von Trier'
        self.movies['horror long 2008 - 1998 international'] = 'Orphan (2008) Jaume Collet-Serra'
        self.movies['horror long 1998 - 1990 international'] = 'Thesis (1996) Alejandro Amenabar'
        self.movies['horror long 1989 - 1970 international'] = 'The Shinning (1980) Stanley Kubrick'
        self.movies['horror long 2022 - 2008 argentina'] = 'Juan de los Muertos (2011) Alejandro Brugues'
        self.movies['horror long 2008 - 1998 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror long 1998 - 1990 argentina'] = 'El Nino de Barro (2007) Jorge Algora'
        self.movies['horror long 1989 - 1970 argentina'] = 'El Nino de Barro (2007) Jorge Algora'  
        self.movies['science fiction short 2022 - 2008 international'] = 'Coherence (2013) James Ward Byrkit'
        self.movies['science fiction short 2008 - 1998 international'] = 'The Butterfly Effect (2004) Eric Bress'
        self.movies['science fiction short 1998 - 1990 international'] = 'The Iron Giant (1998) Brad Bird'
        self.movies['science fiction short 1989 - 1970 international'] = 'The Fly (1984) David Cronenberg'
        self.movies['science fiction short 2022 - 2008 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction short 2008 - 1998 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction short 1998 - 1990 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction short 1989 - 1970 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction medium 2022 - 2008 international'] = 'Ready Player One (2018) Steven Spielberg'
        self.movies['science fiction medium 2008 - 1998 international'] = 'Eternal Sunshine of the Spotless Mind (2004) Michael Gondry'
        self.movies['science fiction medium 1998 - 1990 international'] = 'The Matrix (1998) Lilly Wachowski'
        self.movies['science fiction medium 1989 - 1970 international'] = 'The Swarm (1978) Irwin Allen'
        self.movies['science fiction medium 2022 - 2008 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction medium 2008 - 1998 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction medium 1998 - 1990 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction medium 1989 - 1970 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'   
        self.movies['science fiction long 2022 - 2008 international'] = 'Interstellar (2014) Christopher Nolan'
        self.movies['science fiction long 2008 - 1998 international'] = 'Avatar (2008) James Cameron'
        self.movies['science fiction long 1998 - 1990 international'] = 'Terminator 2: Judgment Day (1996) James Cameron'
        self.movies['science fiction long 1989 - 1970 international'] = 'E.T. the Extra-Terrestrial (1982) Steven Spielberg'
        self.movies['science fiction long 2022 - 2008 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction long 2008 - 1998 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction long 1998 - 1990 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'
        self.movies['science fiction long 1989 - 1970 argentina'] = 'Fase 7 (2010) Nicolas Goldbart'    

    def set_answers(self, g, d, y, c):
        self.genre      = g
        self.duration   = d
        self.year       = y 
        self.country    = c       

    def set_movie(self):
        tags = self.genre + ' ' + self.duration + ' ' + self.year + ' ' + self.country
        print("###############################################")
        print(tags)
        print(self.movies.get(tags))

        self.movie_name = self.movies.get(tags)
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
    
    movie_data = {  "name": movie_name,
                    "img": movies[movie_name]['img'],
                    "link": movies[movie_name]['link']
    
    }
                    
    return jsonify(movie_data), 200

@app.route("/result2", methods=['POST'])
def result2():
    body = request.get_json()
    answers = body['answers']
