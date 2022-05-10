from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

from FloraPosude import db

from FloraPosude.models.plant import Plant
from FloraPosude.plants.forms import CreateUpdatePlantForm
from FloraPosude.helpers.save_image import save_image


plant = Blueprint("plant", __name__)


@plant.route("/plants", methods=["GET", "POST"])
@login_required
def index():
    plants = Plant.query.all()
    return render_template("plants/index.html", plants=plants)


@plant.route("/plants/<id>", methods=["GET", "POST"])
@login_required
def details(id):
    plant = Plant.query.get(id)
    form = CreateUpdatePlantForm()

    if form.validate_on_submit():
        plant.name = form.name.data
        plant.description = form.description.data
        plant.watering = form.watering.data
        plant.humidity = form.humidity.data
        plant.temperature = form.temperature.data
        plant.substrate_addition = form.substrate_addition.data
        plant.place = form.place.data
        plant.ph_value = form.ph_value.data

        if str(form.image.data) == "<FileStorage: '' ('application/octet-stream')>":
            plant.image = plant.image
        else:
            plant.image = save_image(form.image.data) 

        db.session.commit()
        return redirect(url_for("plant.details", id=id))
    
    form.name.data = plant.name
    form.description.data = plant.description
    form.watering.data = plant.watering
    form.humidity.data = plant.humidity
    form.place.data = plant.place
    form.temperature.data = plant.temperature
    form.substrate_addition.data = plant.substrate_addition
    form.image.data = plant.image
    form.ph_value.data = plant.ph_value

    return render_template("plants/details.html", plant=plant, form=form)


@plant.route("/create_plant", methods=["GET", "POST"])
@login_required
def create():
    form = CreateUpdatePlantForm()

    if form.validate_on_submit():
        plant = Plant(
            name = form.name.data,
            description = form.description.data,
            humidity = form.humidity.data,
            temperature = form.temperature.data,
            substrate_addition = form.substrate_addition.data,
            watering = form.watering.data,
            place = form.place.data,
            ph_value = form.ph_value.data
        )

        if str(form.image.data) == "<FileStorage: '' ('application/octet-stream')>":
            plant.image = ""
        else:
            plant.image = save_image(form.image.data)

        db.session.add(plant)
        db.session.commit()
        flash("Biljka je uspješno kreirana.", "success")
        return redirect(url_for("plant.index")) 
        
    return render_template("plants/create.html", form=form)


@plant.route("/delete_plant/<id>", methods=["GET", "POST"])
@login_required
def delete(id):
    plant = Plant.query.get(id)
    db.session.delete(plant)
    db.session.commit()
    flash("Biljka je uspješno obrisana!", "success")
    return redirect(url_for("plant.index"))