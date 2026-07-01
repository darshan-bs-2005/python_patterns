class pattern:
    def pattern10(self,n):
        for i in range(1,2*n):
            star = i

            if i>n:
                star=2*n-i
          
            for j in range(star):
                 print("*", end="")
            print()
p=pattern()
p.pattern10(5)