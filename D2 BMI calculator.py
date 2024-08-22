# 1st input: enter height in meters e.g: 1.65
height = input("Height: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Weight: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

new_h = float(height)
new_w = int(weight)
print("Your BMI is " + str(int(new_w / (new_h * new_h))))