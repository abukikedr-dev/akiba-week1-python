destination = input("Destination: ")
distance = float(input("Distance in km: "))
speed = float(input("Average Speed in km/h: "))

travel_time = distance / speed

print()
print("Destination:", destination)
print("Distance:", distance, "km")
print("Average Speed:", speed, "km/h")
print("Estimated Travel Time:", travel_time, "hours")