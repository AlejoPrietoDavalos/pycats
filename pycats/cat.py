from typing import Literal, List, Generator
from datetime import date

from pydantic import BaseModel, Field
import pandas as pd

KG = "kg"


class Weight(BaseModel):
    weight: float
    date: date

class AntiParasitic(BaseModel):
    name: str
    date: date

class Cat(BaseModel):
    name: str
    color_hex: str = Field(description="Color de los plots asociados.")
    unit: Literal["kg"] = KG
    weights: List[Weight] = Field(default_factory=list)
    anti_parasitic: List[AntiParasitic] = Field(default_factory=list)

    def get_df_weights(self) -> pd.DataFrame:
        return pd.DataFrame([w.model_dump() for w in self.weights])

class Cats:
    def __init__(self, *, cats: List[Cat]):
        assert all(isinstance(c, Cat) for c in cats)
        assert all(c.unit == KG for c in cats)  # FIXME: Solo se inserta en kg.
        self.unit = KG
        self.names = []
        self.cats = {}
        for c in cats:
            self.names.append(c.name)
            self.cats[c.name] = c
    
    def __getitem__(self, name: str) -> Cat:
        return self.cats[name]
    
    def iter_cats(self) -> Generator[Cat, None, None]:
        for name in self.names:
            yield self.cats[name]
