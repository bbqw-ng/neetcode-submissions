class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_nums = set()
            # print("current working row: ", row)
            for num in row:
                # print("current selected num: ", num)
                if num != "." and num in row_nums:
                    # print(f"duplicate num found: {num}")
                    return False
                elif num != ".":
                    # print(f"{num} added to set")
                    row_nums.add(num)

        for row in range(len(board)):
            col_nums = set()
            # print("current working row ", row)
            for col in range(len(board)):
                # print("current selected num ", board[col][row])
                num = board[col][row]
                if num != "." and num in col_nums:
                    return False
                elif num != ".":
                    # print(f"{num} added to set")
                    col_nums.add(num)
        
        hashmap = {}
        for row in range(len(board)):
            print("current working row ", row)
            for col in range((len(board))):
                print("current working col ", col)
                row_id = row//3
                col_id = col//3
                print("quadrant: ", row_id,col_id)
                #creates hashmap entry if it doesnt exist
                hashmap.setdefault((row_id,col_id), set())
                print(hashmap)
                num = board[row][col]
                print("current selected number", num)
                if num != "." and num in hashmap[(row_id,col_id)]:
                    return False
                elif num != ".":
                    print("number added to set: ", num)
                    hashmap[(row_id,col_id)].add(num)
        
        return True


        
        
