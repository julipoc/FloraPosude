from sqlalchemy import func

from flask import Blueprint, render_template
from flask_login import login_required

from FloraPosude.models.pot import Pot
from FloraPosude.home.forms import FilterForm


home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
@login_required
def index():
    pots = Pot.query.all()
    form = FilterForm()

    if form.validate_on_submit():
        pots = Pot.query.filter(
            (func.lower(Pot.status).contains(func.lower(form.filter_value.data)))).all()
        return render_template("index.html", pots=pots, form=form)

    return render_template("index.html", pots=pots, form=form)