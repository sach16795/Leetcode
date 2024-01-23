class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr_dir = 'N'
        x=0
        y=0
        instructions = instructions*2
        dir_move = {'N':[0,1], 'S':[0,-1], 'E':[1,0], 'W': [-1,0]}
        dir_trans = {'N':['E','W'], 'S':['W','E'], 'E':['S','N'], 'W': ['N','S']}
        
        for move in instructions:
            if move == 'G':
                disp = dir_move[curr_dir]
                x += disp[0]
                y+= disp[1]
            elif move =='L':
                curr_dir = dir_trans[curr_dir][1]
            elif move =='R':
                curr_dir = dir_trans[curr_dir][0]
        return (x ==0 and y==0) or curr_dir !='N'
                