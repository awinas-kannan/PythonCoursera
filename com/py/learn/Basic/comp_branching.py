my_age = 19

if (my_age < 18):
    print("below voting age")
elif my_age == 18:
    print("reached voting age")
else:
    print("Voting age")

my_dob_year = 2001

if (my_dob_year > 1990 and my_dob_year < 1999):
    print("90's kid")
elif (my_dob_year > 2000 or my_dob_year > 2050):
    print("2k kid")

print(not (my_dob_year > 2000))
