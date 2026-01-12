person={
    'name':'ashish',
    'age':19,
    'city':'kolhapur',
    'college':'VCK',
    'percentage':'84.36'
}

print(person)
print(type(person))
print(person['age'])

#print(person['pass'])
print(person.get('pass'))


person['pass']='true'
print(person.get('pass'))

del person['college']
print(person)