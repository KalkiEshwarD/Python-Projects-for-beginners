# Here I created an alam for the people who use the pomodoro technique. If you don't know what it is, look it up. It's sure to help you.
# I created it to follow the 20-20-20 rule so that it helps me maintain healthy eyesight. Look it up if you don't know. Try to follow it too. 
# Well, here we would be using two built in modules, os and time.

# Importing modules
import os
import time

sessions = int(input("How many sessions would you like to do?\n"))                          # Here I ask how many sessions the user would like to do and if he would like to go with the traditional timer.
print("Would you like to proceed with 25 minute sessions with 5 min break?")
x = input("Y\\N\n")
y = ['y', 'Y']                                                                              # refer line 24

def timer(st, bt, s):                                                                       # Here i create a function called timer that plays a sound (alarm) based on the amount of time the user sets it to. It takes in 3 arguments, session time, break time and number of sessions.
    time.sleep(st * 60)                                                                     # The sleep function basically puts python to 'sleep' for a certain amount of seconds. Since we are using minutes for each session, I multiply it by 60 to make it last for the specified duration.
    os.startfile('file.mp3')                                                                # Here you could simply specify if the mp3 file name if it's in the same directory, else just type in the file path along with the file name.
    time.sleep(bt * 60)                               
    os.startfile('file.mp3')
    global sessions                                                                         # Again, variables used in functions have to be first declared global variables if we want them to work.
    sessions -= 1
    while sessions > 0:                                                                     # Makes the program run over again until all the sessions are done.
        timer(session_time, break_time)

if x in y:                                                                                  # For some reason if x == 'y' or 'Y' wasn't working on my computer it was always running the if command regardless of imput, was looking up online. Didn't find the reason. Try to find out if you don't know too.                                                                                
    print('Done...')
    timer(25, 5, sessions)

else:                                                                                       # It makes the user specify the session and break time.
    print('Ok...')
    session_time = float(input("For how many minutes would you like to have the session? \n"))
    break_time = float(input("For how many minutes would you like to take a break? \n"))
    timer(session_time, break_time, sessions)
