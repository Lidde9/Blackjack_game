#!/usr/bin/env python
# coding: utf-8

# ## Blackjack Game
# 
# 

# #### The game consists of functions and a game logic at the end

# ### Functions

# deck = [("2H", 2), ("3H", 3), ("4H", 4), ("5H", 5), ("6H", 6), ("7H", 7), ("8H", 8), ("9H", 9), ("10H", 10), ("JH", 10), ("QH", 10), ("KH", 10), ("AH", 11),
#                 ("2D", 2), ("3D", 3), ("4D", 4), ("5D", 5), ("6D", 6), ("7D", 7), ("8D", 8), ("9D", 9), ("10D", 10), ("JD", 10), ("QD", 10), ("KD", 10), ("AD", 11),
#                 ("2C", 2), ("3C", 3), ("4C", 4), ("5C", 5), ("6C", 6), ("7C", 7), ("8C", 8), ("9C", 9), ("10C", 10), ("JC", 10), ("QC", 10), ("KC", 10), ("AC", 11),
#                 ("2S", 2), ("3S", 3), ("4S", 4), ("5S", 5), ("6S", 6), ("7S", 7), ("8S", 8), ("9S", 9), ("10S", 10), ("JS", 10), ("QS", 10), ("KS", 10), ("AS", 11)]

# In[2]:


# Import library to clear output when playing the game
from IPython.display import clear_output


# In[3]:


# Creating of deck of cards by importing random

import random
def deck_of_cards():
    deck = [("2♥️", 2), ("3♥️", 3), ("4♥️", 4), ("5♥️", 5), ("6♥️", 6), ("7♥️", 7), ("8♥️", 8), ("9♥️", 9), ("10♥️", 10), ("J♥️", 10), ("Q♥️", 10), ("K♥️", 10), ("A♥️", 11, 1),
                ("2♦️", 2), ("3♦️", 3), ("4♦️", 4), ("5♦️", 5), ("6♦️", 6), ("7♦️", 7), ("8♦️", 8), ("9♦️", 9), ("10♦️", 10), ("J♦️", 10), ("Q♦️", 10), ("K♦️", 10), ("A♦️", 11, 1),
                ("2♣️", 2), ("3♣️", 3), ("4♣️", 4), ("5♣️", 5), ("6♣️", 6), ("7♣️", 7), ("8♣️", 8), ("9♣️", 9), ("10♣️", 10), ("J♣️", 10), ("Q♣️", 10), ("K♣️", 10), ("A♣️", 11, 1),
                ("2♠️", 2), ("3♠️", 3), ("4♠️", 4), ("5♠️", 5), ("6♠️", 6), ("7♠️", 7), ("8♠️", 8), ("9♠️", 9), ("10♠️", 10), ("J♠️", 10), ("Q♠️", 10), ("K♠️", 10), ("A♠️", 11, 1)]
    random.shuffle(deck)
    return deck
    


# In[4]:


# Create number of boards depending on number of players inputed

def create_player_boards(x):
    """create x amounts of empty player boards """
    
    #dealer_board = []
    player_boards = [[] for i in range(x)]
    return player_boards
    


# In[5]:


# In case of a split this function will split the players hand into two seperate game boards

def split_board(player_board):
    #list_of_two_split_cards = []
    split_player_board = []
    for i in range(2):
        temp_list = []        
        temp_list.append(player_board[i])
        split_player_board.append(temp_list)
        
    split_player_board[0].append(draw_card(deck))
    split_player_board[1].append(draw_card(deck))
    
    return split_player_board
    # return player_


# In[6]:


# First display board which includes all player card but hides one of the dealers cards

def display_board(player_boards, dealer_board, player_turn, board_turn = 5):
    game = 0
    for i in range(len(player_boards)):
        if type(player_boards[i][0]) == list:
            game = 0
            for board_current in player_boards[i]:
                player_print = []
                game += 1
                for tuple_item in board_current:
                    player_print.append(tuple_item[0])
                    
                if i == player_turn and board_turn == 0 :  ##index number of current element
                    print (f"----> Player {i+1} Game {game} {player_print} {check_value(board_current)}")
                elif i == player_turn and board_turn == 1 :
                    print (f"----> Player {i+1} Game {game} {player_print} {check_value(board_current)}")
                else:
                    print (f"Player {i+1} Game {game} {player_print}")
        else:    
            player_print = []
            for tuple_item in player_boards[i]:
                player_print.append(tuple_item[0])
            if i == player_turn:
                print (f"----> Player {i+1} {player_print} {check_value(player_boards[i])}")
            else:
                print (f"Player {i+1} {player_print}")
        
    dealer_print = []
    for tuple_item in dealer_board[1:]:
        dealer_print.append(tuple_item[0])
    
    print("----------------------------")
    print(f"Dealer  : ['👀'] {dealer_print}")
    print("\n")


