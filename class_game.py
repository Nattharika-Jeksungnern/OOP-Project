
class FullDeck :
    def __init__(self, card, number) :
        self._card_collection = card #Aggragation with Card
        self._num_card = number

    def shuffle(self) :
        pass

class Card :
    def __init__(self, name, cost, point, status) :
        self.__name_card = name #"W311"
        self._cost_card = cost #[3,1,0,0,1]
        self._point_card = point #0
        self._status_card = status #"in_deck"

    def update_owner(player):
        pass
    

class Deck (FullDeck):
    def __init__(self,card, tier, number) :
        FullDeck.__init__(self, card, number)
        self.__tier = tier
        self._top_deck = card #Deck call Card
    
    def random_top_deck(self):
        pass

class DeckNoble :
    def __init__(self, noble, number) :
        self._noble_collection = noble #[] #Aggregation with Noble
        self._num_noble = number #3+1+1

class Noble :
    def __init__(self, name, condition, status, owner) :
        self.__name_noble = name #"Arm"
        self.condition_noble = condition #[]
        self.__status_noble = status #False
        self._owner = owner #"Premier" #Association with PLayer

    def update_owner(player):
        pass

class StackCoin :
    def __init__(self, num_coin) :
        self.__num_coin = num_coin # [7,7,7,7] #Aggregation with Coin

class Coin :
    def __init__(self, color) :
        self._color = color #"white"
        self.__value = 1

    def update_owner(player):
        pass

class GoldCoin :
    def __init__(self) :
        self._num_coin = 5

    def reserve(self) : 
        pass

class BoardRoom :
    def __init__(self, number, time, target, status, result, deck1, deck2, deck3, player, noble, coin, gold_coin) :
        self._num_player = number #2+1+1
        self._time = time #600
        self._target = target #15
        self._status_room = status #"playing"
        self._result = result #""
        self._deck_1 = deck1 #[]
        self._deck_2 = deck2 #[]
        self._deck_3 = deck3 #[]
        self._player = player #[]
        self._noble = noble #[]
        self._coin = coin #[]
        self._gold_coin = gold_coin #[]

    def show(self) :
        pass

    def calculate_score(self) :
        pass

    def check_card_player_to_get_noble(self) :
        pass