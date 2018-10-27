#!/usr/bin/env python3
"""
My flask app for NLP project
"""
# Note, capital letters since, Invalid constant name "app" (invalid-name)
# https://stackoverflow.com/questions/10815549/pylint-showing-invalid-variable-name-in-output

# Import
from flask import Flask, render_template, request
from SynonymSentenceParser import SynonymSentenceParser

app = Flask(__name__)

# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", text="No result")

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        string = request.form["myString"]

        newParser = SynonymSentenceParser(string)
        spellingErrors = ', '.join(newParser.spellingErrors)
        newSentences = newParser.newSentences
        return render_template("index.html", spellingErrors=', '.join(spellingErrors), newSentences=newSentences)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

