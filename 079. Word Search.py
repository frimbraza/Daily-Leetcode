# https://leetcode.com/problems/word-search/
# Medium

# Slow and memory intensive ... But it works!

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def in_bounds(coord, height, width):
            y = coord[0]
            x = coord[1]
            if y >= height or y < 0:
                return False
            if x >= width or x < 0:
                return False
            return True
        
        def make_coords(coord, height, width):
            y = coord[0]
            x = coord[1]
            
            coords = []
            for i in range(-1,2):
                if i == 0:
                    continue
                new_coord = (y + i, x)
                if in_bounds(new_coord, height, width):
                    coords.append(new_coord)
                new_coord = (y, x + i)
                if in_bounds(new_coord, height, width):
                    coords.append(new_coord)
            return coords
        
        height = len(board)
        width = len(board[0])
        
        all_coordinates = [(y,x) for y in range(height) for x in range(width)]
        
        stack = []
        for coordinate in all_coordinates:
            y = coordinate[0]
            x = coordinate[1]
            stack.append(([coordinate], board[y][x]))
        
        while stack:
            stack_item = stack.pop()
            
            item_path = stack_item[0]
            item_word = stack_item[1]
            cur_coord = item_path[-1]
            
            if item_word == word:
                return True
            
            if item_word in word[:len(item_word)]:
                # print(item_word)
                next_coords = make_coords(cur_coord, height, width)
                # print(next_coords)
                for coord in next_coords:
                    if coord not in item_path:
                        new_path = item_path + [coord]
                        new_word = item_word + board[coord[0]][coord[1]]
                        stack.append([new_path, new_word])
        
        return False
                
        