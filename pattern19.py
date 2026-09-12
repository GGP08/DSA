def pattern19(n):
    iniS = 0
    for i in range(n):

        #stars
        for j in range(1, n-i+1):
            print("*", end = " ")

        #spaces
        for j in range(iniS):
            print(" ", end = " ")

        #stars
        for j in range(1, n-i+1):
            print("*", end = " ")

        iniS += 2
        print()

    iniS = 2*n-2
    for i in range(1, n+1):
            #stars
            for j in range(1, i+1):
                print("*", end = " ")
    
            #spaces
            for j in range(iniS):
                print(" ", end = " ")
    
            #stars
            for j in range(1, i+1):
                print("*", end = " ")
    
            iniS -= 2
            print()


    

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern19(n)
