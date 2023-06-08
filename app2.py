# This code looks at index.html file and grabs the information from there and puts it on a webpage on localhost. 
from flask import Flask, render_template
from imdb import IMDb


app = Flask(__name__)

@app.route('/')
def index():
    ia = IMDb()
    movies = ia.search_movie('Spider-Man')
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run()
