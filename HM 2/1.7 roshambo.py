#timothy S Brower
#roshambo exercise 1.7



plr1 = raw_input("Player one please choose rock, paper or, scissors:")
plr1 = plr1.lower()

#make sure player one is not trying to cheat
while plr1 != "rock" and plr1 != "paper" and plr1 != "scissors" :
    print 'Player one there are only three acceptibal inputs' , plr1, "is not one of them. Please try again!"
    plr1 = raw_input("Player one please choose rock, paper or, scissors:")
    plr1 = plr1.lower()

plr2 = raw_input("Player two please choose rock, paper or, scissors:")
plr2 = plr2.lower()

#make sure player two is not trying to cheat
while plr2 != "rock" and plr2 != "paper" and plr2 != "scissors" :
    print 'Player two there are only three acceptibal inputs' , plr2, "is not one of them. Please try again!"
    plr1 = raw_input("Player Two please choose rock, paper or, scissors:")
    plr1 = plr2.lower()

#check to see who wone    
if plr1 == "rock":
    if plr2 == "paper":
        print "paper covers rock player two wins"
    elif plr2 == "scissors":
        print "Rock smashes scissors player one wins"
    else:
        print "its a tie"

if plr1 == "paper":
    if plr2 == "rock":
        print "paper covers rock player one wins"
    elif plr2 == "scissors":
        print "Scissors cut paper player two wins"
    else:
        print "its a tie"

if plr1 == "scissors":
    if plr2 == "paper":
        print "Scissors cur paper player one wins"
    elif plr2 == "rock":
        print "Rock smashes scissors player two wins"
    else:
        print "its a tie"

