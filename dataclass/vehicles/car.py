from dataclasses import dataclass

from .vehicle import Vehicle


@dataclass
class Car(Vehicle):
    number_of_doors: int
