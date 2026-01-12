#set - duplicate allowed,unordered.

myset={4,'a','b',45,7.9,4}
print(type(myset))
print(myset)
myset.add('pune')
#print(myset)
myset.add('a')
print(myset)

list=['monday','sunday','friday','saturday','wendsday','monday','sunday']

day=set(list)
print(day)