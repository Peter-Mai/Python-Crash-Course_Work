#3.6 More Guests 

guest = ['Tokido', 'JDCR', 'Mkleo']

print(f"{guest[0].title()}, I would like to invite you to dinner.")

print(f"{guest[1].title()}, I would like to invite you to dinner.")

print(f"{guest[2].title()}, I would like to invite you to dinner.")

print(f"{guest[2]}, can't actually make it.")

#Mkleo couldn't make it so we are now adding Sonicfox

del(guest[2])
guest.insert(2, "Sonicfox")

print(f"{guest[0].title()}, I would like to invite you to dinner.")

print(f"{guest[1].title()}, I would like to invite you to dinner.")

print(f"{guest[2].title()}, I would like to invite you to dinner.")

print("We found an even BIGGER table!")

#Adding a guest to the beginning of the list
guest.insert(0, "Aris")

#Add guest to the middle of the list 
guest.insert(2, "Sajam")

#Add gguest to the end of the list
guest.insert(-1, "TastySteve")

print(f"{guest[0].title()}, I would like to invite you to dinner.")

print(f"{guest[1].title()}, I would like to invite you to dinner.")

print(f"{guest[2].title()}, I would like to invite you to dinner.")

print(f"{guest[3].title()}, I would like to invite you to dinner.")

print(f"{guest[4].title()}, I would like to invite you to dinner.")

print(f"{guest[5].title()}, I would like to invite you to dinner.")