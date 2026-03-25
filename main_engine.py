import random
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

RED   = "\033[1;31m" # Hearts & Diamonds
WHITE = "\033[1;37m" # Spades & Clubs
GOLD  = "\033[1;33m" # For Hand Bonuses
RESET = "\033[0m"

def create_deck():
  suits= {
      'Hearts': '♥',
      'Diamonds': '♦',
      'Clubs': '♣',
      'Spades': '♠'
  }
  ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']

  deck=[[rank, symbol, suit] for suit,symbol in suits.items() for rank in ranks]
  random.shuffle(deck)
  return deck

def get_ascii_hand(hand):
    lines=["" for _ in range(5)]

    for card in hand:

      rank,symbol=card[0],card[1]

      color=RED if symbol in ['♥','♦'] else WHITE

      r=rank.ljust(2)
      lines[0] += f" {WHITE}┌─────────┐{RESET} "
      lines[1] += f" {WHITE}│{color}{r}       {WHITE}│{RESET} "
      lines[2] += f" {WHITE}│    {color}{symbol}    {WHITE}│{RESET} "
      lines[3] += f" {WHITE}│       {color}{r.rjust(2)}{WHITE}│{RESET} "
      lines[4] += f" {WHITE}└─────────┘{RESET} "
    return "\n".join(lines)

def get_score(hand):
  values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14}

  ranks = [card[0] for card in hand]

  symbols = [card[1] for card in hand]

  num_vals = sorted([values[r] for r in ranks])
    
  counts = [ranks.count(r) for r in set(ranks)]

  is_flush = len(set(symbols)) == 1

  is_straight = all(num_vals[i] == num_vals[i-1] + 1 for i in range(1, 5))
    
  bonus = 0

  hand_name = "High Card"

  if is_straight and is_flush:
    bonus, hand_name = 500, "STRAIGHT FLUSH"
  elif 4 in counts:
    bonus, hand_name = 200, "FOUR OF A KIND"
  elif 3 in counts and 2 in counts:
    bonus, hand_name = 120, "FULL HOUSE"
  elif is_flush:
    bonus, hand_name = 85, "FLUSH"
  elif is_straight:
    bonus, hand_name = 70, "STRAIGHT"
  elif 3 in counts:
    bonus, hand_name = 50, "THREE OF A KIND"
  elif counts.count(2) == 2:
    bonus, hand_name = 30, "TWO PAIR"
  elif 2 in counts:
        bonus, hand_name = 15, "PAIR"

  if bonus > 0:
      print(f"{GOLD}🔥 {hand_name} BONUS (+{bonus})!{RESET}")
    
  base_sum = sum(values[r] for r in ranks)
  return base_sum + bonus
    
def display_card(card):
  return f"[ {card[0]} {card[1]} ]"
