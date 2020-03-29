def half_sum (list):
    sum = 0 
    for i in list:
        sum += i
    sum = int(sum/2)
    return sum


def knap(l) :
    wid, hight = len(l) + 1, len(l)
    t = [[0 for x in range(wid)] for y in range(hight)]
    i = 0
    j = 1
    prev = 0
    new = 0
    print()
    while(i<hight):
        j=1
        while(j<wid):
            if i == 0 :
                t[i][j] = l[i] 
            else:
                value = min([abs(half_sum(l)- l[i]), abs(half_sum(l)- t[i][j-1])])
                if value == abs(half_sum(l)- l[i]):
                  t[i][j] = l[i] 
                else :
                      t[i][j] = t[i][j-1] 

                k = i-1
                while k>=0 :
                  
                    y = abs(half_sum(l) - l[i] - t[k][j-1])
                 
                    if y < value :
                        if l[i]+t[k][j-1] <= half_sum(l):
                            t[i][j] = l[i]+t[k][j-1] 
                            value = y
                    t[i][j] = max( [t[i][j], t[i-1][j]])

                    k-=1
            j+=1
        i+=1  
    return t
def get(t, l):
    j = len(t[0])-1
    i = len (t) -1
    
    ans = []
    while i>0 and j >0:
        if t[i][j] == t[i][j-1] :
            j -=1
        elif t[i][j] == t[i-1][j] :
            i -=1
        else:
            ans.append(l[i])
            l.remove(l[i])
            i-=1
            j-=1
    print(str(ans) + " sum = " + str(sum(ans)))
    print(str(l) + " sum = " + str(sum(l)))



#test 
l = [2,4,5,7,9,15]
get(knap(l), l)