# In[7]:


# This display board plus the dealers cards, which is used when the players turn are finished and the dealer starts playing

def display_board_all(player_boards, dealer_board):
    game = 0
    for i in range(len(player_boards)):
        if type(player_boards[i][0]) == list:
            game = 0
            for board_current in player_boards[i]:
                player_print = []
                game += 1
                for tuple_item in board_current:
                    player_print.append(tuple_item[0])
                print (f"Player {i+1} Game {game} {player_print}")
        else:    
            player_print = []
            for tuple_item in player_boards[i]:
                player_print.append(tuple_item[0])
            print (f"Player {i+1} {player_print}")
        
    dealer_print = []
    for tuple_item in dealer_board:
        dealer_print.append(tuple_item[0])
        
        
    print("----------------------")
    print(f"Dealer  : {dealer_print}")
    print("\n")


# In[8]:


# End display board to show the full results of the gmae when all play is finished

def display_board_end(player_boards, dealer_board, lst_results):
    #ii = range(len(player_boards))
    game2 = 0
    for i in range(len(player_boards)):
        game = 0
        if type(player_boards[i][0]) == list:
            for board_current in player_boards[i]:
                player_print = []
                game += 1
                for tuple_item in board_current:
                    player_print.append(tuple_item[0])
                print (f"Player {i+1} Game {game} {player_print}  ={check_value(board_current)}:  {lst_results[i][game-1]}")
            #i += 1 #{lst_results[i][game-1]}
        else:    
            player_print = []
            for tuple_item in player_boards[i]:
                player_print.append(tuple_item[0])
            print (f"Player {i+1} {player_print}  ={check_value(player_boards[i])}:  {lst_results[i+game2]}")       
         
    dealer_print = []
    for tuple_item in dealer_board:
        dealer_print.append(tuple_item[0])
        
        
    print("----------------------")
    print(f"Dealer  : {dealer_print} {check_value(dealer_board)}")
    print("\n")
    
    #print(check_value(player_boards[i][x]))
    #print(check_value(dealer_board))


# In[9]:


# Draw card function when player or dealer hits

def draw_card(deck):
    card = deck.pop(0)
    return card
    


# In[10]:


# Initial board setup when the game starts

def board_start():
    for i in range(len(player_boards)):
        player_boards[i].append(draw_card(deck))
    dealer_board.append(draw_card(deck))
    for i in range(len(player_boards)):
        player_boards[i].append(draw_card(deck))
    dealer_board.append(draw_card(deck))


# In[11]:


# Checks value of the board

def check_value(board):
    total_value = 0
    
    #if # list 
    for tuple_item in board:
        total_value += tuple_item[1]
    
    value_ace = board_ace(board)
    
    while total_value > 21 and value_ace > 0:
        total_value = total_value - 10
        value_ace-= 1
    return total_value


# In[12]:


# If you have an ace it can either be a 1 or 11. This functions includes this functionality to check value function

def board_ace(board):
    ace_count = 0
    aces = ["A♠️", "A♥️", "A♣️", "A♦️"]
    for tuple_item in board:
        if tuple_item[0] in aces:
            ace_count +=1
    return ace_count


# In[13]:


# Checks for blackjack

def check_blackjack(total_value):
    if int(total_value) == 21:
        #print("Blackjack!!!!!!!!!!!!!!!!!!!!!!!")
        return False
    else: #spelar ingen roll
        return True


# In[14]:


# Check if player is bust

def check_bust(total_value):    
    if int(total_value) > 21:
        #print("BUST!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return False
    else: #spelar ingen roll
        return True


# In[15]:


# Check for the result at the end of the game (comparing player vs. dealer hand)

