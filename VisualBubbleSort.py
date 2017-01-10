import time
import os
import random

class stick:

  def __init__(self,value):
    self.length = value
    self.visualRep = self.length * "-"

  def __str__(self):
    print self.visualRep

def BubbleSort(l):
    n=len(l)
    for i in range(n):
        for j in range(n-1-i):
            if l[j].length>l[j+1].length:
                l[j],l[j+1]=l[j+1],l[j]
        printList(l)
        time.sleep(0.5)
        os.system('cls')

        
def listGen():
    newList = []
    for i in range(0,50):
      lenghtOfStick = random.randint(1,100)
      newStick = stick(lenghtOfStick)
      newList.append(newStick)
    return newList

def printList(anyList):
  for i in anyList:
    print i.visualRep

aList = listGen()
BubbleSort(aList)
printList(aList)

print ""
ent=raw_input("Press any key to end")
