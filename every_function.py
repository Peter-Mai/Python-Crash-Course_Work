# 3.10 Every Function

fighting_games = ['Street Fighter', 'Tekken', 'Guilty Gear', 'Melty Blood', 'Marvel vs Capcom', 'Under Night', 'King of Fighters', 'Dragonball Fighterz', 'Blazblue', 'Tekken', 'Killer Instinct', 'Virtua Fighter', 'Vampire Savior', 'Skullgirls']

#append, adds an item to the end of the list 
fighting_games.append('Cross Tag Battle')

#Insert, adds an item based on the index of the element
fighting_games.insert(3, 'Mortal Kombat')

#Delete, deleting item from list. Can be done from any position
del fighting_games[3]
print(fighting_games)

#Removing an item using the pop method. Removes item from the back of the list. "Can also be done from any position if specified"
popped_fighting_games = fighting_games.pop()
print(popped_fighting_games)

#Removing an item using remove, specifies the value of the item
fighting_games.remove('Cross Tag Battle')
print(fighting_games)

#Sorting a list permanently with sort. Alphabetically
fighting_games.sort()
print(fighting_games)

#Sorting temporarily with sorted
print(fighting_games)
print(sorted(fighting_games))

print(fighting_games)


#Reverse list order
print(fighting_games)
fighting_games.reverse()
print(fighting_games)

#Length of list 
len(fighting_games)