def check_win2(player_boards, dealer_board):  
    lst_results = []
    
    d_value = check_value(dealer_board)
    
    for i in range(len(player_boards)):
        # Clear the temp_list for each player
        
        if type(player_boards[i][0]) == list:
            temp_list = []
            for hand in player_boards[i]:  # Use a different variable than 'i'
                p_value = check_value(hand)
                if p_value > 21:
                    temp_list.append("BUST")
                elif p_value > d_value:
                    temp_list.append("WIN")
                elif p_value == d_value:
                    temp_list.append("TIE")
                elif d_value > 21:
                    temp_list.append("WIN")
                else:
                    temp_list.append("LOSS") 
                    
            lst_results.append(temp_list)
        else:
            p_value = check_value(player_boards[i])
            if p_value > 21:
                lst_results.append("BUST")
            elif p_value > d_value:
                lst_results.append("WIN")
            elif p_value == d_value:
                lst_results.append("TIE")
            elif d_value > 21:
                lst_results.append("WIN")
            else:
                lst_results.append("LOSS")
    
    return lst_results


# In[16]:


# Hit function

def hit(board):
    card = draw_card(deck)
    player_board
    return 
    


# In[17]:


# Ask player for a decision when playing its turn

def player_decision():
    i = ""
    while i.lower().startswith("h"):
        i = input("Do you want to hit or pass?")
    
    if i.lower().startswith("h"):
        player_board.append(draw_card(deck))
        print("YOU HIT?!")
        return True
    else:
        print("You pass")
        return False


# In[27]:


# Improt time to load animation function, to allow some time before dealer plays their hand

import time

def loading_animation(duration, string_message):
    print("Loading...", end='', flush=True)
    for _ in range(duration):
        time.sleep(0.2)  # Wait for 0.1 seconds
        print(".", end='', flush=True)
    for charr in string_message:
        time.sleep(0.05)  # Wait for 0.1 seconds
        print(charr, end='', flush=True)
        
    print(".")



# # GAME LOGIC AND MAIN FUNCTION

# In[19]:


# Run below to initiate game


# In[25]:


import time

######################## INITIAL GAME CONDITIONS ##########################
game_on = True
players_turn = True
players_turn_split = True
dealer_turn = True
player_turn_num = 0

