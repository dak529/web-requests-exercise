# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")

import requests
import json

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
response_data = json.loads(response.text)

print(response_data['name'])
print(type(response_data))


request_url2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response2 = requests.get(request_url2)
response_data2 = json.loads(response2.text)
for r in response_data2:
    print("Name: ",r["name"] + "   " + "ID: ", r["id"])

request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request_url3)
response_data3 = json.loads(response3.text)

grades = []
students = response_data3["students"]
for r in students:
    grades.append(r["finalGrade"])

print("MAX: ", max(grades))
print("MIN: ", min(grades))
avg = sum(grades)/len(grades)
print("AVG: ", round(avg, 2))