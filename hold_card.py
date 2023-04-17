from class_game import *
from class_page import *
from class_user import *
import json

f = open('data.json')


if __name__ == "__main__":
    print("Want to create room Y/N")
    a = input()
    
    if a == 'Y':
        print("number of player (2-4)")
        num_player = int(input())
        time = 0
        target = 15
        status = 'creating'
        result = ''
   
        #init gold coins
        gold_coin = GoldCoin()
        #init coins
        stack_coin = StackCoin()
        for i in range(len(color_coin)):
            if num_player == 2:
                num = 5
            elif num_player == 3:
                num = 6
            else :
                num = 8
            temp = []
            for j in range(num):
                temp.append(Coin(color_coin[i]))
            stack_coin._coins.append(temp)

        
        #init card
        full_deck = FullDeck([],90)
        data = json.load(f)
        for card in data['all_card_details']:
            full_deck._card_collection.append(Card(card["name"], card["cost"], card["point"], card["tier"], card["value"]))

        f.close()

        deck_tier_1 = Deck([], 1, 40)
        full_deck.tier_1(deck_tier_1._card_collection)
        deck_tier_2 = Deck([], 2, 30)
        full_deck.tier_2(deck_tier_2._card_collection)
        deck_tier_3 = Deck([], 3, 20)
        full_deck.tier_3(deck_tier_3._card_collection)

        deck_tier_1.shuffle_deck()
        deck_tier_2.shuffle_deck()
        deck_tier_3.shuffle_deck()

        room = BoardRoom(num_player, target, status, result, deck_tier_1._top_deck, deck_tier_2._top_deck, deck_tier_3._top_deck, [], ["noble"], stack_coin, gold_coin)  
        
        player_1 = Player('Guy', 'rainbow', 'kitsadoi', 'online', 'god', 0, 0, 0, [], [], [], [], [], [], 0, [], [], [[],[],[],[],[]], [], [])
        room._player.append(player_1)
        player_2 = Player('Yug'*10, 'rainbow', 'kitsaguy', 'online', 'god', 0, 0, 0, [], [], [], [], [], [], 0, [], [], [[],[],[],[],[]], [], [])
        room._player.append(player_2)
        player_3 = Player('Ugy', 'rainbow', 'saguykit', 'online', 'god', 0, 0, 0, [], [], [], [], [], [], 0, [], [], [[],[],[],[],[]], [], [])
        room._player.append(player_3)
        player_4 = Player('Uyg', 'rainbow', 'guysakit', 'online', 'god', 0, 0, 0, [], [], [], [], [], [], 0, [], [], [[],[],[],[],[]], [], [])
        room._player.append(player_4)
                
        print("Ready to play Y/N")
        b = input()

        remaining_player = 0
        if b == 'Y':
            play = True
            while play:
                #check
                room.get_last_turn(room._player[room._flag])
                room.last_player(room._player[room._flag])
                print(room._last_turn)
                if room._last_turn:
                    play = False
                print(room._player[room._flag]._name)
                print('socre : ', end='')
                print(room._player[room._flag]._score_player)
                print("discount_coin : ", end='')
                print(room._player[room._flag].discount_coin())
                print("hold card : ")
                print(room._player[room._flag].print_hold_card())
                print("gold coin : ",end='')
                print(room._player[room._flag]._gold_coins)
                print("player's coin : ")
                room._player[room._flag].print_coin()
                print("Choose action")
                print("1. pick coin : 1 ")
                print("2. buy card : 2")
                print("3. hold card : 3")
                print("4. buy hold card : 4 ")
                print("Exit : 0")
                c = int(input())
                if c == 0:
                    play = False
                if c == 1: # เหลือ return coin
                    room._coin.check_coin()
                    d = input()
                    e = d.split()
                    #print(e)
                    get_coin = stack_coin.pick_coin(e)
                    stack_coin.check_coin()
                    if get_coin != False:
                        room._player[room._flag].update_coin(get_coin)
                        room._player[room._flag].print_coin()
                        while room._player[room._flag].too_much_coin():
                            print("Please return coins")
                            room._player[room._flag].print_coin()
                            print("gold coin : ",end='')
                            print(room._player[room._flag]._gold_coins)
                            temp = input()
                            room.return_coins(temp, room._player[room._flag])
                        room.update_flag()
        
                    print('-------------------------------')
                if c == 2: #player จ่ายเหรียญ(ทำแล้ว), --> เพิ่มคะแนน(ทำแล้ว), เพิ่มเหรียญถาวร(ทำแล้ว)
                    # show card
                    room.show_card()
                    print("Enter name Card : ", end='')
                    c = input()
                    print("Want to buy Y/N")
                    a = input()
                    if a == 'Y':
                        can_buy = room.buy_card(room._player[room._flag],c)
                        if can_buy != False:
                            if can_buy == 1:
                                deck_tier_1.random_top_deck()
                                room.update_top_deck(deck_tier_1._top_deck, can_buy)
                            elif can_buy == 2:
                                deck_tier_2.random_top_deck()
                                room.update_top_deck(deck_tier_2._top_deck, can_buy)
                            elif can_buy == 3:
                                deck_tier_3.random_top_deck()
                                room.update_top_deck(deck_tier_3._top_deck, can_buy)
                            room.update_flag()

                if c == 3: #จองทำเสร็จแล้ว 
                    room.show_card()
                    print("Enter name Card : ", end='')
                    c = input()
                    print("Want to hold this card Y/N")
                    a = input()
                    if a == 'Y':
                        if room._player[room._flag].can_hold():
                            print("can hold this card")
                            can_hold = room.hold_card(room._player[room._flag],c)
                            if can_hold == 1:
                                deck_tier_1.random_top_deck()
                                room.update_top_deck(deck_tier_1._top_deck, can_hold)
                            elif can_hold == 2:
                                deck_tier_2.random_top_deck()
                                room.update_top_deck(deck_tier_2._top_deck, can_hold)
                            elif can_hold == 3:
                                deck_tier_3.random_top_deck()
                                room.update_top_deck(deck_tier_3._top_deck, can_hold)
                            print(room._gold_coin.print_gold_coin())
                            room.update_flag()   
                        else :
                            print("can't hold card (3/3)")
                
                if c == 4:
                    print("hold card : ")
                    print(room._player[room._flag].print_hold_card())
                    print("Enter name Card : ", end='')
                    c = input()
                    print("Want to buy Y/N")
                    a = input()
                    if a == 'Y':
                        can_buy = room.buy_hold_card(room._player[room._flag],c)
                        if can_buy != False:
                            room.update_flag()
            print(room.win())
                            
      
                    
                            
                            



                    
                    
