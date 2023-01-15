class FightingGame:
    def __init__(self):
        self.player = "Player"
        self.computer = "Computer"
        self.player_score = 1
        self.computer_score = 1
        self.attack = None
        self.defend = None

    def minimax(self, depth, is_maximizing):
        
        if self.is_winning(self.computer):
            return self.computer_score - depth
        if self.is_winning(self.player):
            return -self.player_score + depth
        if self.is_draw():
            return 0
            

        best_value = None
        if is_maximizing:
            best_value = float('-inf')
            for move in ["slash", "thrust"]:
                self.attack = move
                value = self.minimax(depth - 1, False)
                best_value = max(best_value, value)
        else:
            best_value = float('inf')
            for move in ["block", "dodge"]:
                self.defend = move
                value = self.minimax(depth - 1, True)
                best_value = min(best_value, value)

        return best_value

    def check_moves(self, player, move):
        if move == "slash" or move == "thrust":
            self.attack = move
            print(player, "Chose", move, "to attack")
        elif move == "block" or move == "dodge":
            self.defend = move
            print(player, "Chose", move, "to defend")
        else:
            print("Choose a move")
            self.play()

    def is_draw(self):
        if self.player_score == 0 and self.computer_score == 0:
            return True
        return False

    def attack_player(self):
        move = input("Choose your attack (slash/thrust): ")
        self.check_moves(self.player, move)
        
    def defend_player(self):
        move = input("Choose your defense (block/dodge): ")
        self.check_moves(self.player, move)
        
    def check_game_state(self):
        if self.is_draw():
            print("Draw!")
            exit()

        if self.is_winning(self.player):
            print("Player wins!")
            exit()

        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()
        
    
    def is_winning(self, player):
        if player == self.computer:
            if (self.attack == "slash" and self.defend == "block") or (self.attack == "thrust" and self.defend == "dodge"):
                return 1
            if self.computer_score >= 3:
                return 1
        elif player == self.player:
            if (self.attack == "slash" and self.defend == "dodge") or (self.attack == "thrust" and self.defend == "block"):
                return -1
            if self.player_score >= 3:
                return -1
        return 0

    
        
        

    def attack_computer(self):
        depth = 0
        best_attack = None
        best_value = float('-inf')
        for move in ["slash", "thrust"]:
            self.attack = move
            value = self.minimax(depth, False)
            if value > best_value:
                best_value = value
                best_attack = move
        self.attack = best_attack
        print("Computer chose", best_attack, "to attack")

    def defend_computer(self):
        depth = 0
        best_defense = None
        best_value = float('inf')
        for move in ["block", "dodge"]:
            self.defend = move
            value = self.minimax(depth, True)
            if value < best_value:
                best_value = value
                best_defense = move
        self.defend = best_defense
        print("Computer chose", best_defense, "to defend")

    def play(self):
        print("Duel Start...")
        print("\n")
        while True:
            self.attack_player()
            self.defend_computer()
            self.attack_computer()
            self.defend_player()
            self.check_game_state()


if __name__ == '__main__':
    game = FightingGame()
    game.play()
