# timer.py
#
# Function for the countdown timer.

import time

def countdown(minutes):
    assert(isinstance(minutes, int))
    assert(minutes > 0)

    # Initializing values being displayed for the timer
    minutes -= 1
    seconds_left = 59

    while (minutes > -1):
        print("Time left: {:02}:{:02}".format(minutes, seconds_left), end = "\r")
        time.sleep(1)
        seconds_left -= 1

        # Adjusts the values every minute
        if (seconds_left == -1):
            minutes -= 1
            seconds_left = 59
