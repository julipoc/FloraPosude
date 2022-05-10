import random


def generate_values():
    levels = ["Niska", "Visoka", "Srednja"]

    values = {
        "temperature" : round(random.uniform(-10.5, 35.5), 1),
        "humidity" : round(random.uniform(0, 100), 1),
        "light_level" : random.choice(levels),
        "ph_value" : random.randint(1,14)
    }

    return values

    

