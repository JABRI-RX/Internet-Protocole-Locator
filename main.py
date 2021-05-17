#import some packages
from requests import post
from os import system
info = []
#clear the terminal
system('clear')
#setting our variables
url = "http://ip-api.com/line/"
#http://81.192.44.21/
print('_________________________________________________')
print('|     ___     ___________                        |')
print('|    |   |   |           |   |                   |')
print('|    |   |   |    ____    |  |                   |')
print('|    |   |   |   |    |    | |                   |')
print('|    |   |   |   |____|   |  |                   |')
print('|    |   |   |___________|   |                   |')
print('|    |   |   |               |                   |')
print('|    |   |   |               |                   |')
print('|    |   |   |               |                   |')
print('|    |   |   |               |                   |')
print('|    |___|   |               |_______________    |')
print('|------------------------------------------------|')
print('|           Internet Protocole Locator           |')
print('|------------------------------------------------|')
ip = input("|Enter the ip:").strip()
try :
	if ip[0:3]!="htt":
		get = post(url+ip)
		sad = get.text
		info.append(sad.split())
		print('|_________________________________________________')
		print('|Country\t\tRegion')
		print('|_________________________________________________')
		print(f"|{info[0][1]}\t\t\t{info[0][4]}")
		print('|_________________________________________________')
	else:
		print("try removing https/http")
except:
	print("check the format again")
