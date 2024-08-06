num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()
    
'''
TELEPHONE NUMBER PAD USING 2D TUPLE
#O/P

1 2 3 
4 5 6
7 8 9
* 0 #

'''