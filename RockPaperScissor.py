import random,sys
wins = 0
losses = 0
ties = 0
while True:
    print("ROCK, PAPER, SCISSORS")
    print(("%s Wins, %s Losses, %s Ties"%(wins,losses,ties)))
    while True:
        print("Enter your move : (r)ock, (p)aper, (s)cissors or (q)quit")
        mymove = input().lower()
        if mymove=="r" or mymove=="p" or mymove=="s":
            break
        elif mymove == "q":
            sys.exit()
    if mymove == "r":
        print("Rock versus...")
    elif mymove == "p":
     print("Paper versus...")
    elif mymove == "s":
        print("Scissors versus...")
        
    randomNum = random.randint(1,3)
    if randomNum==1:
        computerMove ="r"
        print("Rock")
    elif randomNum==2:
        computerMove="p"
        print("Paper")
    elif randomNum ==3:
        computerMove="s"
        print("Scissors") 
        
               
    if mymove==computerMove:
        ties=ties+1
        print("it is a tie!")
    elif mymove=="r" and computerMove=="p" :
        losses=losses+1
        print("You lose")
    elif mymove=="r" and computerMove=="s":
        wins=wins+1
        print("You win")
    elif mymove =="p" and computerMove=="r":
        wins=wins+1
        print("You win")
    elif mymove =="p" and computerMove=="s":
        losses=losses+1
        print("You lose")
    elif mymove=="s" and computerMove=="r":
        losses=losses+1
        print("You lose")
    elif mymove=="s" and computerMove=="p":
        wins=wins+1
        print("You win")

    print("________________________________")
            
            