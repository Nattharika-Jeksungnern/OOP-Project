class System :
    def __init__(self, system) :
        self._system = system #temp variable

    def sort_ranking():
        pass
    def create_board_room(num_player):
        pass
    def join_board_room(boardroom):
        pass
    def view_ranking():
        pass
class Person :
    def __init__(self, name, color, account, status) :
        self.__name = name #"guy"
        self._color_name = color #"rainbow"
        self._account = account
        self.__status = status #"offline"

    def log_in(self):
        pass
    
    def sign_up(self):
        pass

class User(Person) :
    def __init__(self, name, color, account, status, elo, step, member_type, member_since, all_game_2p, win_game_2p, all_game_3p, win_game_3p, all_game_4p, win_game_4p) :
        Person.__init__(self, name, color, account, status)
        self._elo_player = elo
        self._profile_step = step
        self._profile_member_type = member_type
        self._profile_member_since = member_since
        self.__stats_all_game_2p = all_game_2p
        self.__stats_win_game_2p = win_game_2p
        self.__stats_all_game_3p = all_game_3p
        self.__stats_win_game_3p = win_game_3p
        self.__stats_all_game_4p = all_game_4p
        self.__stats_win_game_4p = win_game_4p

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
    def view_game_page():
        pass
    def ready_play(user):
        pass
    def create_reply(owner):
        pass
    def report_user(person):
        pass
    def view_ranking():
        pass
    def view_player_profile(person):
        pass
    def view_player_static(peraon):
        pass
    def delete_forum(topic):
        pass
    def delete_comment(comment):
        pass
    def like_forum(forum):
        pass
    def ike_comment(comment):
        pass
    def view_forum():
        pass
    def view_comment(owner,describe):
        pass
    def view_reply(onwer,describe):
        pass
    def view_forum_page():
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
        self._role = role #"admin"   

    def ban_user():
        pass
    def view_forum_page():
        pass
    def view_forum():
        pass
    def create_forum(owner):
        pass
    def delete_forum(topic):
        pass
    def create_reply(owner):
        pass
    def delete_comment(comment):
        pass
    def view_ranking():
        pass
    def view_player_profile(person):
        pass
    def view_player_static(person):
        pass
    def view_game_page():
        pass

#player inherit Person
class Player(User) :
    def __init__(self, name, color, account, status, elo, static, time, score, card, hold_card, coins, gold_coin, noble) :
        User.__init__(self, name, color, account, status, elo, static)
        self._time_player = time
        self._score_player = score
        self._card = card
        self._hold_card = hold_card
        self._coins = coins
        self._gold_coin = gold_coin
        self._noble =  noble

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
    def resign_game(person):
        pass
    def back_game(person):
        pass

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

class GamePage :
    def __init__(self, room, create) :
        self._list_room = room #[] #Keep BoardRoom
        self._create_room = create #0

    #function  เข้า forumpage

class ForumPage :
    def __init__(self) :
        self._list_forum = []
        self._create_forum = True
    
    #function  เข้า forumpage

class Forum :
    def __init__(self, title, content, num_like, num_dislike, date, confirm, cancel, owner, comment) :
        self._title_forum = title #"Rule"
        self._content_forum = content #"ba ba ba ba ba bana na"
        self._likes_forum = num_like #999
        self._dislike_forum = num_dislike #-999
        self.__date_forum = date #[10,2,2023]
        self._confirm_forum = confirm #True
        self._cancel_forum = cancel #False
        self._owner_forum = owner #"ngerrrrrrrrrrrrr" #Association with User
        self._comment = comment #[] #Aggregation with Class Comment

    def create_forum(describe):
        pass
    def create_comment(describe):
        pass

class Comment :
    def __init__(self,content, date, confirm, cancel, owner, reply, num_like) :
        self._content_comment = content #"comment"
        self.__date_comment = date #[10,2,2023]
        self._confirm_comment = confirm #True
        self._cancel_comment = cancel #False
        self._owner_comment = owner #"ngerrrrrrrrrrrrrr" #Association with User
        self.__like_comment = num_like
        self._reply = reply #[] #Aggregation with Class Reply
    
    def create_reply(describe):
        pass

class Reply : #Reply 1 level 
    def __init__(self, content, date, confirm, cancel, owner, host) :
        self._content_reply = content#"reply"
        self.__date_reply = date #[10,2,2023]
        self._confirm_reply = confirm #True
        self._cancel_reply = cancel #False
        self._owner_reply = owner #"" #user reply ใคร reply
        self._host_comment = host #"" #user reply comment ของใคร

