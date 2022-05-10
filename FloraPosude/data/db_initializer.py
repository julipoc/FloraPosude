from datetime import datetime

from FloraPosude import db

from FloraPosude.models.user import User
from FloraPosude.models.plant import Plant
from FloraPosude.models.pot import Pot


def db_initialize():
    user = User(
        first_name="Julija",
        last_name="Počekal", 
        username="jpocekal", 
        password="123456"
        )
    db.session.add(user)
    db.session.commit()

    plant_1 = Plant(
        name = "Aloa Vera",
        image = "aloje-vera.jpg",
        watering = "Tjedno",
        humidity = 20.0,
        temperature = 22.0,
        place = "Svjetlije",
        substrate_addition = True,
        ph_value = 6,
        description = """
            Aloe vera je drevna afrička biljka, a danas je jedna od najpopularnijih biljaka zbog ljekovitih svojstava
             i široke primjene u kozmetičkoj i farmaceutskoj industriji.
        """
    )

    db.session.add(plant_1)
    db.session.commit()

    plant_2 = Plant(
        name = "Begonija",
        image = "begonija.jpg",
        watering = "Tjedno",
        humidity = 50.0,
        temperature = 20,
        place = "Svjetlije",
        substrate_addition = True, 
        ph_value = 8,
        description = """
            Begonija spada u porodicu Begoniaceae (hrv. Begonijevke), jednogodišnjih i višegodišnjih trajnica,
            polugrmova i grmova. U hladnijim podnebljima uzgaja se kao sobna biljka i iznosi se samo ljeti.
        """
    )

    db.session.add(plant_2)
    db.session.commit()

    plant_3 = Plant(
        name = "Ciklama",
        image = "ciklama.jpg",
        watering = "Dnevno",
        humidity = 55.0,
        temperature = 18,
        place = "Tamnije",
        substrate_addition = True,
        ph_value = 7.5,
        description = """
            Ciklama (lat. Cyclamen persicum) koja se još naziva i "cvijet iskrenosti" pripada porodici jaglaca,
            a prepoznatljiva je po ružičastim ili bijelim cvjetovima koji rastu poviše tamnozelenih srcolikih listova.
        """
    )

    db.session.add(plant_3)
    db.session.commit()

    plant_4 = Plant(
        name = "Dalija",
        image = "dalija.jpg",
        watering = "Mjesečno",
        humidity = 30.0,
        temperature = 6.0,
        place = "Tamnije",
        substrate_addition = True,
        ph_value = 7,
        description = """
            Dalija (lat. Dahlia variabilis) je rod zeljastih trajnica iz porodice Asteraceae, 
            a prirodno raste na području Meksika. Rod sadrži 42 vrste i nekoliko tisuća hibrida.
        """
    )

    db.session.add(plant_4)
    db.session.commit()

    plant_5 = Plant(
        name = "Fuksija",
        image = "fuksija.jpg",
        watering = "Dnevno",
        humidity = 30.0,
        temperature = 12.0,
        place = "Svjetlije",
        substrate_addition = True,
        ph_value = 5,
        description = """
            Fuksija (lat. Fuchsia x hybrida) ukrasna je trajnica iz porodice vrbolikovki koja je
            najviše raširena u suptropskoj Americi, a ima više od 840 vrsta
        """

    )

    db.session.add(plant_5)
    db.session.commit()

    plant_6 = Plant(
        name = "Ječam",
        image = "jecam.jpg",
        watering = "Tjedno",
        humidity = 5.0,
        temperature = 15.0,
        place = "Svjetlije",
        substrate_addition = False,
        ph_value = 8,
        description = """
            Ječam (lat. Hordeum vulgare L.) pripada rodu Hordeum, odnosno rodu jednogodišnjih i dvogodišnjih raslinja 
            i trajnica iz porodice trava (lat. Poaceae).
        """
    )

    db.session.add(plant_6)
    db.session.commit()

    plant_7 = Plant(
        name = "Kadulja",
        image = "kadulja.jpg",
        watering = "Mjesečno",
        humidity = 15.0,
        temperature = 14.0,
        place = "Tamnije",
        substrate_addition = False,
        ph_value = 8,
        description = """
            Kadulja (lat. Salvia officinalis) samo je jedan naziv za dobro poznatu ljekovitu biljku koja se još naziva žalfija
             i mirišljava kadulja, ljekovita kadulja ili ljekovita žalfija.
        """
    )

    db.session.add(plant_7)
    db.session.commit()

    plant_8 = Plant(
        name = "Majčina dušica",
        image = "majcina-dusica.jpg",
        watering = "Mjesečno",
        humidity = 30.0,
        temperature = 18.0,
        place = "Svjetlije",
        substrate_addition = False,
        ph_value = 4,
        description = """
            Majčina dušica (lat. Thymus serpyllum) jedna je od vrsta timijana koji su rod usnača. U narodu se prava 
            majčina dušica još može naći i pod imenom babina dušica, timijan, divlji bosiljak ili maternika. 
        """
    )

    db.session.add(plant_8)
    db.session.commit()

    plant_9 = Plant(
        name = "Maćuhica",
        image = "macuhica.jpg",
        watering = "Tjedno",
        humidity = 15.0,
        temperature = 17.0,
        place = "Svjetlije",
        substrate_addition = True,
        ph_value = 7,
        description = """
            Maćuhica (lat. Viola tricolor) je poznata i česta livadna biljka iz porodice Violaceae. Narodni nazivi za ovaj cvijet 
            su gospina ljubica, sirotica, poljska ljubica, dan i noć te božji cvit.
        """
    )

    db.session.add(plant_9)
    db.session.commit()

    plant_10 = Plant(
        name = "Ljubičica",
        image = "ljubicica.jpg",
        watering = "Dnevno",
        humidity = 70.0,
        temperature = 20.0,
        place = "Svjetlije",
        substrate_addition = True,
        ph_value = 6,
        description = """
            Ljubičica (lat. Viola) je trajna cvjetnica iz porodice ljubičarki. Radi se o porodici 
            s 25 rodova od kojeg su najveći ljubice s 480 vrsta.
        """
    )

    db.session.add(plant_10)
    db.session.commit()


    pot = Pot(
        location_name = "Prozor u dnevnoj sobi",
        status = "PRAZNA",
        watering_date = datetime.now()
    )

    db.session.add(pot)
    db.session.commit()