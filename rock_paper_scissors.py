# code made by Miłosz Łyczywek
import random

figures=['rock','paper','scissors']
point_player=0
point_comp=0
game_running=True

# how much rounds you want to play
round_count=int(input("Type in at what score the match ends: "))
# player move

def player_move():
    global figures
    global choose
    choose=str(input("Choose rock, paper or scissors: "))
    if choose==figures[0]:
        print("You chose rock.")
    elif choose==figures[1]:
        print("You chose paper.")
    elif choose==figures[2]:
        print("You chose scissors.")
    elif choose not in figures:
        print("You typed in something wrong...")
        quit()

# computer move

def comp_move():
    global figures
    global random_move
    random_move=random.randrange(3)
    if random_move==0:
        print("Your enemy chose rock.")
        random_move=figures[0]
    elif random_move==1:
        print("Your enemy chose paper.")
        random_move=figures[1]
    elif random_move==2:
        print("Your enemy chose scissors.")
        random_move=figures[2]

# moves check
def draw_check():
    if choose==random_move:
        print("It's a draw!")

def win_check():
    global point_player
    global point_comp
     
    if choose!=random_move:
        if choose==figures[0] and random_move==figures[1]:
            print("Enemy won.")
            point_comp+=1
        elif choose==figures[0] and random_move==figures[2]:
            print("You won")
            point_player+=1
        elif choose==figures[1] and random_move==figures[0]:
            print("You won.")
            point_player+=1
        elif choose==figures[1] and random_move==figures[2]:
            print("Enemy won.")
            point_comp+=1
        elif choose==figures[2] and random_move==figures[0]:
            print("Enemy won.")
            point_comp+=1
        elif choose==figures[2] and random_move==figures[1]:
            print("You won.")
            point_player+=1
        

# score table
def score():
    print(point_player,":",point_comp)

# game end
def end():
    global game_running
    if point_player == round_count or point_comp == round_count:
        game_running=False
    if point_player==round_count:
        print("You won the whole game, congratulations!!!")
    elif point_comp==round_count:
        print("Oh, you lost :(")

# code execution
print("--------------")
while game_running:
    player_move()
    comp_move()
    draw_check()
    win_check()
    score()
    print("--------------")
    end()
