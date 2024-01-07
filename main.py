import logging
from src.vehicle_factory import VehicleFactory


if __name__ == '__main__':
    """Example for the test program"""
    logging.getLogger().setLevel(logging.INFO)

    handler = VehicleFactory()
    handler.load_data()
    handler.print()
    