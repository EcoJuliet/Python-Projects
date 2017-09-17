'''# SOME FUNCTIONS
maximum = max(-10, 0, 10)
print (maximum)
# Prints the "largest" number of a string
minumim = min(-10, 0, 10)
print (minimum)
# Prints the 'smallest' number of a string
'type(x) returns the type of ar argument Python sees
Exemple:
print type(3)
print type(3.2)
print type('oi')
RETURNS:
<type 'int'>
<type 'float'>
<type 'str'>



# FUNCTIONS#
def speak(message):
    return message

if happy():
    speak("I'm happy!")
elif sad():
    speak("I'm sad.")
else:
    speak("I don't know what I'm feeling.")'''

# Hotel Costs
def hotel_cost(days):
    return 140*days
    
# Cities and the cost of traveling to them.
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
# Cost os Rental Car.
def rental_car_cost(days):
    cost = 40*days
    if days >= 7:
        cost -= 50
    elif days >=3:
        cost -= 20
    return cost
    
# Trip Cost (Modified)
def trip_cost(city, days, spending_money):
    return plane_ride_cost(city) + rental_car_cost(days)+hotel_cost(days)+spending_money
    
print ((trip_cost)('Los Angeles', 5, 600))
