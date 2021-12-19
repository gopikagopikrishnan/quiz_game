print("Hey! Welcome to Techno Quiz :)")
a = input("Would you like to play the game now?")
a = a.lower()
if a != "yes":
    print("Thanks for choosing us! See u next time")
    quit()
print("Ok, Let's play!")
point = 0
q1 = input("Who's is the father of computer? ")
q1 = q1.lower()
if q1 == "charles babbage":
    print("Correct, 1 point for you")
    point +=1
else:
    print("Sorry! Wrong")
q1 = input("What is the new name of Facebook? ")
q1 = q1.lower()
if q1 == "meta":
    print("Correct, 1 point for you")
    point +=1
else:
    print("Sorry! Wrong")
q1 = input("Which is the first programming language? ")
q1 = q1.lower()
if q1 == "fortran":
    print("Correct, 1 point for you")
    point +=1
else:
    print("Sorry! Wrong")
q1 = input("Who developed Python language? ")
q1 = q1.lower()
if q1 == "guido van rossum":
    print("Correct, 1 point for you")
    point +=1
else:
    print("Sorry! Wrong")
q1 = input("Who developed C language? ")
q1 = q1.lower()
if q1 == "dennis ritchie":
    print("Correct, 1 point for you")
    point +=1
else:
    print("Sorry! Wrong")
print("Thanks for playing, you scored",point,"/5")

    
