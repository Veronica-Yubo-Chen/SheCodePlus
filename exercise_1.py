user_input = float(input("How many kilometers? "))
miles = user_input * 0.621371
meters = int(user_input * 1000)
centimeters = int(user_input * 100000)
print(f"{user_input} km = {miles} miles")
print(f"{user_input} km = {meters} meters")
print(f"{user_input} km = {centimeters} centimeters")