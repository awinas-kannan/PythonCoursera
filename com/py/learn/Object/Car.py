class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed


honda_city = Car("HONDA", "2002", "blue", 100)
print(honda_city.get_speed())
tata_nexon = Car("TATA", "2020", "blue")
print(tata_nexon.get_speed())

honda_city.accelerate(100)
tata_nexon.accelerate(50)

# Print the current speeds of the cars
print(f"{honda_city.make} {honda_city.model} is currently at {honda_city.get_speed()} km/h.")
print(f"{tata_nexon.make} {tata_nexon.model} is currently at {tata_nexon.get_speed()} km/h.")
