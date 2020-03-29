import queue

def change(current, change):
    output = ""
    stack_current = [] 

    x = current.split("/")
    
  
    y = change.split("/")
   
    for i in x :
        if i != '' :
            stack_current.append(i)
    pop = 0
    point =0
    for  k in y :
        
        if k == ".." :
            if   stack_current :
                stack_current.pop()
            pop += 1
        elif( k == ".") :
            point +=1

    while pop > 0 : 

        y.remove("..")
        pop -=1
    while point > 0 : 

        y.remove(".")
        point -=1
       
            


    output = "/"
    for j in stack_current: 
        output +=j + "/"
  
    for k in y: 
        output +=k + "/"
    if(len(output)) == 1:
        print(output)
    else:
        print(output[0:len(output)-1])
    

change("/facebook/anin/elias/ee/aa/ss", "../../.././../ff/./a/.")
    