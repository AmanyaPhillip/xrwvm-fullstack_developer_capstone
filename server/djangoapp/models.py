from django.db import models
# F401: 'django.utils.timezone.now' imported but unused - REMOVED
# E261: at least two spaces before inline comment
# E501: line too long (101 > 79 characters)


# E302: expected 2 blank lines, found 1 - ADDED
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        # E501: line too long (83 > 79 characters) - BROKEN
        # E261: at least two spaces before inline comment - ADDED
        return (f"Name: {self.name}, "  # E114/E116: indentation for comments
                f"Description: {self.description}")  # E501: Line too long


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100, choices=[  # E261, E501
        ('sedan', 'Sedan'), ('suv', 'SUV'),
        ('wagon', 'Wagon'), ('truck', 'Truck'),
        ('van', 'Van'), ('sports', 'Sports Car'),
        ('convertible', 'Convertible'),
        ('hatchback', 'Hatchback'), ('coupe', 'Coupe'), ('minivan', 'Minivan')
    ], default='sedan')
    year = models.IntegerField()  # E261, E501: Assuming a year like 2023

    def __str__(self):
        return (f"Name: {self.name}, "
                f"Make: {self.car_make.name}, "
                f"Type: {self.car_type}, "
                f"Year: {self.year}")


class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long,
                 short_name, st, zip):
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
        return f"Dealer name: {self.full_name}, State: {self.st}"


class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date,
                 car_make, car_model, car_year, sentiment):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment

    def __str__(self):
        # E261: at least two spaces before inline comment - ADDED
        # E501: line too long (89 > 79 characters) - BROKEN
        return (f"Review: {self.review}, "
                f"Sentiment: {self.sentiment}")  # E501: Line too long

# W293: blank line contains whitespace - REMOVED trailing whitespace
