from board import Board

if __name__ == "__main__":
    players = input("How many players are playing? ")

    board = Board(players+1, players+1)

    print(board)

    player_index = 0
    game_over = False

    while not game_over:
        yConfirm = False

        spaceX = 0
        spaceY = 0

        while not yConfirm:
            spaceY = input("Which row would player " + (player_index + 1).__str__() + " like to choose: ") - 1
            print(board.highlight_row(spaceY))
            print ("Player " + (player_index + 1).__str__() + " chose row " + (spaceY + 1).__str__())
            spaceXStr = raw_input("Confirm row by entering a column, or enter \"n\" to enter a new column: ")
            if spaceXStr.isdigit():
                spaceX = int(spaceXStr) - 1
                yConfirm = True



        winning_player = board.place_in_space((player_index+1).__str__(), spaceX, spaceY)
        print(board.highlight_col(spaceX))
        if winning_player != None:
            game_over = True
            print("Player " + winning_player.get_index().__str__() + " won!")
            print(winning_player)
            print(winning_player.get_rows())
        #print(board)

        player_index = (player_index + 1) % players
