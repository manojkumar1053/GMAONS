ages = {

    'jim': 30,
    'pam': 28,
    'kevin': 33

}

person = input('get the age for: ')
try:
    print(f'{person} is {ages[person]} years')
except KeyError:
    print(f"{person}'s age is unknown. ")
