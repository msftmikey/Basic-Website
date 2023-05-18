# This code looks at index.html file and grabs the information from there and puts it on a webpage on localhost. 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
