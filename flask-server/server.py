"""Flask server"""

from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "TODO: Don't forget to make a secret key"


@app.route("/members")  # Members API Route
def members():
    """Test to display backend JSON using React"""
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
