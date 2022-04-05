import os
import xml.etree.ElementTree as ET
import sys

def processThing(x, thing):
    file = open(path + "/" + x)
    tree = ET.parse(file)
    root = tree.getroot()[0]
    return(int(root.get(thing)))

def checkBest(old, new):
    if(new > old):
        return new
    else:
        return old

#Peep stored path file

pathFile = open('path.txt', 'r+')
path = str(pathFile.read())

if len(path) == 0 or input("Enter new username? (y/n)") == 'y':

    if(sys.platform.startswith('linux')):    
        path = "/mnt/c/Users/" + input("Enter your windows username:") + "/AppData/LocalLow/Nolla_Games_Noita/save00/stats/sessions"
    else: 
        path = "/c/Users/" + input("Enter your windows username:") + "/AppData/LocalLow/Nolla_Games_Noita/save00/stats/sessions"
    pathFile.write(path)

#Stats to be ooga'd

kills = 0
deaths = 0
gold = 0
kicks = 0
shots = 0
i = 0

temp = 0

hK = 0
hG = 0
hKi = 0
hS = 0


for d, n, names in os.walk(path):
    
    #Make sure to start on a stats xml file
    if("stats" not in names[0]):
        i = 1

    while i < len(names):
        
        temp = processThing(names[i], 'enemies_killed')
        kills = kills + temp
        hK = checkBest(hK, temp)
        
        temp = processThing(names[i], 'dead')
        deaths = deaths + temp

        temp = processThing(names[i], 'gold_all')
        gold = gold + temp
        hG = checkBest(hG, temp)

        temp = processThing(names[i], 'kicks')
        kicks = kicks + temp
        hKi = checkBest(hKi , temp)

        temp = processThing(names[i], 'projectiles_shot')
        shots = shots + temp
        hS = checkBest(hS, temp)

        i = i + 2

print("Kills: " + str(kills))
print("Deaths: " + str(deaths))
print("Gold: " + str(gold))
print("Kicks: " + str(kicks))
print("Shots: " + str(shots))

print("Most Kills: " + str(hK))
print("Most Gold: " + str(hG))
print("Most Kicks: " + str(hKi))
print("Most Shots: " + str(hS))

pathFile.close()
