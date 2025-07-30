from .models import CarMake, CarModel # E302: Added 1 blank line
from django.db.models import F

def initiate():
    # E231: Missing whitespace after ':'. Add space after colons in dictionary literals.
    # E501: Break long lines.
    car_make_data = [
        {"name": "Nissan", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes-Benz", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Honda", "description": "Great cars. Japanese technology"},
    ]

    for data in car_make_data: # E117: This loop should not be over-indented.
        CarMake.objects.create(name=data['name'], description=data['description']) # E501: Line too long.

    # E303: Remove extra blank line.
    # E231, E501: Add whitespace after colons and break long lines.
    car_model_data = [
        {"car_make": "Nissan", "name": "Pathfinder", "type": "SUV", "year": 2023},
        {"car_make": "Nissan", "name": "Frontier", "type": "Truck", "year": 2023},
        {"car_make": "Nissan", "name": "Leaf", "type": "Sedan", "year": 2023},
        {"car_make": "Mercedes-Benz", "name": "C-Class", "type": "Sedan", "year": 2023},
        {"car_make": "Mercedes-Benz", "name": "E-Class", "type": "Sedan", "year": 2023},
        {"car_make": "Mercedes-Benz", "name": "GLC SUV", "type": "SUV", "year": 2023},
        {"car_make": "Audi", "name": "A4", "type": "Sedan", "year": 2023},
        {"car_make": "Audi", "name": "Q5", "type": "SUV", "year": 2023},
        {"car_make": "Audi", "name": "e-tron", "type": "SUV", "year": 2023},
        {"car_make": "Kia", "name": "Telluride", "type": "SUV", "year": 2023},
        {"car_make": "Kia", "name": "Sorento", "type": "SUV", "year": 2023},
        {"car_make": "Kia", "name": "Forte", "type": "Sedan", "year": 2023},
        {"car_make": "Honda", "name": "CR-V", "type": "SUV", "year": 2023},
        {"car_make": "Honda", "name": "Civic", "type": "Sedan", "year": 2023},
        {"car_make": "Honda", "name": "Pilot", "type": "SUV", "year": 2023},
    ]

    for data in car_model_data: # E117: This loop should not be over-indented.
        # E131: Align continuation line for hanging indent.
        car_make_instance = CarMake.objects.get(name=data['car_make'])
        CarModel.objects.create(
            car_make=car_make_instance,
            name=data['name'],
            car_type=data['type'],
            year=data['year']
        ) # E501: Line too long. Break into multiple lines for readability.

# W292: Add a newline at the very end of the file.
