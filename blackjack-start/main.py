import random

dealer_cards = []
player_cards = []
deck = []
for card in range (2,12):
  for card_for_each_type in range(0,4):
    if card == 10:
      for face_cards in range(0,4):   #Add 4x Jacks, Queens, Kings
        deck.append(card)
    else:
      deck.append(card)

def get_card_from_deck(hand):
  position = random.randint(0,int(len(deck))-1)
  card = deck[position]
  if card == 11:
    card = picked_ace(card, hand)
  hand.append(card)
  deck.pop(position)

def picked_ace(card,hand):
  score = calculate_score(hand)
  if score+card > 21:
    card = 1
    print("print ace 1")
  if hand == dealer_cards:
    card = dealer_ace(card,score)
  elif hand == player_cards:
    card_ph = int(input("Picked an ace, 1 or 11:"))
    return card_ph
  return card
  
def dealer_ace(card, dealer_score):
  player_score = calculate_score(player_cards)
  dealer_score = dealer_score+card
  if dealer_score > player_score:
    return card
  elif dealer_score == player_score and dealer_score < 15:
    return card
  elif dealer_score < player_score and dealer_score < 16:
    card = 1
    return card
    
def show_cards(hand):
  card_str = ""
  score = 0
  for i in range(0, len(hand)):
    if hand == dealer_cards and i == 0:
      card_str += "[#]"
    else:
      score += hand[i]
      text = str(hand[i])
      card_str +=  "[" +text+ "]"
  print(f"{card_str}    {score}")

def show_cards_without_blank(hand):
  card_str = ""
  score = 0
  for i in range(0, len(hand)):
    score += hand[i]
    text = str(hand[i])
    card_str +=  "[" +text+ "]"
  print(f"{card_str}    {score}")
  

def calculate_score(hand):
  score = 0
  for card in hand:
    score += card
  return score

def two_cards_each():
  for i in range (0,2):
    get_card_from_deck(player_cards) 
    get_card_from_deck(dealer_cards)    
  show_cards(player_cards)
  show_cards(dealer_cards)

### Gameloop 
two_cards_each()
playing = True
dealer_turn = False
while playing:
  decision = input("Want another card ? yes/no ").lower()
  if decision == "no":
    print("Stopped at: ")
    show_cards(player_cards)
    playing = False
    dealer_turn = True
  else:
    get_card_from_deck(player_cards)
    show_cards(player_cards)
    score = calculate_score(player_cards)
    if score > 21:
      playing = False
      print("Bust!")
    if score == 21:
      print("Blackjack!")
      playing = False
      dealer_turn = True
      
print("\nDealers turn")

while dealer_turn:
  show_cards(dealer_cards)
  dealer_score = calculate_score(dealer_cards)
  player_score = calculate_score(player_cards)
  if dealer_score > 21:
    dealer_turn = False
    show_cards_without_blank(dealer_cards)
    print("Dealer busted! You win")
  elif dealer_score < player_score:
      get_card_from_deck(dealer_cards)
  elif dealer_score > player_score:
      dealer_turn = False
      show_cards_without_blank(dealer_cards)
      print("Dealer wins")
  elif dealer_score == player_score and dealer_score > 14:
      dealer_turn = False
      show_cards_without_blank(dealer_cards)
      print("Push - nobody wins")
  
    
    