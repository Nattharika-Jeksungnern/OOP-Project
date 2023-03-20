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