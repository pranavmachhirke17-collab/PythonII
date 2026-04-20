class vehicle:
    def move(self):
        print("The vehicle is moving.")

class car(vehicle):
    def move(self):
        print("Driving on the road.")
class bicycle(vehicle):
    def move(self):
        print("Pedaling on the road.")

vehicle = [car(), bicycle()]
for v in vehicle:
    v.move()