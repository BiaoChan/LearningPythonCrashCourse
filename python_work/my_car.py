from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# my_new_car.odometer_reading = 12
my_new_car.update_odometer(12)

my_new_car.read_odometer()

my_new_car.increment_odometer(12)
my_new_car.read_odometer()


print("\n")
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
