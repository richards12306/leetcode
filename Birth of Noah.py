tree =  {'Adam':[0,930],'Seth':[1,912],'Enosh':[2,905],'Kenan':[3,910],\
    'Mahalalel':[4,895],'Jared':[5,962],'Enoch':[6,365],'Methuselah':[7,969],\
        'Lamech':[8,777],'Noah':[9,0],'Shem':[10,0],'Ham':[10,0],'Japheth':[10,0]}

while True:
    name1,name2=input().split( )
    if name1 in tree and name2 in tree:
        
        if tree[name1][0] < tree[name2][0]:
            print("Yes")
        else:
            print("No")

        if tree[name1][1]==0 or tree[name2][1]== 0:
            print("No enough information")
        elif tree[name1][1] > tree[name2][1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No enough information")
        print("No enough information")
    

    