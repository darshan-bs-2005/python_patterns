class pattern():
    def pattern8(self,n):
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