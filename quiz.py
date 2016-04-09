# Music Quiz Program
# Written by Maho

score = 0

question1 = input("Who sings 'Shut up and Dance'? ")
if question1.lower() == "walk the moon":
    print("You are a genius")
    score = score + 2
else:
    print("Divvy!")
    score = score - 1

question2 = input("Who sings 'Love Me Like You Do'? ")
if question2.lower() == "ellie goulding":
    print("You are a genius")
    score = score + 2
else:
    print("Divvy!")
    score = score - 1

question3 = input("Who sings 'Sax'? ")
if question3.lower() == "fleur east":
    print("You are a genius")
    score = score + 2
else:
    print("Divvy!")
    score = score - 1

print("Your final score is", score)
