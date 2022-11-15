"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route("/game")
def show_madlib_form():
    answer = request.args.get("answer")
    if answer == 'no':
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route("/madlib", methods=['POST', 'GET'])
def show_madlib():
    person = request.form.get('person')
    color = request.form.get('color')
    nouns = request.form.get('nouns').split(' ')
    past_verb = request.form.get('past_verb')
    present_verb = request.form.get('present_verb')
    adjectives = request.form.getlist('adjectives')
    adverb = request.form.get('adverb')
    template = choice(["madlib.html", "madlib2.html", "madlib3.html"])

    return render_template(template, person=person, nouns=nouns, color=color, adjectives=adjectives, past_verb=past_verb, present_verb=present_verb, adverb=adverb)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
