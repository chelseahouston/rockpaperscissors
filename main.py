# ROCK PAPER SCISSORS GAME ---
def main():
  # NAME ---
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # ANSWER INPUT ---
 
  p1a = input(f"{player1}, rock, paper or scissors? ").lower()
  while p1a not in ('rock', 'paper', 'scissors'):
    print("Incorrect value.")
    break
  
  p2a = input(f"{player2}, rock, paper or scissors? ").lower()
  if p2a not in ('rock', 'paper', 'scissors'):
    print("Incorrect value.")
      
 # COMPARE ANSWERS ---
  if p1a == p2a:
    print("It's a Tie!")
  elif p1a == 'rock':
    if p2a == 'scissors':
      print(f"{player1} wins!")
    else:
      print(f"{player2} wins!")
  elif p1a == 'paper':
    if p2a == 'rock':
      print(f"{player1} wins!")
    else:
      print(f"{player2} wins!")
  elif p1a == 'scissors':
    if p2a == 'paper':
      print(f"{player1} wins!")
    else:
      print(f"{player2} wins!")

# RUN AGAIN? ---
  def run():
    while True:
      playagain = input("Play again? (Y/N): ").upper()
      if playagain not in ('Y', 'N'):
        print("Invalid Input.")
        break
        run()
      if playagain == 'Y':
        main()
      if playagain == 'N':
        print("Thank you for playing.")
        break
  run()

main()