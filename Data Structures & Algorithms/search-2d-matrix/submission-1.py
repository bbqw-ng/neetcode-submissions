class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            #gives us the middle element every time with this formula
            middle = start + (end - start) // 2
            first = matrix[middle][0]
            last = matrix[middle][-1]
            if target >= first and target <= last:
                m = matrix[middle]
                m_start = 0
                m_end = len(m) - 1
                while m_start <= m_end:
                    m_middle = m_start + (m_end - m_start) // 2
                    if target == m[m_middle]:
                        return True
                    elif target < m[m_middle]:
                        m_end = m_middle - 1
                        print(m_end)
                    elif target > m[m_middle]:
                        m_start = m_middle + 1
                return False
            elif target < matrix[middle][0]:
                end = middle - 1
            elif target > matrix[middle][-1]:
                start = middle + 1
        return False 

