family = ["nato", "edemi", "aleko", "beqa"]
ages = [50, 55, 15, 22]

ages_in_10_years = [age + 10 for age in ages]

name = "My mom's name is: {},My father's name is: {}, My brother's name is: {}, My name is: {}".format(family[0], family[1], family[3], family[2])
age_10_years_later = "We are {} years old, and in 10 years, we will be {} years old.".format(
    ', '.join([str(age) for age in ages]), #                                                    
    ', '.join([str(age) for age in ages_in_10_years])
)

print(name)
print(age_10_years_later)
