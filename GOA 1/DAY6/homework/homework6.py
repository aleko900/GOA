
i = 1
while i <=30:
    print (i)
    i = i + 1   #ინკრემენტაცია(ზრდა)

print("finished")

def analyze_number(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

# Example usage:
number_to_analyze = 30  # Replace with the number you want to analyze
analyze_number(number_to_analyze)