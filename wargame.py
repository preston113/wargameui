import random
import json
import time
def ranks():
    return ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

def suits():
    return  ["diamonds", "clubs", "spades", "hearts"]
class card:
    def __index__(self):
        return 1
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)

    def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
    def __gt__(self, other):
        if isinstance(other, card):
            if (self.rank == "Jack"):
                rank = 11
            elif (self.rank == "Queen"):
                rank = 12
            elif (self.rank == "King"):
                rank = 13
            elif (self.rank =="Ace"):
                rank = 1
            else: rank = self.rank

            if (other.rank == "Jack"):
                otherRank = 11
            elif (other.rank == "Queen"):
                otherRank = 12
            elif (other.rank == "King"):
                otherRank = 13
            elif (other.rank =="Ace"):
                otherRank = 1
            else: otherRank = other.rank
            return rank > otherRank
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, card):
            if (self.rank == "Jack"):
                rank = 11
            elif (self.rank == "Queen"):
                rank = 12
            elif (self.rank == "King"):
                rank = 13
            elif (self.rank =="Ace"):
                rank = 1
            else: rank = self.rank

            if (other.rank == "Jack"):
                otherRank = 11
            elif (other.rank == "Queen"):
                otherRank = 12
            elif (other.rank == "King"):
                otherRank = 13
            elif (other.rank =="Ace"):
                otherRank = 1
            else: otherRank = other.rank
            return self.rank == other.rank

    def __str__(self):
        return "rank: " + str(self.rank) + " suit: " + self.suit


        

class game:    
        def play_round(self, a_cards, b_cards):
            a_stash = []
            b_stash = []
            a_card = a_cards.pop()
            print("player a's card is:")
            print(a_card)
            b_card = b_cards.pop()
            print("player b's card is:")
            print(b_card)
            if a_card > b_card:
                print("a wins the round")
                return "a wins the round"
                a_stash.append(a_card) 
                a_stash.append(b_card) 
                a_cards = a_stash + a_cards
                a_stash.clear() 

            elif a_card == b_card:
                print("its a war")
                if len(a_cards) < 5:
                    print("b wins the game")
                    return "b wins the game"
                if len(b_cards) < 5:
                    print("a wins the game")
                    return "a wins the game" 
                a_stash.append(a_cards.pop())
                a_stash.append(a_cards.pop())
                a_stash.append(a_cards.pop())
                a_warcard = a_cards.pop()
                

                b_stash.append(b_cards.pop())
                b_stash.append(b_cards.pop())
                b_stash.append(b_cards.pop())
                b_warcard = b_cards.pop()
                print("a/'s warcard is ")
                print(a_warcard)
                print("b/'s warcard is ")
                print(b_warcard)
                if a_warcard > b_warcard:
                    print("a wins the war")
                    a_stash.append(a_warcard)
                    a_stash.append(b_warcard)
                    a_stash.append(a_card)
                    a_stash.append(b_card)
                    a_cards = a_stash + b_stash + a_cards
                    a_stash.clear()
                    b_stash.clear()
                    return "a wins the round"

                else:
                    print("b wins the war")
                    b_stash.append(a_warcard)
                    b_stash.append(b_warcard)
                    b_stash.append(a_card)
                    b_stash.append(b_card)
                    b_cards = b_stash + a_stash + b_cards
                    b_stash.clear()
                    a_stash.clear()
                    return "b wins the game"

            else:

                print("b wins the round")
                return "b wins the round"
                b_stash.append(a_card) 
                b_stash.append(b_card) 
                b_cards = b_stash + b_cards
                b_stash.clear()
        

        def play_war(self, deck):   
            card_count = 0
            a_stash = []
            b_stash = []
            a_cards = deck[:len(deck)//2]
            b_cards = deck[len(deck)//2:]
            while len(a_cards) and len(b_cards) >= 0:
               # time.sleep(1)
                print("player a has " + str(len(a_cards)) + " in their deck")
                print("player b has " + str(len(b_cards)) + " in their deck")
                if len(a_cards) == 0:
                    print("b wins the game")
                    return "b wins the game"
                    
                elif len(b_cards) == 0:
                    print("a wins the game")
                    return "a wins the game"
                else:
                    a_card = a_cards.pop()
                    print("player a's card is:")
                    print(a_card)
                    b_card = b_cards.pop()
                    print("player b's card is:")
                    print(b_card)
                    if a_card > b_card:
                        print("a wins the round")
                        a_stash.append(a_card) 
                        a_stash.append(b_card) 
                        a_cards = a_stash + a_cards
                        a_stash.clear() 

                    
                    elif a_card == b_card:
                        print("its a war")
                        if len(a_cards) < 5:
                            print("b wins the game")
                            return "b wins the game"
                        if len(b_cards) < 5:
                            print("a wins the game")
                            return "a wins the game" 
                        a_stash.append(a_cards.pop())
                        a_stash.append(a_cards.pop())
                        a_stash.append(a_cards.pop())
                        a_warcard = a_cards.pop()
                        

                        b_stash.append(b_cards.pop())
                        b_stash.append(b_cards.pop())
                        b_stash.append(b_cards.pop())
                        b_warcard = b_cards.pop()
                        print("a/'s warcard is ")
                        print(a_warcard)
                        print("b/'s warcard is ")
                        print(b_warcard)
                        if a_warcard > b_warcard:
                            print("a wins the war")
                            a_stash.append(a_warcard)
                            a_stash.append(b_warcard)
                            a_stash.append(a_card)
                            a_stash.append(b_card)
                            a_cards = a_stash + b_stash + a_cards
                            a_stash.clear()
                            b_stash.clear()
                        else:
                            print("b wins the war")
                            b_stash.append(a_warcard)
                            b_stash.append(b_warcard)
                            b_stash.append(a_card)
                            b_stash.append(b_card)
                            b_cards = b_stash + a_stash + b_cards
                            b_stash.clear()
                            a_stash.clear()



                    else:

                        print("b wins the round")
                        b_stash.append(a_card) 
                        b_stash.append(b_card) 
                        b_cards = b_stash + b_cards
                        b_stash.clear()
        
                
            
class deck:
    
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent=4)
    def __init__(self):
        self.deck = []
        for suit in suits():
            for rank in ranks():        
                self.deck.append(card(rank, suit))
        random.shuffle(self.deck) 
    def __repr__(self):
        json.dumps(self.__dict__)

    def getDeck(self):
        return self.deck
def obj_to_dict(obj):
    return obj.__dict__    
    
if __name__ == "__main__":
    deck = deck().getDeck()
    game = game()
    game.play_war(deck)






   
