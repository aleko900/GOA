#1

def sides_of_a_tringle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("ასეთი სამკუთედი იარსებებს")
    else:
        print("ასეთი სამკუთხედი ვერ იარსებებს")

sides_of_a_tringle(60, 60, 60,)
sides_of_a_tringle(3, 7, 11,)

#2
def names(aleko, beqa, saba):
    names_list = [aleko, beqa, saba]
    names_str = ", ".join(names_list)
    print("names: " + names_str)

names("aleko", "beqa", "saba")