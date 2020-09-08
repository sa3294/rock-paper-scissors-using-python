'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.



import random


def wonnaplay():
  print("wonna play rock,paper,scissors? PRESS Y or y  for Yes and N or n  for no")
  ans = input()

  if(ans=="n" or ans=="N"):
    print("Okay ! alright . Bye")
  else:
    playgame()




def chooseoption():
  user_choice =input("choose rock,paper or scissors:  ")
  if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
  elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
  elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
  else:
        print("I don't understand, try again.")
        chooseoption()
  return user_choice



def computeroption():
  comp_choice = random.randint(1,3)
  if comp_choice == 1:
    comp_choice = "r"
  elif comp_choice == 2:
    comp_choice = "p"
  else:
    comp_choice = "s"  
  return comp_choice   



def againornot():
  print(" Do you wonna play again? PRESS Y or y  for Yes and N or n  for no")
  ans1 = input()
  if(ans1=="n" or ans1=="N"):
    print("Okay ! alright . Bye")
  else:
    playgame()




def playgame():
  comp_wins = 0
  player_wins = 0

  while True:
    user_choice = chooseoption()
    comp_choice = computeroption()


    if user_choice == "r":
      if comp_choice == "r":
        print("computer chose rock")
        print("  IT IS A TIE !")
        
        
      elif comp_choice == "p":
        print("computer chose paper")
        print(" SOORY YOU LOSE!")
        comp_wins += 1  
        
        
      else:
        print("computer chose was scissors")
        print(" WOHOO YOU WIN!")
        player_wins += 1
        
        


    if user_choice == "p":
      if comp_choice == "p":
        print("computer choice was paper")
        print(" IT IS A TIE !")
        
       
      elif comp_choice == "r":
        print("computer chose rock")
        print(" WOHOO YOU WIN!")
        player_wins += 1 
        
        

      else:
        print("computer chose scissors")
        print(" SORRY YOU LOSE!") 
        comp_wins += 1      
        
      


    if user_choice == "s":
      if comp_choice == "s":
        print("computer chose scissors")
        print(" IT IS A TIE !")
        
        
      elif comp_choice == "r":
        print("computer chose rock")
        print(" SORRY YOU LOSE!")
        comp_wins += 1 
        

      else:
        print("computer chose paper")
        print(" WOHOO YOU WIN!") 
        player_wins += 1        

    print("player score = " + str(player_wins))
    print("computer score = " + str(comp_wins))

    if(player_wins > comp_wins):
      print(" YAY YOU WON THE GAME")
    elif(player_wins == comp_wins):
      print(" ITS A TIE")
    else:
      print(" OOPS YOU LOST THE GAME")  
    againornot()  


wonnaplay()
