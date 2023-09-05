import json
import requests

#Welcome to Week 3 of Network Programmability

#This is a list of exercises to get some exposure to RESTAPI using Python.

#Exercise 1
#Get the Weather of London for today
#Use the API Key under .nonsecrets file
#Find Latitude and Longitude of London and execute a Get and dump JSON all details as output
#Avoid any Loops
#Check requirements and endpoints in https://openweathermap.org/current


#lat 51.5
#lon 0.1
#API_KEY = 9b4d948471f973ee68c4172f4cd3ef49

#https: // api.openweathermap.org/data/2.5/weather?lat = 44.34 & lon = 10.99 & appid = {API key}

r = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?lat=51.5&lon=0.1&appid=9b4d948471f973ee68c4172f4cd3ef49")

#print(r.json())
  
#Exercise 2
#Get the Weather of Great Malvern for today
#Use the API Key under .nonsecrets file
#Find City ID and execute a Get and dump JSON all details as output with temperature in Celsius
#Avoid any Loops
#Check requirements and endpoints in https://openweathermap.org/current

#API_KEY = 9b4d948471f973ee68c4172f4cd3ef49
#CityID=2648063
#units=metric

#https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}


r = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?id=2648063&appid=9b4d948471f973ee68c4172f4cd3ef49")

print(r.json())

#Exercise 3
#Get the Weather for Lisbon, Portugal
#Use the API Key under .nonsecrets file
#Find the temperature in Celsius
#Avoid any Loops
#Check requirements and endpoints in https://openweathermap.org/current

#Exercise 4
#Compare all previous cities and return which one is the coldest and warmest by City (Temperature)
#Use the API Key under .nonsecrets file

#Check requirements and endpoints in https://openweathermap.org/current

