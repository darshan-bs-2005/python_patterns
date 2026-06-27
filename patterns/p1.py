class pattern:
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

p = pattern()
p.pattern1(5)