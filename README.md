# PPS-Case-Study

For my Programming for problem solving assignment, Instead of trying to make a typical case study, I decided to make this version of poker, specifically my take on an already existing version of poker called "Choice Poker".

# How to start

1. Add all the files into a folder and import them into vsc
2. using the terminal, call the main_engine.py , wallet.py and game.py files into the terminal in the respective order.
3. python main_engine.py --> --> python wallet.py --> python game.py
4. After game.py is called, the game starts.


How to play:
1. The game starts off by asking for your name.
2. Then, the game shuffles and deals you 5 cards.
3. Based on the rank of the card, the sum of the cards is totalled, but unlike normal poker, since you are betting, you are able to choose whether the winner needs to have the sum highest or sum lowest to win.
4. Based on your cards, you have to pick (G)reater or (L)esser as the winner.
5. Winner gets decided based on the above condition.
6. All results are exported to a scores.csv file where they are saved.
7. In case you lose all your chips, the computer gives you 1000 chips to continue playing.
