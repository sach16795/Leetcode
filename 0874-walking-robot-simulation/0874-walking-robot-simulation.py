class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curr_p = [0,0]
        ans = 0
        curr_d = 'n'
        obx = {}
        oby = {}
        
        for i in obstacles:
            if i[0] in obx:
                obx[i[0]].append(i[1])
            else:
                obx[i[0]] = [i[1]]
            
            if i[1] in oby:
                oby[i[1]].append(i[0])
            else:
                oby[i[1]] = [i[0]]

        disp = {'n' : [0,1],'s' : [0,-1],'e' : [1,0],'w' : [-1,0]}
        dirn = {'n' : ['w','e'],'s' : ['e','w'],'e' : ['n','s'],'w' : ['s','n']}
        
        for i in commands:
            if i < 0:
                curr_d = dirn[curr_d][i+2]
                continue
            while i > 0:
                next_step = disp[curr_d]
                next_step = [curr_p[0] + next_step[0], curr_p[1] + next_step[1]]
                
                if curr_d in ['e' , 'w']:
                    if next_step[0] in obx and next_step[1] in obx[next_step[0]]:
                        break
                else:
                    if next_step[1] in oby and next_step[0] in oby[next_step[1]]:
                        break
                curr_p = next_step
                i -=1
                ans = curr_p[0] **2 + curr_p[1] **2 if curr_p[0] **2 + curr_p[1] **2 > ans else ans
        return ans
                    