import os
import sys
import random

#Enemies
goblin = {}
goblin['Name'] = 'Goblin'
goblin['Health'] = 50.0
goblin['Agility'] = 40.0
goblin['Strength'] = 35.0
goblin['Level'] = 1

def Death():
    print("You have died!")
    print("GAME OVER")
    exit_game = input()
    sys.exit()
    
#Character Creaion

player={}
player['Name'] = input("Please enter your character's name. ")
player['Strength'] = (random.random() * 100)
player['Agility'] = ((10 * 100) + 70) / 2
player['Health'] = (random.random() * 100 + 100)

#End Character Creation
 

def Fight(enemy):
    print("All of a sudden a " + str(enemy['Name']) + " attacks you!")
    Enemy = enemy.copy()
    while Enemy['Health'] > 0:
        Attack = False
        A = input("Type A to attack the " + str(Enemy['Name']) + ". ")
        if A == "Attack" or "attack" or "A" or "a":
            Attack = True
            
        else:
            pass
        
        if Attack == True:
            Player_attack_lands = False
            Enemy_attack_lands = False
            if (Enemy['Agility'] - player['Agility'] + (random.random() - random.random()) * 100) <= 0:
                Player_attack_lands = True
                
            else:
                pass
            
            if Player_attack_lands == True:
                print("You strike the " + str(Enemy['Name']) + "!")
                Enemy['Health'] = round(Enemy['Health'] - player['Strength'])
                print("You've done " + str(round(player['Strength'])) +" damage! ")
                print("The " + str(Enemy['Name']) + " now has " + str(Enemy['Health']) + " left. ")
                if Enemy['Health'] <= 0:
                    pass
                
                else:
                    print("The " + str(Enemy['Name']) + " launches an attack at you! ")
                    if (Enemy['Agility'] - player['Agility'] + (random.random() - random.random()) * 100) <= 0:
                        Enemy_attack_lands = True
                        
                    else:
                        print("The " + str(Enemy['Name']) + " missed! ")
                        
                    if Enemy_attack_lands == True:
                        print("The " + str(Enemy['Name']) + " lands its attack! ")
                        player['Health'] = round(player['Health'] - Enemy['Strength'])
                        print("The " + str(Enemy['Name']) + " deals " + str(Enemy['Strength']) + " damage to you. ")
                        print("You have " + str(player['Health']) + " Health left. \na")
                        if player['Health'] <= 0:
                            Death()
                        else:
                            pass
                    else:
                        pass      
            else:
                print("You miss!")
                print("The " + str(Enemy['Name']) + " launches an attack at you! ")
                if (Enemy['Agility'] - player['Agility'] + (random.random() - random.random()) * 100) <= 0:
                    Enemy_attack_lands = True
                    
                else:
                    print("The " + str(Enemy['Name']) + " missed! ")
                    
                if Enemy_attack_lands == True:
                    print("The " + str(Enemy['Name']) + " lands its attack! ")
                    player['Health'] = round(player['Health'] - Enemy['Strength'])
                    print("The " + str(Enemy['Name']) + " deals " + str(Enemy['Strength']) + " damage to you. ")
                    print("You have " + str(player['Health']) + " Health left. ")
                    
                    if player['Health'] <= 0: 
                        Death()
                        
                    else:
                        pass
                    
    print("You've killed the " + str(enemy['Name']) + "!")    
while player['Health'] > 0:
    Fight(goblin)
    print("")   
    
