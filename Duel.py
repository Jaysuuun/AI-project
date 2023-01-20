import time

# Initialize the variables for the game, player and computer, their scores, and the attack and defense moves.
class DuelStart:
    def __init__(self):
        self.player = "Player"
        self.computer = "Computer"
        self.player_score = 0
        self.computer_score = 0
        self.attack = None
        self.defend = None
        self.turn = None

    # The minimax algorithm that the computer uses to determine its moves.
    def minimax(self, depth, is_maximizing):
        # Check if the computer is winning, if the game is a draw, or if it's a tie.
        if depth == 0:
            return self.is_winning(self.computer)
        if self.is_winning(self.computer) == 1:
            return 1
        if self.is_winning(self.player) == -1:
            return -1
        if self.is_draw():
            return 0
        

        best_value = None
        #the maximizer layer(computers turn)
        if is_maximizing:
            best_value = float('-inf')
            for move in ["slash", "thrust"]:
                self.attack = move
                value = self.minimax(depth - 1, False)
                best_value = max(best_value, value)
        #minimizer layer (players turn)
        else:
            best_value = float('inf')
            for move in ["block", "dodge"]:
                self.defend = move
                value = self.minimax(depth - 1, True)
                best_value = min(best_value, value)

        return best_value

    #Shows the score of the player and the computer.
    def show_scores(self):
        print("Player: ", self.player_score)
        print("Computer: ", self.computer_score)

    #Checks if the moves made by the player is valid.
    def check_moves(self, player, move, turn):
        valid_moves = ["slash", "thrust", "block", "dodge"]
        if turn == "attack":
            valid_moves = ["slash","thrust"]
        elif self.turn == "defend":
            valid_moves = ["block", "dodge"]
        if move not in valid_moves:
            print("Invalid move, please choose a valid move.")
            self.play()
        if move == "slash" or move == "thrust":
            self.attack = move
            print(player, "Chose", move, "to attack")
        elif move == "block" or move == "dodge":
            self.defend = move
            print(player, "Chose", move, "to defend")
    #Checks if the game results in a draw if player and computer has the same score.
    def is_draw(self):
        if self.player_score == self.computer_score:
            return True
        return False

    #Accpets the move when the player is attacking  and checks if it's valid or not.
    def attack_player(self):
        start_time = time.time()
        self.turn = "attack"
        move = input("Choose your attack (slash/thrust): ")
        if time.time() - start_time > 5:
            print("Player took too long to make a move, automatic loss.")
            self.computer_score += 1
            self.check_game_state()
            exit()
        self.check_moves(self.player, move, self.turn)
        if self.is_winning(self.player) == -1:
            self.player_score += 1
        
    #Accpets the move when the player is defending and checks if it's valid or not.
    def defend_player(self):
        start_time = time.time()
        self.turn = "defend"
        move = input("Choose your defense (block/dodge): ")
        if time.time() - start_time > 5:
            print("Player took too long to make a move, automatic loss.")
            self.computer_score += 1
            self.check_game_state()
            exit()

        self.check_moves(self.player, move, self.turn)
        if self.is_winning(self.player) == -1:
            self.player_score += 1

    #Checks the state of the game whether it is a draw, the player is winning or the computer is winning.
    def check_game_state(self):
        if self.is_draw():
            print(self.show_scores())
            print("It's a Draw! You Survived!")
            exit()

        if self.is_winning(self.player):
            print(self.show_scores())
            print("Player wins!")
            exit()

        if self.is_winning(self.computer):
            print(self.show_scores())
            print("Computer wins!")
            exit()
        
    # Check if the player or computer wins the round
    def is_winning(self, player):
        #If either of these conditions are true, it returns 1 indicating that the computer has won .
        if player == "Computer":
            if (self.attack == "slash" and self.defend == "dodge") or (self.attack == "thrust" and self.defend == "block"):
                return 1
        #If either of these conditions are true, it returns -1 indicating that the player has survived.
        elif player == "Player":
            if (self.attack == "slash" and self.defend == "block") or (self.attack == "thrust" and self.defend == "dodge"):
                return -1
        return 0


    
        
        
    #This function uses the minimax algorithm to determine the best move for the computer to attack. 
    def attack_computer(self):
        depth = 2
        best_attack = None
        best_value = float('-inf')
        for move in ["slash", "thrust"]:
            self.attack = move
            value = self.minimax(depth, False)
            if value > best_value:
                best_value = value
                best_attack = move
        self.attack = best_attack
        if self.is_winning(self.computer) == 1:
            self.computer_score += 1
        print("Computer chose", best_attack, "to attack")
        


    #This function also uses the minimax algorithm to determine the best move for the computer to defend. 
    def defend_computer(self):
        depth = 2
        best_defense = None
        best_value = float('inf')
        for move in ["block", "dodge"]:
            self.defend = move
            value = self.minimax(depth, True)
            if value < best_value:
                best_value = value
                best_defense = move
        self.defend = best_defense
        if self.is_winning(self.computer) == 1:
            self.computer_score += 1
        print("Computer chose", best_defense, "to defend")
    

    # The main function that starts the game, where the player and computer make their moves and the game state is checked and shows the final score when the game is over.
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
    game = DuelStart()
    game.play()



