######################## START GAME ##########################
while game_on:
    print("GAME ON WHILE LOOP")
    
    ######################## ASK FOR PLAYER NUMBERS ##########################
    while True:
        try:
            user_input = int(input("Please choose amount players between 1 and 8: "))
            if 1 <= user_input <= 8:
                break  # Valid input, exit the loop
            else:
                print("Input must be between 1 and 8. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    player_boards = create_player_boards(user_input)
    
    ######################## INITIAL GAME BOARDS ##########################
    
    player_board=[]
    dealer_board=[]
    deck = []
    deck = deck_of_cards()
    players_turn = 0
    board_start()
    
################### PLAYER TURN LOOP START ################

    for i in range(len(player_boards)):
        #display("1")
        players_turn=True
    
    ################### INDIVIDUAL PLAYER TURN ####################
        while players_turn:  ##for player_board in player_boards:
            print("PLAYER TURN WHILE LOOP")
            clear_output(wait=True)
            display("1")
            display_board(player_boards, dealer_board, player_turn_num)

            ################### CHECK BLACKJACK AND 21 ####################
            players_turn_split = True
            if not check_blackjack(check_value(player_boards[i])):
                if len(player_boards[i]) == 2:
                    print("Players has blackjack")
                    player_turn_num += 1
                    display("")
                    time.sleep(1.5)
                    break
                else:
                    print("Player has 21")
                    player_turn_num += 1
                    display("")
                    time.sleep(1.5)
                    break

        ############### SPLIT TURN LOOP ###############           
            if len(player_boards[i]) == 2:
                x = ""
                if player_boards[i][0][0][0] == player_boards[i][1][0][0]:
                    while not (x.lower().startswith("y") or x.lower().startswith("n")):
                        x = input(f"Player {i+1}: Do you want to split?      Choice YES or NO: ")
                        time.sleep(0.25)
                    if x.lower().startswith("n"):
                        pass
                    elif x.lower().startswith("y"):
                        player_boards[i] = split_board(player_boards[i])
                        print(player_boards[i])
                        
                        for current_board_iteration in range(2):
                            players_turn_split = True
                            while players_turn_split:##for player_board in player_boards:
                                clear_output(wait=True)
                                display("2")
                                print("PLAYER SPLIT TURN WHILE LOOP")
                                display_board(player_boards, dealer_board, player_turn_num, current_board_iteration) 
                                
                                ################### CHECK BLACKJACK AND 21 ####################
                                if not check_blackjack(check_value(player_boards[i][current_board_iteration])):
                                    if len(player_boards[i][current_board_iteration]) == 2:
                                        print("Players has blackjack")
                                        players_turn_split = False
                                        #player_turn_num += 1
                                        time.sleep(1.5)
                                        break
                                    else:
                                        print("Player has 21")
                                        #player_turn_num += 1
                                        players_turn_split = False
                                        time.sleep(1.5)
                                        break
                                    
                                ############# SPLIT BOARD PLAYR TURN ###################
                                if not check_bust(check_value(player_boards[i][current_board_iteration])):
                                    print("Player is bust")

                                print(check_value(player_boards[i][current_board_iteration]))
                                print("split check value")
                                #print(check_value(dealer_board))

                                display("3")
                                y = ""
                                while not (y.lower().startswith("h") or y.lower().startswith("p")):
                                    y = input(f"Player {i+1} Game {current_board_iteration+1}: Do you want to hit or pass?    Choice: ")
                                    time.sleep(0.25)
                                if y.lower().startswith("h"):
                                    player_boards[i][current_board_iteration].append(draw_card(deck))
                                    print("YOU HIT?!")
                                else:
                                    print("You pass")
                                    #player_turn_num += 1
                                    players_turn_split = False
                                    break

                                if not check_blackjack(check_value(player_boards[i][current_board_iteration])):
                                    players_turn_split = False
                                    #player_turn_num += 1
                                    time.sleep(1.5)
                                    break
                                if not check_bust(check_value(player_boards[i][current_board_iteration])):
                                    players_turn_split = False
                                    #player_turn_num += 1
                                    time.sleep(1.5)
                                    break
                        player_turn_num += 1                           
                
        ############# END OF SPLIT TURN ############ 

            ############# PLYAER TURN ###################
            if players_turn_split == False:
                break
            if not check_bust(check_value(player_boards[i])):
                print("Player is bust")

            display("4")
            y = ""
            while not (y.lower().startswith("h") or y.lower().startswith("p")):
                y = input(f"Player {i+1}: Do you want to hit or pass?    Choice: ")
                time.sleep(1.5)
            if y.lower().startswith("h"):
                player_boards[i].append(draw_card(deck))
                print("YOU HIT?!")
            else:
                print("You pass")
                player_turn_num += 1
                players_turn = False
                break

            if not check_blackjack(check_value(player_boards[i])):
                players_turn = False
                player_turn_num += 1
                display("")
                time.sleep(1.5)
                break
            if not check_bust(check_value(player_boards[i])):
                players_turn = False
                player_turn_num += 1
                display("")
                time.sleep(1.5)
                break         
            
    print("End of Player Turn")
########## END OF PLAYER TURN ##############

########## DEALER TURN #####################
   
    print("\n")
    print("------------<<<DEALER>> <<TURN>>>-------------")    
    
    while dealer_turn:
        clear_output(wait=True)
        #print("DEALER TURN WHILE LOOP")
        display_board_all(player_boards, dealer_board)
        
        #if not check_bust(check_value(player_board)):
            #print ("Dealer won, player has busteeeed")
            #break
        if not check_blackjack(check_value(dealer_board)) and len(dealer_board) == 2:
            print("Dealer has blackjack")
            break
        if not check_bust(check_value(dealer_board)):
            print("Dealer is bust")
            break
        
        while check_value(dealer_board) < 17:
            loading_animation(10, " Dealer draws card......")
            clear_output(wait=True)
            dealer_board.append(draw_card(deck))
            display_board_all(player_boards, dealer_board)
            if not check_bust(check_value(dealer_board)):
                dealer_turn = False
                print("Dealer is bust")
                #print("Player has won")
                clear_output(wait=True)
                break
            #clear_output(wait=True)
                
        dealer_turn = False

########## DEALER TURN END #####################
        
############### END SCREEN RESULTS ####################
    loading_animation(10, " ::::::::RESULTS:::::::")
    clear_output(wait=True)
    print (":::::RESULTS:::::")
    lst_results = check_win2(player_boards, dealer_board)
    #print (lst_results)
    #display_board_all(player_boards,dealer_board)
    display_board_end(player_boards, dealer_board, lst_results)
            
    game_on=False


# ###### 
