from datetime import datetime, timedelta

from flask import flash


def empty_pot(plant, status):
    if plant == "" and status == "U REDU":
        flash("Status posude je promijenjen u PRAZNA jer joj nije dodijeljena biljka.", "warning")
        return "PRAZNA"
    elif plant != "" and status == "PRAZNA":
        flash("Status posude je promijenjen u U REDU jer joj je dodijeljena biljka.", "warning")
        return "U REDU"
    elif plant != "" and status == "POKVARENA":
        flash("Posuda je pokvarena! Preporučamo da ispraznite posudu.", "danger")
        return "POKVARENA"
    elif plant == "" and status == "POKVARENA":
        flash("Posuda je pokvarena! Preporučamo da obrišete posudu.", "danger")
        return "POKVARENA"
    elif plant == "":
        return "PRAZNA"
    else:
        return "U REDU"


def check_watering(watering, date):
    if watering:
        return datetime.now()
    else:
        return date


def next_watering_date(last_watering, watering_time):
    time = 0
    if watering_time == "Dnevno":
        time = 1
    elif watering_time == "Tjedno":
        time = 7
    elif watering_time == "Mjesečno":
        time = 30

    date = last_watering + timedelta(days=time)
    return date

