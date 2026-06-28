class pattern():
    def pattern6(self,n):
        for i in range(1,n+1): #n
            for j in range(1,n-i+2): #1,n-i+1
                print(j,end=" ")
            print()

p =pattern()
p.pattern6(5)