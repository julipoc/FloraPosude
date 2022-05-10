from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

from FloraPosude import db

from FloraPosude.models.plant import Plant
from FloraPosude.models.pot import Pot
from FloraPosude.pots.forms import CreateUpdatePotForm

from FloraPosude.helpers.changing_pot_status import *
from FloraPosude.helpers.sync_func import generate_values


pot = Blueprint("pot", __name__)


@pot.route("/details_pot/<id>", methods=["GET", "POST"])
@login_required
def details(id):
    pot = Pot.query.get(id)

    #checking if sync button was clicked
    result_values = {}
    if request.args.get("sync") == "sync":
        if pot.status != "PRAZNA" and pot.plant_id:
            result_values = generate_values()

    #scheduling watering date
    next_watering = ""
    if pot.plant:
        next_watering = next_watering_date(pot.watering_date, pot.plant.watering)
    
    if result_values:
        if result_values["humidity"] > pot.plant.humidity:
            next_watering = next_watering + timedelta(days=1)
        elif result_values["humidity"] < pot.plant.humidity:
            pot.watering_date = datetime.now()
            next_watering = next_watering_date(pot.watering_date, pot.plant.watering)
            db.session.commit()
    
    form = CreateUpdatePotForm()
    form.planted_plant.choices = [("", "---")]+[(i.id, i.name) for i in Plant.query.all()]

    if form.validate_on_submit():
        pot.location_name = form.location_name.data
        pot.status = empty_pot(form.planted_plant.data, form.status.data)
        pot.plant_id = form.planted_plant.data

        if next_watering == pot.watering_date:
            pot.watering_date = datetime.now()
        
        pot.watering_date = check_watering(form.watering.data, pot.watering_date)
        db.session.commit()
        return redirect(url_for("pot.details", id=id))
  
    form.location_name.data = pot.location_name
    form.status.data = pot.status
    form.planted_plant.data = str(pot.plant_id)

    return render_template(
        "pots/details.html", pot=pot, form=form, result_values=result_values, next_watering=next_watering
        )


@pot.route("/create_pot", methods=["GET", "POST"])
@login_required
def create():
    form = CreateUpdatePotForm()
    form.planted_plant.choices = [("", "---")]+[(i.id, i.name) for i in Plant.query.all()]

    if form.validate_on_submit():
        pot = Pot(
            location_name = form.location_name.data,
            status = empty_pot(form.planted_plant.data, form.status.data),
            plant_id = form.planted_plant.data,
            watering_date = datetime.now()
        )

        db.session.add(pot)
        db.session.commit()
        flash("Posuda je uspješno kreirana.", "success")
        return redirect(url_for("home.index"))

    return render_template("pots/create.html", form=form)


@pot.route("/delete_pot/<id>", methods=["GET", "POST"])
@login_required
def delete(id):
    pot = Pot.query.get(id)
    db.session.delete(pot)
    db.session.commit()
    return redirect(url_for("home.index"))