
name = input("Enter the user's name: ")
age = int(input("Enter the user's age: "))
if name.lower() == "mate":
    print(f"Happy birthday, {name.capitalize()}! You have attended many, you turned {age + 1} years old.")
else:
    print("Not Mate's birthday.")