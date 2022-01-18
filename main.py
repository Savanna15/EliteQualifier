import random

#chat program
#Responds randomly with one of the preprogrammed responses

def generate_marvel(user_input):
  marvel = [
    "What's your favorite mcu team?",
    "Omg me too!!",
    "Best villain?",
    "Which infinity stone do you want?",
    "That's amazing!",
    "Team Cap or Team Iron Man?",
    "Favorite mcu show on disney+?",
    "Favorite mcu show on Netflix?",
  ]
  return random.choice(marvel)

  #team iron man
  #team cap

def generate_kpop(user_input):
  kpop = [
    "Ult boy group?",
    "Ult girl group?",
    "That's so cool!",
    "SM, YG, or JYPE",
    "SOTY?",
    "Gen 2, 3, or 4?",
    "Favorite solo artisti?",
    "No way, same!",
    "100% agree with you!",
  ]
  return random.choice(kpop)

  #gen 2
  #gen 3
  #gen 4
  #SM
  #JYPE
  #YG

def init_chat():
  quit_character = 'q'

  user_input = input("Would you like to discuss the MCU or Kpop today?\n")

  if(user_input == "MCU"):
    while user_input != quit_character:
      #Ask the user for more input, then use that in your response
      user_input = input(generate_marvel(user_input) + "\n")
      #if user inputs iron man start using list of questions relating to team iron man
      #if cap list realting to team cap
  elif(user_input == "Kpop"):
    while user_input != quit_character:
      #Ask the user for more input, then use that in your response
      user_input = input(generate_kpop(user_input) + "\n")
      #if gen ask from gen's list
      #if company ask from company's list


if __name__ == "__main__":
  init_chat()