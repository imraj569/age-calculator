import time
import os
import datetime

os.system('clear')
print ('''
▄▀█ █▀▀ █▀▀
█▀█ █▄█ ██▄

█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄

v - 0.1
author - raj
---------------------------------------
''')

time.sleep(1)
dob = int(input("Enter your birthday year e.g 2001 :"))
age = datetime.datetime.now().year - dob
per = age - 1
os.system('clear')
print ('''
╭━━╮╱╱╱╱╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮┣━┳━╮┃╭╋━╮╭╮╭━┳┳┳╮╭━╮┃╰┳━┳┳╮
┃┣┫┃╋┃┻┫┃╰┫╋╰┫╰┫━┫┃┃╰┫╋╰┫╭┫╋┃╭╯
╰╯╰╋╮┣━╯╰━┻━━┻━┻━┻━┻━┻━━┻━┻━┻╯
╱╱╱╰━╯''')
time.sleep(1)
print ('you are now' , per, 'years' )
time.sleep(2)
print ("thanks for using \U0001F642 ")
time.sleep(1)

