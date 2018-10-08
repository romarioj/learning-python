# stopwatch.py - Project Stopwatch
'''
This program will:
    1. Track the time between presses of the ENTRY key, with each key press starting a new "lap" on the timer.
    2. Print the lap number, total time and lap time.
'''

import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.')
print('Press Ctrl-C to quit.')

input() # press Enter to begin
print('Started.')

startTime = time.time() # first lap start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone.')
            
