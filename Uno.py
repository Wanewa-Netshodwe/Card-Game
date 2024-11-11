""" 
Reverse - causes the Players to Swap Cards
"""
import random
from time import sleep
colors = ('Blue', 'Green', 'Yellow', 'Red')
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Draw', 'Reverse')
wild_cards =('Wild','Wild_Draw_Four')
gameover = False
vld =True
discard_pile = []
# if ANTI-CLOCKWISE SWAP CARDS
# Generate the deck of cards
cards = [{'color': c, 'number': n} for c in colors for n in numbers]
#Duplicate The Cards for full stack
cards += cards 
#Add the 0 card on each color 
for c in colors:
    #Add the wild cards
    # for w in wild_cards :
    #     cards.append({'color':'black','number':w})
    cards.append({'color': c, 'number': '0'})
#Shuffle Deck
random.shuffle(cards)
#Set Discard Pile
discard_pile.append(cards.pop())
#Players
players = [
    {
        'name': 'human',
        'cards': []
    },
    {
        'name': 'computer',
        'cards': []
    }
]
#check if is action card
def isSpecialCard(card):
    special_cards = ['Skip', 'Draw', 'Reverse']
    return card['number'] in special_cards

#deal the cards among the players
def handoutCards():
    for player in players:
        for _ in range(7):
            player['cards'].append(cards.pop())
            
#add 2 cards for the next player
def draw(p):
    idx = (players.index(p) + 1) % len(players)
    for _ in range(2):
        players[idx]['cards'].append(cards.pop())
# Reverse player order to swap cards
def reverse():  
    players.reverse()
    
def make_move(p):
      
      global vld
      if "'name': 'computer'" in str(p):
            for i in range(2):
                print('\nComputer playing .')
                sleep(.5) 
                print('Computer playing ..')
                sleep(.5) 
                print('Computer playing ...')
                sleep(.5)  
            print("\n---   Computer's Turn   ---")
            print('Top Card:', discard_pile[-1])
            idx = players.index(p)
            for card in players[idx]['cards']:
                #computer card selection              
                # if the color or the number of the card is equal to the card in the discard pile 
                if card['color'] == discard_pile[-1]['color'] or card['number'] == discard_pile[-1]['number']:
                    #print the computer play
                    print("Computer plays:", card)
                    #check if selected card is a action card
                    if isSpecialCard(card):
                        if card['number'] == 'Reverse':
                            reverse()
                            return
                        if card['number'] == 'Skip':
                            discard_pile.append(card)
                            players[idx]['cards'].remove(card)
                            print('itsskip')
                            vld = False
                            print(len(p['cards']))
                            return
                        elif card['number'] == 'Draw':
                            print('its a draw card ')
                            draw(players[idx])
                            print(len(p['cards']))
                            return
                    discard_pile.append(card)
                    players[idx]['cards'].remove(card)
                    print(len(p['cards']))
                    return
                    
                
                    # If no matching card, draw a card
            print("Computer draws a card")
            players[idx]['cards'].append(cards.pop())   
            
            return
      else:
            print("\n---   Your Turn    ---")
            idx = players.index(p)
            print("index--- \tcards\n")
            #loop though the human cards
            for i, card in enumerate(players[0]['cards']):
                print(i, '        ', card)
            print('Top Card:', discard_pile[-1])
            option = input("Enter 'D' to draw a card or the index of your card to play: ")
            # if option is 'd' then draw card 
            if option.lower() == 'd':
                players[idx]['cards'].append(cards.pop())
                return
            # if option is an int  
            elif option.isdigit():
                index = int(option)
                #check if the index is not higher  than the player cards
                if index in range(len(players[idx]['cards'])):
                    selected_card = players[idx]['cards'][index]
                    # if the color or the number of the card is equal to the card in the discard pile 
                    if selected_card['color'] == discard_pile[-1]['color'] or selected_card['number'] == discard_pile[-1]['number']:
                        print("You play:", selected_card)
                        discard_pile.append(selected_card)
                        players[idx]['cards'].remove(selected_card)
                        
                        if isSpecialCard(selected_card):
                            if selected_card['number'] == 'Reverse':
                                reverse()
                                
                            elif selected_card['number'] == 'Draw':
                                draw(players[idx])
                                
                            elif selected_card['number'] == 'Skip':
                                make_move(p)  
                                
                    else:
                        print("Invalid card. You must match color or number.")
                        make_move(p) 
                        
                else:
                    print("Invalid card index.")
                    make_move(p) 
                 
            else:
                print("Invalid input.")
                make_move(p) 
                                      
def gameStart(gameover):
    print('NB : A little  Rule Change  Reverse- Swaps The  Cards GoodLuck :) ')
    #Deal The cards
    handoutCards()     
    while not gameover:
       for player in players:
           make_move(player)
           if len(player['cards']) <1 :
               print('PLAYER :',player['name'],'Won ')
               return               
# Start the game
gameStart(gameover)
