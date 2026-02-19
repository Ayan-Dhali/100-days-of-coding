print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?\n"))
tip=float(input("How much tip would you like to give?10,12 or 15?\n"))
split=float(input("How many person should pay:\n"))

total_tip=bill*(tip/100)
bill_for_each=round((bill+total_tip)/split,3)
print(f"Each person should pay:{bill_for_each}")