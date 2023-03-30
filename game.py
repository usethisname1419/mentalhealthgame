def title():
    print(" |\/| /__ |\ | T  /\ |   ")
    print(" |  | |__ | \| | /  \|__ ")
title()
print("The deadly game of insufficient mental health")

print("Welcome, what is your name?")
name = input("Enter Your Name:    ")
print(name, "is running out of medication and without it bad things can happen. What are you going to do?")


print('\n',
"self medicate(1)",
"call pharmacy(2)",
"call psychiatrist(3)",
"call mentalhealth(4)",
)
todo = input("What are you going to do?")
if todo == "1":
    print("ahh your going through drug crazed psychosis, you feel fine but this can't keep going on like this")
if todo == "2":
    print("You have been on hold for a while, finally you get through and they cannot perscribe you your meds because of some bullshit polocies, they say call psychiatrist")
if todo == "3":
    print("The psychiatrist says he wont refill the meds until we have met, appointment is in 3 months")
if todo == "4":
    print("These guys tell you if you want meds you gotta pay because no meds are covered")
