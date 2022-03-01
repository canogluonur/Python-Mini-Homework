'''''
first_list=([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
flat_list = []

def flat(l):
    for i in l:
        if type(i)==list:
            first_list(i)
        else:
            flat_list.append(i)

print(flat_list)
'''''

first_list= [[1, 2], [3, 4], [5, 6, 7]]
bos = []

def ters(l):
    for i in l:
        if type(i)==list:
            bos.append(list(reversed(i)))
            
            
      
ters([[1, 2], [3, 4], [5, 6, 7]])
print(list(reversed(bos)))