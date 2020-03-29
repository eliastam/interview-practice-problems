
def most_reserved(l):
    key = ""
    rep= 0
    my_dict={}
    for i in l:
        if i[0] == '+' :
            w= i[1:len(l)]
            if w in my_dict:
                val = my_dict.get(w) +1
                my_dict[w] = val
            else:
                  my_dict[w] = 1
        if my_dict.get(w) > rep :
            rep = my_dict.get(w)
            key = w
           
        elif my_dict.get(w) == rep :
            
            c1 = key[0]
            c2 = w[0]
            if c2 < c1  : 
                key = w
            elif c2 == c1 :
                a1 = key[1]
                a2 = w[1]
                if a2 < a1  : 
                    key = w

    print(key)

A = ["+5A", "+3E", "-5A","-3E", "+3E", "+4F", "+5A", "-3E"]
most_reserved(A)