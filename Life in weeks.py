age = input("Age? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
#one year has 52 weeks
new_age = int(age)
full_life = 90 * 52
weeks = (52)
#How much we already lived
weeks_lived = new_age * weeks
weeks_left = f"You have {full_life - weeks_lived} weeks left."
print(weeks_left)