import sys

weight = float(input("What is your weight in pounds?: "))
height = float(input("What is your height in inches?: "))
BMI = (703 * weight) / (height ** 2)
print("Your body mass index (BMI) is " + str(BMI) + "%")
