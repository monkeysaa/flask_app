"""Flask server"""

from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "TODO: Don't forget to make a secret key"


@app.route("/members")  # Members API Route
def members():
    """Test to display backend JSON using React"""
    return {"members": ["Member1", "Member2", "Member3"]}


def login_required(f):  # login required decorator
    """Redirect to Login as needed"""

    @wraps(f)
    def wrap(*args, **kwargs):
        """Do we really need two docstrings, pylint?"""
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("login"))

    return wrap


@app.route("/")
# @login_required
def home():
    """Every app has to start somewhere"""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Authenticate user"""
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid credentials. Please try again."
        else:
            session["logged_in"] = True
            flash("You were just logged in!")
            return redirect(url_for("home"))
    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    """Logout user"""
    session.pop("logged_in", None)
    flash("You were just logged out!")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
