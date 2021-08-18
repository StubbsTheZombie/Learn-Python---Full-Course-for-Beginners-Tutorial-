'''
I wake up
If I'm hungry
    I eat breakfast

I leave my house
If it's cloudy
    I bring an umbrella
otherwise
    I bring sunglasses

I'm at a restaurant
If I want meat
    I order steak
Otherwise if I want pasta
    I order spaghetti & meatballs
otherwise
    I order salad
'''

#

is_male = True
is_tall = True
#or one or the other have to be correct
if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = False
#and both have to be true
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")