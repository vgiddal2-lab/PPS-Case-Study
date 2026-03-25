
import os
import time
import random
import wallet
import main_engine
import winsound


def clear():
  os.system('cls' if os.name== 'nt' else 'clear')

RED=main_engine.RED
GOLD=main_engine.GOLD
RESET=main_engine.RESET
WHITE=main_engine.WHITE


while True:
  clear()
  print(f"{GOLD}---WELCOME TO HIGH CHOICE POKER---{RESET}")
  user_name=input("\nEnter your name to register.").strip()
  print(f"Welcome, {user_name}. The Comp is ready for you.")

  exit_all= False

  while True:
    chips=wallet.load_wallet()


    if chips<=0:
      print(f"\n{RED}You have no chips remaining.{RESET}")
      print("Resetting wallet to 1000 Chips.")
      wallet.save_wallet(1000)
      break

    print(f"\n" + "="*30)
    print(f"PLAYER: {user_name.upper()}Current Balance is : {chips} chips")
    print("="*30)

    print(f"\nGathering cards. . .")
    time.sleep(0.5)
    print(f"\nShuffling deck. . .")
    time.sleep(1)

    deck=main_engine.create_deck()
    player_hand=deck[0:5]
    comp_hand=deck[5:10]

    for i in range(1,6):
      clear()
      print(f"PLAYER : {user_name.upper()} | Balance : {chips} chips")
      print("="*30)

      print("\nYour Hand :")
      print(main_engine.get_ascii_hand(player_hand[:i]))

      winsound.Beep(800,80)
      time.sleep(1)

    try:
      bet=int(input(f"Place your bet(1-{chips}): "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if bet>chips:
      print(f"{RED}You don't have enough chips!{RESET}")
      continue


    choice=input("Will your score be (G)reater or (L)esser than comp's?").strip().upper()


    print("\nComp is calculating possibilities. . . .")
    time.sleep(1.2)

    for i in range(1,6):
      clear()
      print("Your Hand : ")
      print(main_engine.get_ascii_hand(player_hand))
      print(f"Comp's Hand. . .")

      print(main_engine.get_ascii_hand(comp_hand[:i]))
      winsound.Beep(600,50)
      time.sleep(1)

    p_score=main_engine.get_score(player_hand)
    c_score=main_engine.get_score(comp_hand)

    print(f"\nYour Score : {p_score} | Comp's Score : {c_score}")

    won=False
    if choice=="G" and p_score>c_score:
      won=True
    elif choice=="L" and p_score<c_score:
      won=True

    if won:
      print(f"{GOLD}You Win! {bet} chips have been added to your wallet!{RESET}")
      winsound.Beep(1000,150)
      winsound.Beep(1200,200)
      wallet.save_wallet(chips+bet)
      wallet.log_score(user_name, bet)

    else:
      print(f"{RED}Defeat! You Lost {bet} chips!{RESET}")
      winsound.Beep(300,400)
      wallet.save_wallet(chips-bet)
      wallet.log_score(user_name, -bet)

    play_again=input("Would you like to play again? (y/n)").strip().lower()

    if play_again=="y":
      who=input("Same Player(1) or Different Player(2)?")
      if who=="2":
        break
      else:
        clear()
        continue
    else:
      print(f"\nThe arena is closing. Your progress has been saved.")
      print(f"See you later, {user_name}")
      exit_all=True
      break
  if exit_all:
    break
