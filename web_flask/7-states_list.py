#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:              display "Hello HBNB!"
            /hbnb:          display "HBNB"
            /c/<text>:      display "C" + text (replace underscores with space)
            /python/<text>: display "Python" + text (default is "is cool")
            /number/<n>:    display "n is a number" only if n is an integer
            /number_template/<n>: display HTML page only if n is an integer
            /number_odd_or_even/<n>: display HTML page only if n is an integer
            /states_list: display a HTML page: (inside the tag BODY)
                H1 tag: “States”
                UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
                LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_in_int(n):
    """display text only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_in_int(n):
    """display HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def html_odd_or_even(n):
    """display HTML page only if n is an integer"""
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states_list')
def states_list():
    """display html page
       fetch sorted states to insert into html in UL tag"""
    states = list(storage.all("State").values())
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
