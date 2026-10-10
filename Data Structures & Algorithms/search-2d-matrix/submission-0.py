class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_count = len(matrix)
        cols_count = len(matrix[0])
        l_outer, r_outer = 0, rows_count - 1

        while l_outer <= r_outer:
            if target > matrix[r_outer][-1] or target < matrix[l_outer][0]:
                return False
            m = (l_outer + r_outer) // 2
            if target < matrix[m][0]:
                r_outer = m - 1
            elif target > matrix[m][-1]:
                l_outer = m + 1
            else:
                l_inner, r_inner = 0, cols_count - 1
                while l_inner <= r_inner:
                    if target > matrix[m][r_inner] or target < matrix[m][l_inner]:
                        return False
                    m_inner = (l_inner + r_inner) // 2
                    if target > matrix[m][m_inner]:
                        l_inner += 1
                    elif target < matrix[m][m_inner]:
                        r_inner -= 1
                    else:
                        return True
