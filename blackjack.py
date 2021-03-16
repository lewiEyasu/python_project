import random
import art
import os

card_number=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

hit_me='y'
play_again='yes'
def dealing_card():
  x_number=random.choice(card_number)

  return x_number

def starting_card(card,number):
  for i in range(number):
    card.append(dealing_card())

  return card

def calculating_card(list_card):
  result=0
  list_string=['J','Q','K']

  for card in list_card:
    if card == "A":
        result+=11
    elif card in list_string :
      result+=10
    else:
      result+=int(card)
  for A in list_card:
    if A=="A":
      result=A_values(result)

  return result

def checking_result(user,computer,user_list):
  if user >21:
    print("Busts,you lost dummy")

  elif computer >21:
    print('Busts,you have won')   
  
  elif user == computer:
    print("push,it is a draw")
  elif user==21 and len(user_list)==2:
    print("Blackjack,you won")
  elif user > computer:
    print('you have won my friend')

  else:
    print('you lost dummy')  

def A_values(value):
 
  if value==21 or (value-11)<10:
    return value
  else:
    return value-10
# start the game 
def play_game():

  user_card=[]
  computer_card=[]
  user_result=0
  computer_result=0
  hit_me='y'

  print(art.logo)
  user_card=starting_card(user_card,2)
  computer_card=starting_card(computer_card,2)
  user_result=calculating_card(user_card)
  computer_result=calculating_card(computer_card)

  while hit_me=='y' and user_result<21:
    print('   your cards are:',user_card,f'current_score :{user_result}')
    print('   computer first card is :',computer_card[0])
    hit_me=input('type "y" to get another card or type "n" to pass \n').lower()
    if hit_me=="y":
      user_card=starting_card(user_card,1)
      user_result=calculating_card(user_card)
  print('   your final hand',user_card,'final score is :',user_result)    
  while computer_result<17:
    computer_card=starting_card(computer_card,1)
    computer_result=calculating_card(computer_card)
  print('   computer final hand',computer_card,'final score is :',computer_result)
  checking_result(user_result,computer_result,user_card)

while play_again=='yes':
  play_game()
  play_again=input("Do you want to Blackjack again? Type 'yes' or 'no'\n").lower()
  if play_again=='yes':
    os.system('clear')
  else:
    break  
