import random

def main():

  muerto = False
  done = False
  miles_traveled = 0
  thirst = 0
  camel_tiredness = 0
  native_miles = -20
  drinks = 3

  print("Welcome to Camel!")
  print("You have stolen a camel to make your way across the great Mobi desert.")
  print("The natives want their camel back and are chasing you down! Survive your")
  print("desert trek and out run the natives.")

  while not done:
      oasis = random.randint(1,20)
      print(" A. Drink from your canteen.")
      print(" B. Ahead moderate speed.")
      print(" C. Ahead full speed.")
      print(" D. Stop for the night.")
      print(" E. Status check.")
      print(" Q. Quit.")
      choice = str(input("what is your choice? "))

      if choice.upper() == "Q":
        print("You exit the game")
        done = True
      elif choice.upper() == "E":
          print("Miles traveled:", miles_traveled)
          print("Drinks left:", drinks)
          print("Native are", -native_miles, "miles away")
      elif choice.upper() == "D":
          camel_tiredness = 0
          print("The camel is happy")
          native_move = random.randint(7, 14)
          native_miles += native_move
      elif choice.upper() == "C":
          forward = random.randint(10, 20)
          miles_traveled += forward
          print("You traveled", forward,"miles")
          thirst += 1
          tiredness = random.randint(1, 3)
          camel_tiredness += tiredness
          native_move = random.randint(7, 14)
          native_miles += native_move
          native_miles -= forward
      elif choice.upper() == "B":
          forward = random.randint(5, 12)
          miles_traveled += forward
          print("You traveled", forward,"miles")
          thirst += 1
          camel_tiredness += 1
          native_move = random.randint(7, 14)
          native_miles += native_move
          native_miles -= forward
      elif choice.upper() == "A":
          if drinks>0:
              thirst = 0
              drinks -= 1
          else:
              print("You have no drinks left")

      if thirst>4 and thirst<=6:
          print("You are thirst")
      elif thirst>6:
          print("You died of thirst!")
          done = True
          muerto = True

      if camel_tiredness>5 and camel_tiredness<=8:
         print("Your camel is getting tired.")
      elif camel_tiredness>8:
          print("Your camel is dead.")
      if native_miles == 0:
          print("The natives have caught up!")
          done = True
          muerto = True
      elif native_miles<15 and native_miles>0:
          print("The natives are getting close!")
      if miles_traveled>200 and muerto == False:
          print("You escape!")
          done = True
      if oasis == 1 and (choice == "B" or choice == "C"):
          drinks = 3
          thirst = 0
          camel_tiredness = 0








main()
