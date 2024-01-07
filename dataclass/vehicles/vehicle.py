from abc import ABC

from dataclasses import dataclass


@dataclass
class Vehicle(ABC):
    brand: str
    