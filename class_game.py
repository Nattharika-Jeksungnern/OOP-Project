import random
import math
class FullDeck :
    def __init__(self, card, number) :
        self._card_collection = card #Aggragation with Card
        self._num_card = number

    def tier_1(self, deck):
        for card in self._card_collection:
            if card._tier == 1:
                deck.append(card)

    def tier_2(self, deck):
        for card in self._card_collection:
            if card._tier == 2:
                deck.append(card)
    
    def tier_3(self, deck):
        for card in self._card_collection:
            if card._tier == 3:
                deck.append(card)

class Card :
    def __init__(self, name, cost, point, tier, value) :
        self._name = name #"W311"
        self._cost = cost #[3,1,0,0,1]
        self._point = point #0
        self._tier = tier #"in_deck"
        self._value = value
    def update_owner(player):
        pass
    
    def print_card(self):
        print('name :', end='')
        print(self._name)
        print('cost :',end='')
        print(self._cost)
        print('point :',end='')
        print(self._point)
        print('tier :',end='')
        print(self._tier)
        print('value :',end='')
        print(self._value)
        print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
class Deck (FullDeck):
    def __init__(self,card, tier, number) :
        FullDeck.__init__(self, card, number)
        self.__tier = tier
        self._top_deck = []
        #self._show_deck = [] #Deck call Card
    def print_top_deck(self):
        for card in self._top_deck:
            card.print_card()

    def shuffle_deck(self):
        for i in range(5):
            random.shuffle(self._card_collection)
            self._top_deck.append(self._card_collection[0])
            self._card_collection.remove(self._card_collection[0])

    def random_top_deck(self):
        random.shuffle(self._card_collection)
        self._top_deck.append(self._card_collection[0])
        self._card_collection.remove(self._card_collection[0])

class DeckNoble :
    def __init__(self, noble, number) :
        self._noble_collection = noble #[] #Aggregation with Noble
        self._num_noble = number #3+1+1

class Noble :
    def __init__(self, name, condition, point) :
        self._name = name #"Arm"
        self.condition = condition #[]
        self._point = point
        #self.__status_noble = status #False
        #self._owner = owner #"Premier" #Association with PLayer

    def update_owner(player):
        pass

color_coin = [ "White", "Blue", "Green", "Red", "Black"]
class StackCoin :
    def __init__(self) :
        self._coins = [] # [7,7,7,7] #Aggregation with Coin

    def pick_coin(self, choose_coin) :
        coin = []

        if len(choose_coin) == 2:
            if choose_coin[0] != choose_coin[1]:
                print("Can't pick coin, please pick 1 pair or 3 differrent")
                return False
            else :
                for list_coin in self._coins:
                    if len(list_coin) - 1 < 4 and list_coin[0]._color == choose_coin[0]:
                        print("Can't pick coin.")
                        return False
        elif len(choose_coin) == 3:
            if choose_coin[0] == choose_coin[1] or choose_coin[1] == choose_coin[2] or choose_coin[0] == choose_coin[2]:
                print("Can't pick like this. Please choose 3 different or 1 pair.")
                return False
            for temp in self._coins:
                if len(temp) - 1 == 0:
                    print("0 coin, can't pick.")
                    return False
        else :
            print("Can't pick like this. Please choose 3 different or 1 pair.")
            return False
        
        for i in range(len(choose_coin)):
            for list_coin in self._coins:
                if choose_coin[i] == list_coin[0]._color :
                    if len(list_coin) - 1 > 0:
                        coin.append(list_coin[0])
                        list_coin.remove(list_coin[0])
                    """  else :
                        print("0 coin, can't pick.")
                        return False """
        #print check                  
        return coin
    
    def check_coin(self):
        for b in self._coins:
            g = []
            for i in b:
                g.append(i._color)
            g.append(len(b))
            print(g) 
        print('*******************')

    def update_coins(self, coin):
        for temp in coin:
            for list_coin in self._coins:
                if temp._color == list_coin[0]._color:
                    list_coin.append(temp)
   
        
class Coin :
    def __init__(self, color) :
        self._color = color #"white"
        self.__value = 1


class GoldCoin :
    def __init__(self) :
        self._coins = ["Gold", "Gold", "Gold", "Gold", "Gold"]
    
    def pay_gold_coin(self):
        coin = self._coins[0]
        self._coins.remove(coin)
        return coin
    
    def update_gold_coin(self, coin):
        self._coins.append(coin)

    def print_gold_coin(self):
        print(self._coins)



