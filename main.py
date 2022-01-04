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

def generate_kpop(user_input):
  kpop = [
    "Ult boy group?",
    "Ult girl group?",
    "That's so cool!",
    "SM, YG, or JYPE",
    "SOTY?",
    "Best generation of kpop?",
    "Favorite solo artisti?",
    "No way, same!",
    "100% agree with you!",
  ]
  return random.choice(kpop)

def init_chat():
  quit_character = 'q'

  user_input = input("Would you like to discuss the MCU or Kpop today?\n")

  if(user_input == "MCU"):
    while user_input != quit_character:
      #Ask the user for more input, then use that in your response
      user_input = input(generate_marvel(user_input) + "\n")
  elif(user_input == "Kpop"):
    while user_input != quit_character:
      #Ask the user for more input, then use that in your response
      user_input = input(generate_kpop(user_input) + "\n")


if __name__ == "__main__":
  init_chat()