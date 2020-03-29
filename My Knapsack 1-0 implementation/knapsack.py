w = [1,3,4,5]
val= [1,4,5,7]

def knap(n, val, w ) :
    wid, hight = n+1, len(val)
    t = [[0 for x in range(wid)] for y in range(hight)]
    i = 0
    j = 1
    prev = 0
    new = 0
    print()
    while(i<hight):
        j=1
        while(j<wid):
            if  j < w[i]:
                    t[i][j] = t[i-1][j]
            else :
                prev = t[i-1][j]
                new = val[i]+t[i-1][j-w[i]]
                t[i][j] = max([new , prev])
            j+=1
        
        i+=1  
    return t

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
                j-=w[i]
    print(ans)

print(knap(7,val,w))
num(knap(7,val,w),w)
