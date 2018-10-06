#learningJSON
'''
Websites provide their API's through JSON formatted content.
Fb, Twitter, Yahoo, etc... offer APIs in JSON format.
APIs are useful because:
    1. You can scrape raw data from websites a lot easier than parsing HTML with BeatutifulSoup
    2. Automatically download new post from one social network website and post them to another social website
    3. Pull data from IMDb, Wikipedia or whatever and put it into a single text file
    4. Example APIs https://automatetheboringstuff.com/list-of-json-apis.html
'''

# To translate a JSON string into Python, pass it intio the: json.loads() function
# JSON strings always use double quotes

jsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(jsonData)
print(jsonDataAsPythonValue)
# Python dictionaries are not ordered, so the key-value pairs may appear in a different order when you print the variable

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue) #json.dumps converts from python to JSON
print(stringOfJsonData)
# The value can only be one of the following basic Python data types:
# dictionary, list, integer, float, string, Boolean, or None.
