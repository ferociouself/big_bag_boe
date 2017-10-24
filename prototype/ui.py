from board import Board

from settings import nothing

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
            player_input.append(spaceY+1)
            if highlight:
                print(board.highlight_row(spaceY))
            print ("Player " + (player_index + 1).__str__() + " chose row " + (spaceY + 1).__str__())
            spaceXStr = raw_input("Confirm row by entering a column, or enter \"n\" to enter a new column: ")
            if spaceXStr.isdigit():
                player_input.append(int(spaceXStr))
                spaceX = int(spaceXStr) - 1
                yConfirm = True
            if board.get_at_space(spaceX, spaceY) != nothing:
                print("That space is invalid. Please enter another space.")
                yConfirm = False



        game_over, board_full, winning_player = board.place_in_space((player_index+1).__str__(), spaceX, spaceY)
        if highlight:
            print
            print(board.highlight_col(spaceX))
        else:
            print
            print(board)
        if board_full:
            game_over = True
            if winning_player != None:
                print("Player " + (winning_player.get_index()+1).__str__() + " won!")
                print(winning_player.__str__())
                print(str(winning_player.get_rows()))
            else:
                print("There was a tie!")
            for player in board.get_player_list():
                print
                print("Player " + (player.get_index()+1).__str__())
                print("Score: " + player.get_points(board.get_point_dict()).__str__())
        elif winning_player != None:
            print("Player " + (winning_player.get_index()+1).__str__() + " won!")
            print(winning_player)
            print(winning_player.get_rows())
        #print(board)

        player_index = (player_index + 1) % players
