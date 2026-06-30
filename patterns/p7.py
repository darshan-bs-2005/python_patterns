class pattern():
    def pattern7(self,n):
        for i in range(n): 
            #for space
            for j in range(n-i-1):
                print(" ",end=" ")
            #for star
            for j in range(2*i+1):
                print("*",end=" ")
            # for space
            for j  in range(n-i-1):
                print(" ",end=" ")
            print()

p =pattern()
p.pattern7(5)