# ROCK PAPER SCIRROS GAME ---
def main():
  # NAME INPUT ---
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")
  # ANSWER INPUT ---
  p1a = input(f"{player1}, rock, paper or scissors? ").lower()
  p2a = input(f"{player2}, rock, paper or scissors? ").lower()

  # COMPARE ANSWERS ---
  if p1a == p2a:
    print("It's a Tie!")
    runagain()
  elif p1a == 'rock':
    if p2a == 'scissors':
      print(f"{player1} wins!")
      runagain()
    else:
      print(f"{player2} wins!")
      runagain()
  elif p1a == 'paper':
    if p2a == 'rock':
      print(f"{player1} wins!")
      runagain()
    else:
      print(f"{player2} wins!")
      runagain()
  elif p1a == 'scissors':
    if p2a == 'paper':
      print(f"{player1} wins!")
      runagain()
    else:
      print(f"{player2} wins!")
      runagain()

# RUN AGAIN?
  def runagain():
      run = input("Run again? (Y/N) ").upper()
      if run == "Y":
        main()
        runagain()
      if run == "N":
        print("Thank you for playing!")
  runagain()
main()
