
print("Welcome to the Tip calculator!")

price = float(input("ENTER THE BILL PRICE $: \n"))

tip = int(input("What presentage tip whould you like to give? 10 , 12 or 15 ? :"))

people = int(input("How many people to split the bill? : "))

bill = tip/100 * price + price
bill_per_person = bill / people
round_value = round(bill_per_person, 2)
round_value = "{:.2f}".format(bill_per_person)

print(f"Each person should pay {round_value} ")
