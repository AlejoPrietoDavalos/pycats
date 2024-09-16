from typing import List
from datetime import date

from pycats.cat import Cats, Cat, Weight, AntiParasitic

KG = "kg"
EPSILON = "Épsilon"
CURIE = "Curie"
GAUSS = "Gauss"

ANTI_PARASITIC_APRAX = "APRAX Raza mediana 3/4 de pastilla"

def get_epsilon() -> Cat:
    return Cat(
        name=EPSILON,
        unit=KG,
        color_hex="#08acd1",
        weights=[
            Weight(weight=6.20, date=date(2024,9,11))
        ],
        anti_parasitic=[
            AntiParasitic(name=ANTI_PARASITIC_APRAX, date=date(2024,9,15))
        ]
    )

def get_curie() -> Cat:
    return Cat(
        name=CURIE,
        unit=KG,
        color_hex="#e87827",
        weights=[
            Weight(weight=6.25, date=date(2024,9,11))
        ],
        anti_parasitic=[
            AntiParasitic(name=ANTI_PARASITIC_APRAX, date=date(2024,9,15))
        ]
    )

def get_gauss() -> Cat:
    return Cat(
        name=GAUSS,
        unit=KG,
        color_hex="#03826d",
        weights=[
            Weight(weight=6.20, date=date(2024,9,11))
        ],
        anti_parasitic=[
            AntiParasitic(name=ANTI_PARASITIC_APRAX, date=date(2024,9,15))
        ]
    )

def get_cats() -> Cats:
    return Cats(cats=[get_epsilon(), get_curie(), get_gauss()])