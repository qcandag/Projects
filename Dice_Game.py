import random

def ran_dice(X):
    
    if X == 1:
        D = random.randint(1, 6)
        return D
    elif X == 2:
        D1 = random.randint(1, 6)
        D2 = random.randint(1, 6)
        return [D1,D2]
    
    else:
        print("")
        
        
def get_yn():
    
    Q = input("Do you want to throw again ? :")
    
    
    if Q[0] == "y".upper():
        
        return 1
    elif Q[0] == "n".upper():
        return 0
    else:
        print("")
        
        
        
def mainpy():
    
    C = 100
    print("Welcome user, you have 100 credits.")
    while (C != 0):
        Q1 = int(input("How much do you want to gamble?:"))
    
        if Q1 > C :
            print("You need to give a positive integer no more than your credit.")
            
        else:
            
            User_Dice = ran_dice(2)
            
            if User_Dice[0] < User_Dice[1]:
                K = User_Dice[0] 
                B = User_Dice[1]
                
            elif User_Dice[1] < User_Dice[0]:
                K = User_Dice[1]
                B = User_Dice[0]
                
            else:
                print("Error3 !!!")
                
            Total_Dice = sum(User_Dice)
            print("You throw {} , {}. Your total is {}".format(User_Dice[0],User_Dice[1]),User_Dice[0+1])
                
            if Total_Dice <= 6:
                Q2 = get_yn()
                if Q2 ==1:
                    Total_Dice += ran_dice(1)
                    
                else:
                    C = 0
                    
            elif Total_Dice == 7:
                Q3 = get_yn()
                
                if Q3 == 1:
                    K = ran_dice(1)
                    
                else:
                    C = 0
                    
            elif User_Dice[0] == User_Dice[1]:
                C -= Q1
                print("You Lose")
             
                
            #  PC İçin
            PC_Dice = ran_dice(2)
            
            if PC_Dice[0] < PC_Dice[1]:
                
                PK = PC_Dice[0]
                PB = PC_Dice[1]
                
            elif PC_Dice[1] < PC_Dice[0]:
                PK = PC_Dice[1]
                PB = PC_Dice[0]
                
            else:
                print("Error4 !!!")
                
            print("Computer throws {} , {}. ".format(User_Dice[0],User_Dice[1]))

                    
            Total_PC = sum(PC_Dice)
            print("PC {}  , {}".format(PC_Dice[0],PC_Dice[1]))
  
            if Total_PC <= 6:
                Total_PC += ran_dice(1)
                
            elif Total_PC == 7:
                PK = ran_dice(1)
                
            elif PC_Dice[0] == PC_Dice[1]:
                
                C += Q1
                print("You Win")
                
            print("PC {}  , {}".format(PC_Dice[0],PC_Dice[1]))

                
    
        if Total_Dice > Total_PC:
            C += Q1

            print("Kredidiniz : {}".format(C))
            print("You Win")
        
        elif Total_Dice < Total_PC:
            C -= Q1

            print("Krediniz : {}".format(C))
            print("You Lose")
        
        else:
             print("Krediniz : {}".format(C))
             print("Berabere")
        
        
    
mainpy()
        
           
                   
                   
        
                       
                   
               
           
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    