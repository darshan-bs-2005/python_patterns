class pattern():
    def pattern8(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end=" ")
            #for star
            for j in range(2*i+1):
                print("*",end=" ")
            # for space
            for j  in range(n-i-1):
                print(" ",end=" ")
            print()
    def pattern9(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end=" ")
            for j in range(2*(n-i-1)+1): #2n-(2i+1)
                print("*",end= " ")
            for j in range(i):
                print(" ",end=" ")
            print()

p=pattern()
p.pattern8(5)
p.pattern9(5)