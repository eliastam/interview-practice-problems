import math 
def rob(l):
    wid, hight = math.ceil(len(l)/2)+1, len(l)
    t = [[0 for x in range(wid)] for y in range(hight)]
    i=0
    j =1
  
    
    while(i < hight):
        j=1
        while(j<wid):
            if i ==0:
                t[i][j] = l[i]
                j+=1
                continue
            if  i == 1 :
                t[i][j] = max([l[0], l[1]])
                j+=1
                continue
            t[i][j] = max([ t[i-1][j] , t[i-2][j-1] + l[i] ])
            j+=1
        
        i+=1
    return(t)

def num(l,w):
    i = len(l)-1
    j = len(l[0])-1
    max_n = l[i][j]
    ans = []
    while i>=0 and j >= 0 :
        if i == 0 :
            if l[i][j] > 0 :
                ans.append(w[0])
                i-=1
            else :
                break
        else:
            if l[i][j] == l[i-1][j]:
                i-=1
            else:
                ans.append(w[i])
                i-=2
                j-=1
    print(ans)

l = [2,7,1,8]
num(rob(l),l)