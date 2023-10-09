# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("indexe.html")


@app.route("/interdit")
def interdit():
    abort(405)


@app.route('/aurevoir')
def aurevoir():
    return render_template('aurevoir.html')


@app.errorhandler(405)
def page_interdite(e):
    return render_template("page_interdite.html"), 405


# @app.route('/page_interdite')
# def page_interdite():
#     return render_template('page_interdite.html')


if __name__ == "__main__":
    app.run(debug=False)
