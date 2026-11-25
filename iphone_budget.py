#Goal
#Create a program that helps the user make a financially responsible decision about buying a new iPhone
#and decides whether they can buy the new phone  
#or not

#START
#ASK the user how much available money do you currently have
#STORE the answer/input
# IF money (input) is less than 1000
#   DISPLAY "It is still too early to buy a new phone."
#ELSE IF money(input) is less than 2000 
#   DISPLAY "You should save a little more."
#ELSE IF money (input) is less than 3200
#   DISPLAY "You're almost there."
#ELSE 
#   DISPLAY "Congratulations for saving enough, you can go buy the new phone."


money = int(input("How much available money do you currently have:"))

if money < 1000:
    print("It is still too early to buy a new phone.")
elif money < 2000:
    print("You should save a little more.")
elif money < 3200:
    print("You're almost there.")
else:
    print("Congratulations for saving enough, you can go buy the new phone.")