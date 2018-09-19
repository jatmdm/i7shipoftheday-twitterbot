# import settings
import tweepy
from shipgenerator import *


newship = GenerateRandomShip()
shipstring = ""

for index in newship:
	shipstring += index + " "

print("The I7 Ship of the Day is " + shipstring)