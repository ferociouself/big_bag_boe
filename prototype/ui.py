from board import Board

highlight = True

player_input = []

if __name__ == "__main__":
    players = input("How many players are playing? ")
    player_input.append(players)

    board = Board(players+1, players+1)

    print(board)

    print(board.get_point_dict())

    player_index = 0
    game_over = False

    while not game_over:
        yConfirm = False

        spaceX = 0
        spaceY = 0

        while not yConfirm:
            spaceY = input("Which row would player " + (player_index + 1).__str__() + " like to choose: ") - 1
            player_input.append(spaceY)
            if highlight:
                print(board.highlight_row(spaceY))
            print ("Player " + (player_index + 1).__str__() + " chose row " + (spaceY + 1).__str__())
            spaceXStr = raw_input("Confirm row by entering a column, or enter \"n\" to enter a new column: ")
            if spaceXStr.isdigit():
                spaceX = int(spaceXStr) - 1
                player_input.append(spaceX)
                yConfirm = True



        game_over, board_full, winning_player = board.place_in_space((player_index+1).__str__(), spaceX, spaceY)
        if highlight:
            print(board.highlight_col(spaceX))
        else:
            print(board)
        if board_full:
            game_over = True
            print("Player " + winning_player.get_index().__str__() + " won!")
            print(winning_player)
            print(winning_player.get_rows())
            for player in board.get_player_list():
                print("Player " + player.get_index().__str__())
                print("Score: " + player.get_points(board.get_point_dict()).__str__())
        elif winning_player != None:
            print("Player " + winning_player.get_index().__str__() + " won!")
            print(winning_player)
            print(winning_player.get_rows())
        #print(board)

        player_index = (player_index + 1) % players

    for inp in player_input:
        print(inp)
