listA = ['a-b-c', 'd-e-f', 'g-h-i']

def convert(list1):
    listB=[]
    for each in list1:
        counter=0
        leach=list(each)
        while counter < len(leach):
            if leach[counter]=='e':
                leach[counter]='z'

            
            counter+=1
        listB.append(''.join(leach))
    return listB

print(convert(listA))
