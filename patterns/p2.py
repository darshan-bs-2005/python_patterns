class pattern():
    def pattern2(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end=' ')
            print()

p =pattern()
p.pattern2(5)