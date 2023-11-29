

class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        return 1 <= self._value <= 9

    def get_row(self):
        if self._value in (1, 2, 3):
            return 0  # First row
        elif self._value in (4, 5, 6):
            return 1  # Second row
        else:
            return 2  # Third row

    def get_column(self):
        if self._value in (1, 4, 7):
            return 0  # First column
        elif self._value in (2, 5, 8):
            return 1  # Second column
        else:
            return 2  # Third column


# BOARD :
#        COL0 COL1 COL2
# ROW 0: | 1 |  2  | 3 |
# ROW 1: | 4 |  5  | 6 |
# ROW 2: | 7 |  8  | 9 |

# move = Move(3)

# print(move.value)
# print(move.get_column())
# print(move.get_row())
