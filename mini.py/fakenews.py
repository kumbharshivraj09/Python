import random

celibraties=[
"virat kohali",
"akshay kumar",
"Messi",
"ronaldo",
"Prime minister",
"Rohit Sharma",
"Dhoni"

]

subject=[
    "lounches",
    "cancel",
    "dancing with",
    "eats",
    "declares war on"
    "play football"
    "celebrates"
]

actions=[
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "during ipl match",
    "in india gate"
    "team"
]

while True:
    cel=random.choice(celibraties)
    sub=random.choice(subject)
    act=random.choice(actions)
    headlines=f"BREAKING NEWS : {cel} {sub} {act}"
    print('\n ' + headlines)
    user_input=input('\ndo you want another headlines?(yes/no)').strip().lower()
    if user_input=='no':
     break 
print("thanks for using the fake news !")