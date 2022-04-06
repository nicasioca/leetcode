class TicTacToe(object):

    def __init__(self, n: int):
        self.__size = n
        self.__rows = [[0, 0] for _ in range(n)]
        self.__cols = [[0, 0] for _ in range(n)]
        self.__diagonal = [0, 0]
        self.__anti_diagonal = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        i = player - 1
        self.__rows[row][i] += 1
        self.__cols[col][i] += 1
        if row == col:
            self.__diagonal[i] += 1
        if col == len(self.__rows) - row - 1:
            self.__anti_diagonal[i] += 1
        if any(self.__rows[row][i] == self.__size,
               self.__cols[col][i] == self.__size,
               self.__diagonal[i] == self.__size,
               self.__anti_diagonal[i] == self.__size):
            return player

        return 0




# Example:
# Input:
# move(0, 0) // X turn
# move(1, 0) // O trun 
# move(1, 1) // X turn
# move(2, 0) // O turn
# move(2, 2) // X turn and win
# move(0, 0)  //throw GameEndException
# move(0, 0) // X turn
# move(0, 0) // throw AlreadyTakenException
# move(1, 0) // O turn
# move(1, 1) // X turn
# move(2, 0) // o turn
# move(2, 2) // X turn and win
# Output:
# x player wins!
# x player wins!
