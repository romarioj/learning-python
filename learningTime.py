import time
def calcProd():
    product = 1
    # Calculate the product of numbers 1-10 or the equivalent of 10! (10 factorial)
    for i in range(1,11):
        product = product * i
    return product

startTime = time.time()
# The time.time() function returns the number of seconds since January 1, 1970
# aka Coordinated Universal Time (UTC)
prod = print('The product is: %s' % (calcProd()))
prod1 = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod1))))
print('Took %s seconds to calculate.' % round((endTime - startTime),6)) # round to 6 digits

for i in range(0):
    print('tick')
    time.sleep(1) # will pause program for 1 second or however many you specify
    print('tock')
    time.sleep(1)

import datetime
print(datetime.datetime.now()) # returns date and time right now in your zone
datetime.datetime.fromtimestamp(5000000)

