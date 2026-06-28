class pattern():
    def pattern4(self,n):
        for i in range(n):
            for j in range(n,i,-1): #n-i+1
                print("*",end=" ")
            print()

p =pattern()
p.pattern4(5)