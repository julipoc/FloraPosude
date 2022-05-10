from flask_login import current_user, login_user
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from FloraPosude import db
from FloraPosude.models.user import User
from FloraPosude.users.forms import LoginForm, ProfileForm


user = Blueprint("user", __name__)


@user.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    user = User.query.all()
    print(user)
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

        if user is not None:
            if form.remember_me.data == True:
                login_user(user, remember=True)
            else:
                login_user(user, remember=False)
            return redirect(url_for("home.index"))
    return render_template("login.html", form=form)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))


@user.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.password = form.password.data

        db.session.commit()
        return redirect(url_for("user.profile"))

    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.username.data = current_user.username
    form.password.data = current_user.password

    return render_template("profile.html", form=form)


