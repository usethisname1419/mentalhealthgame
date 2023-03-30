
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
print("")
print("With no meds all you can do is goto a institution or try handle it out here, so whats your next move", name)
print('\n',
"goto institution(1)",
"handle it(2)",
)

whatnext = input("Make your choice")
if whatnext == "1":
    print("So long buddy, you won't get much care and you will have a hell of a time getting out, should of handled it man")
if whatnext == "2":
    print(name, "might make it, stay calm, take it easy and maybe smoke some weed, we going to get our meds in a month or two")
print("")
input("Game is done. write 'exit'     ")
print ("\n" * 100)
print("They make getting meds that you need to take really hard to do, there is always something going wrong. Front line staff are ill equipped "
      "to deal with mental healt patients. Staff always seem to get a mental health emergency with drug use and that can cause them to "
      "not give you the proper care. If you are having mental health issues or need a medication plan changed a bit, you should be able to goto "
      "a hospital and get treatment and if you were sick or injured, not make you wait 3 or 4 more months to see a mental health doctor")
