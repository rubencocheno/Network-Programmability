import json
import requests

#Welcome to Week 3 of Network Programmability

#Exercise 1
#Get the Weather of London for today.
#Use the API Key under .nonsecrets file
#Find Latitude and Longitude of London and execute a Get and dump all details
#Avoid any Loops
#Check requirements and endpoints in https://openweathermap.org/current

r = requests.get(" https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&&appid=9b4d948471f973ee68c4172f4cd3ef49"
                 )
#Exercise 2
#Get the Weather of Great Malvern for today
#Use the API Key under .nonsecrets file
#Find City ID and execute a Get and dump all details with temperature in Celsius
#Avoid any Loops
#Check requirements and endpoints in https://openweathermap.org/current

r = requests.get(" https://api.openweathermap.org/data/2.5/weather?id=2648063&&units=metric&&appid=9b4d948471f973ee68c4172f4cd3ef49"
                 )
#Exercise 3
#Get the Weather for Lisbon, Portugal
#Use the API Key under .nonsecrets file
#Find the temperature in Celsius
#Avoid any Loops
#Check requirements and endpoints in https://openweathermap.org/current

r = requests.get(" https://api.openweathermap.org/data/2.5/weather?id=2648063&&units=metric&&appid=9b4d948471f973ee68c4172f4cd3ef49"
                 )
#Exercise 4
#Compare all previous cities and return which one is the coldest and warmest by City (Temperature)
#Use the API Key under .nonsecrets file

#Check requirements and endpoints in https://openweathermap.org/current

r = requests.get(" https://api.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&&appid=9b4d948471f973ee68c4172f4cd3ef49")


