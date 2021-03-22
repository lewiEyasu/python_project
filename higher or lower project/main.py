import game_data
import random
import art
import os

campare_A={}
campare_B={}
final_score=0
input_answer=True
#assign a random value from game_data
def assigning():

  random_index=random.randint(0,len(game_data.data))

  return game_data.data[random_index]

def checking(campare_A,campare_B,answer):

  if campare_A > campare_B:
    corrct_answer='A'
  elif campare_A < campare_B:
    corrct_answer='B'

  if answer==corrct_answer:
    return True

  else:
    return False  

def checking_repeation(B):
  B=assigning()
  while campare_A==B:
    B=assigning()

  return B


def start_game(A,B):

  print(art.logo)

  if final_score!=0:
    print(f'you are right! current score: {final_score}')
    
  print(f"compare A:{A['name']},{A['description']},{A['country']}")
  print(art.vs)
  print(f"against B:{B['name']},{B['description']},{B['country']}")

def game_over():
  print(art.logo)
  print(f"sorry that is a wrong. final score {final_score}")


while input_answer:

  if final_score==0:
    campare_A=assigning()

  else:
    campare_A=campare_B
  
  campare_B=checking_repeation(campare_B)

  start_game(campare_A,campare_B)
  answer=input('who has more followers? Type "A" or "B": ').upper()
  input_answer=checking(campare_A[ 'follower_count'],campare_B[ 'follower_count'],answer)
  if input_answer:
    final_score+=1
    os.system('clear')

  else:
    os.system('clear')
    game_over()
    