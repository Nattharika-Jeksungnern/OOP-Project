import random
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
        
        print('-+-+-+-+-+-+-+')
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
        else :
            print("Can't pick like this. Please choose 3 different or 1 pair.")
            return False
        
        for i in range(len(choose_coin)):
            for list_coin in self._coins:
                if choose_coin[i] == list_coin[0]._color :
                    if len(list_coin) - 1 > 0:
                        coin.append(list_coin[0])
                        list_coin.remove(list_coin[0])
                    else :
                        print("0 coin, can't pick.")
                        return False
                        

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

    def return_coin(self, coin, player):
        for p_coin in player._coins :
            if p_coin._color == coin:
                self._coins.append(p_coin)
                player._coins.remove(p_coin)

    """ def update_coins(self, coin):
        for i in range(len(color_coin)):
            if coin == color_coin[i]:
                self._coins[i].append(coin) """
   
        
class Coin :
    def __init__(self, color) :
        self._color = color #"white"
        self.__value = 1


class GoldCoin :
    def __init__(self) :
        self._coins = ["Gold", "Gold", "Gold", "Gold", "Gold"]



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

    def show_card(self):
        print("tier 3")
        for card in self._deck_3:
            card.print_card()
        print("-"*20)
        print("tier 2")
        for card in self._deck_2:
            card.print_card()
        print("-"*20)
        print("tier 1")
        for card in self._deck_1:
            card.print_card()
        print("-"*20)
        
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
        for i in range(5):
            if len(player._coins[i]) < current_card._cost[i]:
                can_buy = False

        if can_buy:
            print("--------------------------")
            print(player._name)
            player.update_score(current_card._point)
            player._card.append(current_card)
            current_deck.remove(current_card)         

            for card in player._card :
                card.print_card()
            print('******************************')
            for card in current_deck:
                card.print_card()
            return current_card._tier
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

    def show(self) :
        pass

    def calculate_score(self) :
        pass

    def check_card_player_to_get_noble(self) :
        pass