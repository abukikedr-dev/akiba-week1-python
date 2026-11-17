# BMI calculculator

name = input("Enter your name: ")
weight_kg = float(input("Enter your weight in kilograms (kg): "))
height_m = float(input("Enter your height in meters (m): "))

bmi_value = weight_kg / (height_m * height_m)


print("=" * 30)
print("BMI HEALTH REPORT")
print("=" * 30)
print("Name: ", name)
print("Weight: ", weight_kg, "kg")
print("Height: ", height_m, "m")
print("-" * 30)
print("Your BMI Result: ", (round(bmi_value, 2)), "kg/m^2")
print("=" * 30)