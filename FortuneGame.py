Numbers = [1,2,3,4,5,6,7,8]
ColorsEven = ["Purple", "Pink", "Blue", "Rainbow"]
ColorsOdd = ["Green","Yellow","Orange","Red"]
Fortunes = ["Remember what we say to the God of Death. 'Not Today.'", 
    "Play the lottery today! (The $1 scratcher, you're not feeling that lucky).",
    "Age is just a number, so is being rich.",
    "Try answering the phone, 'Ahoy!'",
    "Smile through the pain. Cry through the joy."]
AcceptInput = ["Yes","No"]

# Game
x = input("I see you are here for a fortune, is that correct?:")
if x not in AcceptInput :
    x = input("Speak plainly! 'Yes' or 'No'?!")
elif x == "No" :
    exit
else :
    print("Excellent, Please choose a number from this list " + str(Numbers))
CE = input()
if int(CE) not in Numbers:
    CE = input("Please choose a number btwn 1 and 8, I won't tell you again!")
else :
    if int(CE) % 2 == 0 :
        print("Great, please choose one of these colors " + str(ColorsEven))
        FE = input()
        if FE == "Purple" :
            print("Remember what we say to the God of Death. 'Not Today.'")
        elif FE == "Pink" :
            print("Play the lottery today! (The $1 scratcher, you're not feeling that lucky).")
        elif FE == "Blue" :
            print("Age is just a number, so is being rich.")
        elif FE == "Rainbow" :
            print("I see you like to live dangerously; try answering the phone, 'Ahoy!' today.")
    else :
        print ("Great, please choose one of these colors " + str(ColorsOdd))
        FO = input()
        if FO == "Green" :
            print("Smile through the pain. Cry through the joy.")
        elif FO == "Yellow" :
            print("One day you will cause an apocolypse. It will be an accident. Don't feel bad.")
        elif FO == "Orange" :
            print("Soon all your dreams will come true. Soon...")
        elif FO == "Red" :
            print("You were a matador in a previous life, perhaps that explains your choice")
input("Would you like a different fortune?")
print("Too bad, that's not how this works. That's not how any of this works!")
exit