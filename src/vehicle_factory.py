import fileinput
import glob
import json
import logging

from dataclass.vehicles.bike import Bike
from dataclass.vehicles.car import Car


class VehicleFactory:
    def __init__(self) -> None:
        self.vehicles = []
        
    def load_data(self) -> None:
        """Fetches JSONs from data directory and creates the corresponding Vehicle object"""
        logging.info('Loading data...')
        
        file_paths = glob.glob("data/**/*.dat", recursive=True)
        with fileinput.input(files=file_paths) as files:
            try:
                for f in files:
                    data = json.loads(f)
                    if data['type'] == 'auto':
                        self.vehicles.append(Car(data['marka'], data['ajtok_szama']))
                    elif data['type'] == 'bicikli':
                        self.vehicles.append(Bike(data['marka'], data['terhelhetoseg']))
                    else:
                        raise TypeError(f'Unknown type given ({data["type"]})...')
            except json.decoder.JSONDecodeError:
                logging.error('The files must contain only JSON objects! Aborting operation...')
        
    def print(self):
        """Prints and formats already loaded vehicles"""
        print(*self.vehicles, sep='\n')
    