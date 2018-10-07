'''
This script uses the requests module to download data weather from the web.
This script will:
    1. Read the requested location from the text
    2. Download JSON data from openweathermap.org
    3. Convert the JSON string into Python data
    4. Prints the weather for today

    a. Call requests.get() to download weather data
    b. Call json.loads() to convert the JSON data to a Python data structure
    c. Print the weather forecast
'''
run = True
while run:
    import json, requests, re
    
    # Step 1: Download JSON data from OpenWeatherMap.org API
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

    def city(): # This while loops makes sure the input is alphabet letters only
        while True:
            location = input('Enter a city: ')
            if re.match(r'(^\w+(\s?)\w+$)', location): 
            # \w matches words and + means it matches 0 or more times
            # ^ and $ mark the begin and end of the string
            # \s matches space and ? means it matches 0 or 1 time
                return location
            else:
                print("Please only use letters, try again")
                
    r = url + city()
    response = requests.get(r)
    response.raise_for_status() # Check for erros
    
    # Step 2: Load JSON data into a Python variable
    
    # print(response.text) # This will display the JSON string text
    weatherData = json.loads(response.text) #response.text is where the weather text is downloaded
    # This text is a long dictionary 
    # We can grab specific keys from this dictionary
    # Example keys are 'weather' 'sys'
    # To better understand where these are, visit the JSON code or type it into a nice JSON editor to visualize it i.e. https://jsoneditoronline.org/
    # Step 3: Display data nicely
    
    import datetime
    d = datetime.datetime.fromtimestamp(weatherData['sys']['sunrise']) # Converting a timestamp to mm/dd/yy format
    print('\nToday is:', d.strftime('%A, %B %d')) # %A, %b etc are specified in the .strftime module https://docs.python.org/2/library/datetime.html
    print('Time data was calculated:', datetime.datetime.fromtimestamp(weatherData['dt']).strftime('%I:%M %p'))
    w = weatherData['weather']
    print('Current location is: ' + weatherData['name'].title() + ',', weatherData['sys']['country'])
    print('The weather mood is: ' + w[0]['main'], '-', w[0]['description'].capitalize())
    print('The sunrise is at:', d.strftime('%I:%M %p'))
    print('The sunset is at:', datetime.datetime.fromtimestamp(weatherData['sys']['sunset']).strftime('%I:%M %p'))
    print('The humidity is: ' + str(weatherData['main']['humidity']) + '%')
    print('The temp is:', str(round((((weatherData['main']['temp'])-273.15) * 9/5 + 32), 1)), 'F')
    print('The min temp is:', str(round((((weatherData['main']['temp_min'])-273.15) * 9/5 + 32), 1)), 'F')
    print('The max temp is:', str(round((((weatherData['main']['temp_max'])-273.15) * 9/5 + 32), 1)), 'F')
    quit = input('Restart? Press Y/N: ').lower()
    if quit == 'n':
        run = False
