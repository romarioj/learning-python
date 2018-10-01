# This script will play the game 2048 https://gabrielecirulli.github.io/2048/
# Turns out a high score can be achieved by playing up, right, down and left.
# Write a script to get a high score by repeating this pattern.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

body = browser.find_element_by_tag_name('body') # activate the page

# Create dictionary to call keys Up, Right, Down, Left as 0,1,2,3
click = {0: Keys.UP, 1:Keys.RIGHT, 2:Keys.DOWN, 3:Keys.LEFT}

browser.find_element_by_class_name('grid-container').click() # clicks on game

# Create a while loop to click buttons until game is over
count = 0
while True: # means loop forever. 
    count = count + 1
    body.send_keys(click(count))

# by clicking 'try again' the python code repeats 
browser.find_element_by_class_name('retry-button').click()

#Future To-Do's in this project.
'''
1. Have the script "try again" until it records a score > 5000
2. Count how many tries it took to score > 5000
3. Have to script play 100 games and export it as excel or csv
    a. or maybe store it in a list on the python code
    b. find average score from 100 games using python
'''
