import os
import xml.etree.ElementTree as ET
import sys

def processAttribute(x, thing):
    file = open(path + "/" + x)
    tree = ET.parse(file)
    root = tree.getroot()[0]
    return(int(root.get(thing)))

def checkBest(old, new):
    if(new > old):
        return new
    else:
        return old

#f = filename
#s = second dictionary key (stat name)
#a = attribute name
def processStat(f, s, a):
    global stats
    temp = processAttribute(f, a)
    if(stats['Most'][s] < temp):
        stats['Most'][s] = temp
    stats['Total'][s] = stats['Total'][s] + temp

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

stats = {
        'Most': {'Kills': 0, 'Deaths': 0, 'Gold': 0, 'Kicks': 0, 'Shots': 0},
        'Total': {'Kills': 0, 'Deaths': 0, 'Gold': 0, 'Kicks': 0, 'Shots': 0}
        }

for d, n, names in os.walk(path):
    
    #Make sure to start on a stats xml file
    if("stats" not in names[0]):
        i = 1

    while i < len(names):

        processStat(names[i], 'Kills', 'enemies_killed') 
        processStat(names[i], 'Deaths', 'dead')
        processStat(names[i], 'Gold', 'gold_all')
        processStat(names[i], 'Kicks', 'kicks')
        processStat(names[i], 'Shots', 'projectiles_shot')
        
        i = i + 2

for i in stats['Total']:
    print(i + ' ' + str(stats['Total'][i]))

pathFile.close()
