# Learn Python the Hard Way - Exercise No. 4
# Set the cars equal to 100
cars = 100
# set the space in the car to float 4
space_in_a_car = 4.0
# Set the drivers equal to 30
drivers = 30
# Set the passengers equal to 90
passengers = 90
# Calculate how many cars can be driven, given no. of drivers.
cars_not_driven = cars - drivers
# Set one driver per car
cars_driven = drivers
# Calculate how many people can be transported total
carpool_capacity = cars_driven * space_in_a_car
# Calculate passengers per car
average_passengers_per_car = passengers / cars_driven

#Print report on carring.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."