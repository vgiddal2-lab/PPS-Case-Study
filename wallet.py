import csv
from datetime import datetime
import os

def load_wallet():
  try:
    with open("wallet.txt","r") as f:
      content=f.read().strip()
      return int(content) if content else 1000
  except (FileNotFoundError, ValueError):
    return 1000

def save_wallet(amount):
  with open("wallet.txt","w") as f:
    f.write(str(amount))

def log_score(name,change):
  path=(r"C:\Users\elixi\OneDrive\Desktop\PPS\scores.csv")
  with open(path,"a",newline="") as f:
    writer=csv.writer(f)
    now=datetime.now().strftime("%Y-%m-%d %H:%M")
    writer.writerow([now, name, change])