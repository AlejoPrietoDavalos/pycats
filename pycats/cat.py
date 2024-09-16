from typing import Literal, List, Generator
from datetime import date

from pydantic import BaseModel, Field
import pandas as pd


class Weight(BaseModel):
    weight: float
    date: date

class Cat(BaseModel):
    name: str
    unit: Literal["kg"] = "kg"
    weights: List[Weight] = Field(default_factory=list)

    def get_df_weights(self) -> pd.DataFrame:
        return pd.DataFrame([w.model_dump() for w in self.weights])

class Cats:
    def __init__(self, *, cats: List[Cat]):
        assert all(isinstance(c, Cat) for c in cats)
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
