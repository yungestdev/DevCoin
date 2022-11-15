from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from database import Crypto 

app = Flask(__name__)
app.secret_key = 'YungCr1pt0B07'

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)