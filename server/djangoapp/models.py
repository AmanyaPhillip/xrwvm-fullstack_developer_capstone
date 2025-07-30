from django.db import models
from django.utils.timezone import now # F401: This import seems unused. If not used later, remove it.

# E303, E302: Reduce blank lines to 2 between top-level class/function definitions.

# <--- Ensure 2 blank lines here --->
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description # E501: Break long line
                                                  # E128: Align continuation line.
                                                  # E501: Line is 95 chars, needs breaking.

# <--- Ensure 2 blank lines here --->
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) # Many-to-one relationship
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100, choices=[ # E501: Line is 95 chars, needs breaking.
        ('sedan', 'Sedan'), ('suv', 'SUV'), ('wagon', 'Wagon'), ('truck', 'Truck'), ('van', 'Van'),
        ('sports', 'Sports Car'), ('convertible', 'Convertible'), ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'), ('minivan', 'Minivan')
    ], default='sedan')
    year = models.IntegerField() # Assuming a year like 2023

    def __str__(self):
        # E128: Align continuation line with the opening parenthesis of the value.
        return (f"Name: {self.name}, "
                f"Make: {self.car_make.name}, "
                f"Type: {self.car_type}, "
                f"Year: {self.year}") # E501: Line is 95 chars, needs breaking.

# <--- Ensure 2 blank lines here --->
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip): # Line 30, E128
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        # E128: Align continuation lines.
        return "Dealer name: " + self.full_name + ", " + \
               "State: " + self.st # E501: Line is 95 chars, needs breaking.

# <--- Ensure 2 blank lines here --->
class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment # This will be added by the sentiment analysis service
    
    def __str__(self):
        # E128: Align continuation lines.
        return "Review: " + self.review + ", " + \
               "Sentiment: " + self.sentiment # E501: Line is 95 chars, needs breaking.

# W391: Remove any blank lines at the very end of the file.
