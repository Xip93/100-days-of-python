#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give?\n"))
people = int(input("How many people split the bill?\n"))
tip_percent = float((tip / 100) * total_bill)

new_total = total_bill + tip_percent

each_person = (new_total / people)

print(f'Each person has to pay {each_person: .2f}')
