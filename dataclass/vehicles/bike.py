from dataclasses import dataclass

from .vehicle import Vehicle


@dataclass
class Bike(Vehicle):
    load_capacity: int
