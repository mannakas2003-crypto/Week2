#Goal
#Create a program that asks the user for the current hour
#and decides whether they can watch another Telia TV episode 
#or should go to bed

#START
#ASK the user about the current hour
#STORE the answer/input
# IF hour (input) is less than 21
#   DISPLAY "Plenty of time. You can go for another episode."
#ELSE IF hour(input) is 22 
#   DISPLAY "One more episode is probably fine."
#ELSE 
#   DISPLAY "Time to go to bed."  
#END


hour = int(input("What time it is? Enter the current hour:"))

if hour < 21:
    print("Plenty of time. You can go for another episode.")
elif hour < 22:
    print("One more episode is probably fine.")
else:
    print("Time to go to bed.")