class BoardRoom :
    def __init__(self, number, target, status, result, deck_tier_1, deck_tier_2, deck_tier_3, player, noble, coin, gold_coin) :
        self._num_player = number #2+1+1
        self._target = target #15
        self._status_room = status #"playing"
        self._result = result #""
        self._deck_1 = deck_tier_1 #[]
        self._deck_2 = deck_tier_2 #[]
        self._deck_3 = deck_tier_3 #[]
        self._player = player #[]
        self._noble = noble #[]
        self._coin = coin #[]
        self._gold_coin = gold_coin #[]
        self._flag = 0
        self._last_turn = False

    def show_card(self):
        print("tier 3")
        for card in self._deck_3:
            card.print_card()
        print("-"*40)
        print("tier 2")
        for card in self._deck_2:
            card.print_card()
        print("-"*40)
        print("tier 1")
        for card in self._deck_1:
            card.print_card()
        print("-"*40)
        
    def add_player(self, player):
        self._player.append(player)

    def check_player_in_room(self):
        if self._num_player > len(self._player):
            return True
        else :
            return False

    def update_flag(self):
        self._flag += 1
        self._flag = self._flag % self._num_player
    
    def buy_card(self,player,card_name):
        search=True
        while search:
            for i in self._deck_1:
                if card_name == i._name:
                    current_card=i
                    current_deck=self._deck_1
                    search=False
                    continue
            for i in self._deck_2:
                if card_name == i._name:
                    current_card=i
                    current_deck=self._deck_2
                    search=False
                    continue
            for i in self._deck_3:
                if card_name == i._name:
                    current_card=i
                    current_deck=self._deck_3
                    search=False
                    continue
        can_buy = True
        discount = player.discount_coin()
        player_coin = 0
        card_coin = 0
        for i in range(5):     
            if len(player._coins[i]) + discount[i] < current_card._cost[i]:
                player_coin += len(player._coins[i]) + discount[i]
                card_coin += current_card._cost[i]
                can_buy = False

        if not can_buy:
            if len(player._gold_coins) >= card_coin - player_coin:
                can_buy = True
                """ for i in range(card_coin - player_coin):
                    self._gold_coin.update_gold_coin(player.pay_gold_coin()) """

        if can_buy:
            #update score
            player.update_score(current_card._point)
            #update card
            player.update_card(current_card)
            #remove card from deck
            current_deck.remove(current_card)

            #remove coin from player
            for i in range(5):
                print(1)
                if current_card._cost[i] > 0:
                    print("Mark")
                    if current_card._cost[i] > len(player._coins[i]) + discount[i]:
                        print("cost > coin")
                        diff = current_card._cost[i] - len(player._coins[i]) - discount[i]
                        self._coin.update_coins(player.pay_coin(i, len(player._coins[i])))
                        for i in range(diff):
                            self._gold_coin.update_gold_coin(player.pay_gold_coin())
                    else :
                        print("coin > cost")
                        self._coin.update_coins(player.pay_coin(i, current_card._cost[i]))
            return current_card._tier
        else:
            print("Not enough coin, can't buy.")
            return False

    def buy_hold_card(self, player, card_name):
        search = False
        for card in player._hold_card:
            if card._name == card_name:
                current_card = card
                search = True
        if not search:
            print("Don't have this card on your hand")
            return False
        can_buy = True       
        discount = player.discount_coin()
        player_coin = 0
        card_coin = 0
        for i in range(5):     
            if len(player._coins[i]) + discount[i] < current_card._cost[i]:
                player_coin += len(player._coins[i]) + discount[i]
                card_coin += current_card._cost[i]
                can_buy = False

        if not can_buy:
            if len(player._gold_coins) >= card_coin - player_coin:
                can_buy = True
                """ for i in range(card_coin - player_coin):
                    self._gold_coin.update_gold_coin(player.pay_gold_coin()) """

        if can_buy:
            #update score
            player.update_score(current_card._point)
            #update card
            player.update_card(current_card)
            #remove card from deck
            player._hold_card.remove(current_card)

            #remove coin from player
            for i in range(5):
                print(1)
                if current_card._cost[i] > 0:
                    print("Mark")
                    if current_card._cost[i] > len(player._coins[i]) + discount[i]:
                        print("cost > coin")
                        diff = current_card._cost[i] - len(player._coins[i]) - discount[i]
                        self._coin.update_coins(player.pay_coin(i, len(player._coins[i])))
                        for i in range(diff):
                            self._gold_coin.update_gold_coin(player.pay_gold_coin())
                    else :
                        print("coin > cost")
                        self._coin.update_coins(player.pay_coin(i, current_card._cost[i]))
            return True
        else:
            print("Not enough coin, can't buy.")
            return False
        
    def update_top_deck(self, deck, tier):
        if tier == 1:
            self._deck_1 = deck
        elif tier == 2:
            self._deck_2 = deck
        elif tier == 3:
            self._deck_3 = deck

    def hold_card(self, player, card_name):
        search=True
        while search:
            for i in self._deck_1:
                if card_name == i._name:
                    current_card=i
                    current_deck=self._deck_1
                    search=False
                    continue
            for i in self._deck_2:
                if card_name == i._name:
                    current_card=i
                    current_deck=self._deck_2
                    search=False
                    continue
            for i in self._deck_3:
                if card_name == i._name:
                    current_card=i
                    current_deck=self._deck_3
                    search=False
                    continue
        #card เข้า player
        player.add_hold_card(current_card)
        current_deck.remove(current_card)
        #gold coin เข้า player
        if self._gold_coin._coins != []:
            player.update_gold_coin(self._gold_coin.pay_gold_coin())
        return current_card._tier

    def return_coins(self, color, player):
        if color == 'Gold':
            self._gold_coin.update_gold_coin(player.pay_gold_coin())
            return True
        for i in range(5):
            if color_coin[i] == color:
                self._coin.update_coins(player.pay_coin(i, 1))
        return False
        
    def get_last_turn(self, player):
        if player._score_player == 15:
            self._last_turn = True
            return True
        return False
    def last_player(self, player):
        if player._name == self._player[self._num_player - 1]._name and self._last_turn:
            print("last player")

    def win(self):
        score = 0
        for player in self._player:
            if player._score_player > score:
                winner = player._name
                score = player._score_player
        print(winner)

    def show(self) :
        pass

    def calculate_score(self) :
        pass

    def check_card_player_to_get_noble(self) :
        pass