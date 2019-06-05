import os
import sys
import random
import time
    

print("HeacockBros RPG\n")    
    
start = True
while (start):
    print ("(A) Start Game\n"
              "(B) Quit")
    choice = input('')
    if choice == ('A'):
        start = False
        break
    elif choice == ('B'):
        sys.exit()
    elif(): 
        break
        
print (f"""        You awake in a rocky terrane. Your back is stiff and you feel a numbness in your left elbow.\n 
        Then you look over to see that you haveno left arm. Freaked out you stumble to your feet and\n
        lean on a boulder to your left. You then see a broken sword laying on the ground. It looks\n 
        almost as it where perfectly broken in half with the handle and half the blade in contact.\n 
        Regaining your thoughts and the events that happened before.\n\n""")

# Character Build

name = input('my name is...')
Class = input('\nI was a (knight or mage)...')
Race = input('\nI grew up as a young (human or orc)...')
print ('in my home village')
Past = input('\n"right your past":')



print ('So you set forth on your quest')
    
    
#Characters

def human(object):
    
    self.maxHP = 100
    self.mana = 200
    self.attack = 100
    
def orc(object):
    
    self.maxHP = 150
    self.mana = 100
    self.attack = 150 

#Variables

#ITEMS
    
#Weapons

sword = 10

#Game Mechanics  

def damage(lvl, weapon):
    
        lvl * 5 + weapon
    
def createKnight(self, name, lvl):

        self.name = name

        self.clss = "warrior"

        self.maxHP = 100 * lvl - (lvl * 10)

        self.life = self.maxHP - 30*lvl

        self.lucky = lvl*4

        self.dex = 6 + lvl

        self.armor = 10 + lvl

def createMage(self,name, lvl):
        
        self.name = name
        
        self.clss = "mage"
        
        self.maxHP = 100 * lvl -(lvl * 10)
        
        self.life = self.maxHP - 25*lvl
        
        self.lucky = lvl*5
        
        self.dex = 6 + lvl
        
        self.armor = 5 + lvl
        
#Enemies

goblin = {}
goblin['Name'] = 'Goblin'
goblin['Health'] = 50.0
goblin['Agility'] = 40.0
goblin['Strength'] = 35.0
goblin['Level'] = 1
