class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                seen_numbers = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        element = board[row][col]
                        if element in seen_numbers:
                            return False
                        elif element != ".":
                            seen_numbers.append(element)

        for i in range(9):
            seen_numbers = []
            for element in board[i]:
                if element in seen_numbers:
                    return False
                elif element != ".":
                    seen_numbers.append(element)

        for i in range(9):
            seen_numbers = []
            for j in range(9):
                element = board[j][i]
                if element in seen_numbers:
                    return False
                elif element != ".":
                    seen_numbers.append(element)

        return True
