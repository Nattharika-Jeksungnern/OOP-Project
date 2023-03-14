class Person :
    def __init__(self) :
        self.__name = "guy"
        self._color_name = "rainbow"
        self._account = Account
        self.__status = "offline"

    def log_in(self):
        pass
    
    def sign_up(self):
        pass

class User :
    def __init__(self) :
        elo_player = 99999
        static = Statistic

    def check_step(self) :
        pass

    def create_board_room(self) :
        pass

    def join_board_room(self) :
        pass

    def create_forum(self) :
        pass

    def comment_forum(self) :
        pass

class Account :
    def __init__(self, email, password, forgot_password) :
        self.__email_account = email #"65010037@kmitl.ac.th"
        self.__passwerd_account = password #"********"
        self._forgot_password = forgot_password #False

    def reset_password(self) :
        pass

# Admin inherit Account
class Admin (Account): 
    def __init__(self, email, password, forgot_password, role) :
        Account.__init__(self, email, password, forgot_password)        
        self._role = role #"addmin"   

class Profile :
    def __init__(self) :
        self._step_player = "super ultra hyper very nice great number one king granmaster"
        self._member_type = "god"
        self._member_since = "tomorrow"
        self._status_person = "death"

class Statistic :
    def __init__(self) :
        self.__all_game_2p = 999
        self.__win_game_2p = 999
        self.__all_game_3p = 999
        self.__win_game_3p = 999
        self.__all_game_4p = 999
        self.__win_game_4p = 999

    def plus(self) :
        pass

    def plot_graph(self) :
        pass

    def cal_win_rate_2p(self) :
        pass

    def cal_win_rate_3p(self) :
        pass

    def cal_win_rate_4p(self) :
        pass

#player inherit Person
class Player(User) :
    def __init__(self) :
        self._time_player = 600
        self._score_player = 0
        self.hand = """Hand"""

    def winner(self) :
        pass

    def hold_card(self) :
        pass

    def buy_card(self) :
        pass

    def pick_coin(self) :
        pass

    def return_coin(self) :
        pass

class Hand :
    def __init__(self) :
        card = Card
        hold_card = Card
        coin = Coin
        gold_coin = GoldCoin
        noble = Noble

class FullDeck :
    def __init__(self) :
        self._card_collection = []
        self._num_card = 20+30+40

    def shuffle(self) :
        pass

class Card :
    def __init__(self) :
        self.__name_card = "W311"
        self._cost_card = [3,1,0,0,1]
        self._point_card = 0
        self._status_card = "in_deck"

# Deck1 inherit Full Deck
class Deck1 (FullDeck):
    def __init__(self,card) :
        self.__tier = 1
        self._top_deck = card
    
    def random_top_deck(self):
        pass
        
# Deck2 inherit Full Deck
class Deck2 (FullDeck):
    def __init__(self,card) :
        self.__tier = 2
        self._top_deck = card
        
    def random_top_deck(self):
        pass

# Deck3 inherit Full Deck
class Deck3 (FullDeck):
    def __init__(self,card) :
        self.__tier = 3
        self._top_deck = card

    def random_top_deck(self):
        pass

class DeckNoble :
    def __init__(self) :
        self._noble_collection = []
        self._num_noble = 3+1+1

class Noble :
    def __init__(self) :
        self.__name_noble = "Arm"
        self.condition_noble : list
        self.__status_noble = False

class StackCoin :
    def __init__(self) :
        self.__num_coin = [7,7,7,7]

class Coin :
    def __init__(self) :
        self._color = "white"
        self.__value = 1

class GoldCoin :
    def __init__(self) :
        self._num_coin = 5

    def reserve(self) : 
        pass

class BoardRoom :
    def __init__(self) :
        self.num_player = 2+1+1
        self.time = 600
        self.target = 15
        self.status_room = "playing"

    def show(self) :
        pass

    def calculate_score(self) :
        pass

    def check_card_player_to_get_noble(self) :
        pass

class GamePage :
    def __init__(self) :
        self._list_room = []
        self._create_room = 0

class ForumPage :
    def __init__(self) :
        self._list_forum = []
        self._create_forum = True

class CreateForum :
    def __init__(self) :
        self._title_forum = "Rule"
        self._content_forum = "ba ba ba ba ba bana na"
        self._likes_forum = 999
        self._dislike_forum = -999
        self._date_forum = [10,2,2023]
        self._confirm_forum = True
        self._cancel_forum = False
        self._owner_forum = "ngerrrrrrrrrrrrr"

class Comment :
    def __init__(self) :
        self._content_comment = "comment"
        self._date_comment = [10,2,2023]
        self._confirm_comment = True
        self._cancel_comment = False
        self._owner_comment = "ngerrrrrrrrrrrrrr"

class Reply :
    def __init__(self) :
        self._content_reply = "reply"
        self._date_reply = [10,2,2023]
        self._confirm_reply = True
        self._cancel_reply = False
        self._ower_reply = "??"
        self._host_reply = "??"
