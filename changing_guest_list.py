#3.5 Changing Guest List 

dinner = ['Tokido', 'JDCR', 'Mkleo']

print(f"{dinner[0].title()}, I would like to invite you to dinner.")

print(f"{dinner[1].title()}, I would like to invite you to dinner.")

print(f"{dinner[2].title()}, I would like to invite you to dinner.")

print(f"{dinner[2]}, can't actually make it.")

#Mkleo couldn't make it so we are now adding Sonicfox

del(dinner[2])
dinner.insert(2, "Sonicfox")

print(f"{dinner[0].title()}, I would like to invite you to dinner.")

print(f"{dinner[1].title()}, I would like to invite you to dinner.")

print(f"{dinner[2].title()}, I would like to invite you to dinner.")