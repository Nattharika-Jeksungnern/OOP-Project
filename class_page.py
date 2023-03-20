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