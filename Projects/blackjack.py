import random


def welcome():
  print("Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this simple version of Blackjack, we only use the cards 2 through 11(ace).")
  print("\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!")


def get_cards():
  c = []
  # makes hand
  for i in range(2):
    c.append(random.randint(2, 11))
  return c


def hand_check(cards):
  card_value = 0
  
  for card in cards:
    card_value += card
  return card_value


def play():
  playing = True
  while playing == True:
    input('\nPress Enter to start playing.\n')
    cards = []
    
    cards += get_cards(), get_cards()
    print(f'Here is your hand:\n{cards[0]}')
    player_card_values = hand_check(cards[0])
    dealer_card_values = hand_check(cards[1])
    
    turn = 0
    stopped = False
    
    while True:
      if stopped == False:
        choice = input('Type in H to hit or S to stay: ')
        
        if choice == 'H':
          cards[0].append(random.randint(2, 11))
          print(f'\nHere is your new hand:\n{cards[0]}')
          player_card_values = hand_check(cards[0])
          
        if player_card_values > 21:
          print('You have busted. ')
          break
        
        if choice == 'S':
          stopped = True
          
      else:
        dealer_card_values = hand_check(cards[1])
        
        if dealer_card_values >= 17 and dealer_card_values < 21:
          print(f'\nHere is the dealers hand:\n{cards[1]}')
          
          if dealer_card_values > player_card_values:
            print('The dealer has won the game.')
            break
          
          if dealer_card_values < player_card_values:
            print('The player has won the game.')
            break
          
          if dealer_card_values == player_card_values:
            print('There is a tie.')
            break
        
        if dealer_card_values > 21:
          print(f'\nHere is the dealers hand:\n{cards[1]}')
          print('The dealer has busted.')
          break
        
        else:
          cards[1].append(random.randint(2, 11))


    

welcome()
play()