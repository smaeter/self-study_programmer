class  Card:
    suits = ["spades","hearts","dianmonds","clubs"]

    values = [None,None,
              "2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

    def __init__(self,v,s):
        self.value = v
        self.suit = s

    def __it__(self,c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            return self.suit < c2.suit

        return Flase

    def __gt__(self,c2):
        if self.value > c2.value:
            return True

        if self.value == c2.value:
            return self.suit > c2.suit
        
        return False

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        """card.values[]分繰り返す"""
        for i in range(2,15):
            """card.suit[]分繰り返す"""
            for j in range(4):
                self.cards.append(Card(i,j))
                
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) != 0:
            return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前：")
        name2 = input("プレーヤー2の名前：")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()

    def print_winners(self,winners):
        print("このラウンドは {} が勝ちました。".format(winners))

    def draw(self,p1,p2):
        print(" {} は「{}」、 {} は「{}」を引きました。".format(p1.name,p1.card,p2.name,p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます。")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay："
            responce = input(m)
            if responce == "q":
                print("q が押されました。終了します。")
                break
            self.p1.card = self.deck.rm_card()
            self.p2.card = self.deck.rm_card()
            self.draw(self.p1,self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winners(self.p1.name)
            else:
                self.p2.wins += 1
                self.print_winners(self.p2.name)

        win = self.winner(self.p1,self.p2)
        print("ゲーム終了、{} の勝ちです！".format(win))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        else:
            return p2.name
        return "引き分け"

game = Game()
game.play_game()
