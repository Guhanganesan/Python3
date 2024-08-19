# Python program to remove given element from the list
lst = ['Iris', 'Orchids', 'Rose', 'Lavender',
	'Lily', 'Carnations']
print("Original List is :", lst)

# using discard() method to remove list element 'orchids'
lst1 = filter(lambda item: item!='Orchids',lst)

print("List after element removal is :", list(lst1))


# Example 2

import itertools

lst = [1, 9, 8, 4, 9, 2, 9]
print("Original List is :", lst)

# itertools.filterfalse() to filter out all occurrences of 9 from the list
lst_filtered = list(itertools.filterfalse(lambda x: x == 9, lst))
print("List after element removal is :", lst_filtered)
#this code is contributed by Jyothi pinjala.