class Car(object):
    condition='new'
    def __init__(self,model,color,mpg):
        self.model=model
        self.color=color
        self.mpg=mpg
my_car = Car('Colorado','red',23)

print("I drive a Chevy", my_car.model, "it is",my_car.color, "and it only gets",my_car.mpg,"miles to the gallon")

