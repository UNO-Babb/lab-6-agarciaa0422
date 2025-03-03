#DiceRoll.py
#Name:Arturo
#Date:3/2/2025
#Assignment:Dice Roll
import random
start = 1

end = 6
def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  numRolls = 10000
  for count in range(numRolls):
    dice1 = random.randint(start,end)
    dice2 = random.randint(start,end)
    #find the sum total of the two dice
    sum() = dice1 + dice2

    rolls[sum() - 2] = rolls[sum()- 2]  + 1
    #print statictics for dice rolls
  num = 2
  for r in rolls:
    percent = round(r/ numRolls * 100, 1)
    print(num, ":", r)
    num = num + 1
if __name__ == '__main__':
  main()
