def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (True if distance_to_pump/mpg<=fuel_left else False)
# Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.