#Kiera McMurtrie
#1/25/2018
#Computer Programming

def split_and_join():
    x = ('My name is Jose')
    xx = x.split()  #Splits x
    print(xx)
    
    y = ('user1;user2;user3')
    yy = y.split(';') #Splits and replaces ';' with blank spaces
    print(yy)
    
    z = ['this', 'is', 'a', 'sentence']
    zz = ' '
    zzz = zz.join(z) #Joins list w/ ' ' between each string
    print(zzz)


split_and_join()
