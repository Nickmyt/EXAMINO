
import random


table = [0,1,2,3,4,5,6,7,8]


# τυπωνουμε τον πινακα
def show(table) :
    print (table[0], "|", table[1], "|", table[2])
    print ("-----------")
    print (table[3], "|", table[4], "|", table[5])
    print ("-----------")
    print (table[6], "|", table[7], "|", table[8])
    
    
#  Συνάρτηση που ελέγχει ποιος νίκησε σε κάθε παρτίδα     
def check() :
    if table[0]==table[3] and table[3]==table[6]:
        print ("BAMBOOZLE!")
        check=False
        
    elif table[1]==table[4] and table[4]==table[7]:
        print ("BAMBOOZLE!")
        check=False
        
    elif table[2]==table[5] and table[5]==table[8]:
        print("BAMBOOZLE!")
        check=False
    
    elif table[0]==table[1] and table[1]==table[2]:
        print ("BAMBOOZLE!")
        check=False
    
    elif table[3]==table[4] and table[4]==table[5]:
        print ("BAMBOOZLE!")
        check=False
    
    elif table[6]==table[7] and table[7]==table[8]:
        print ("BAMBOOZLE!")
        check=False
        
    elif table[0]==table[4] and table[4]==table[8]:
        print ("BAMBOOZLE!")
        check=False
    
    elif table[2]==table[4] and table[4]==table[6]:
        print ("BAMBOOZLE!")
        check=False
    else:
       
        check=True
        
    return check  

#Αρχικοποιώ το i για να κάνει συγκεκριμενες επαναλήψεις 
print("Lets start")        
print ("You are 'X' and the 'AI' is 'O'")
i=0
double_check=check()
while (i<10 and double_check):
    i=i+1
    thesi = int(input("Select thesi: "))
    while (thesi>=9):
        thesi = int(input("The input number must be below 9:"))
    if table[thesi] != "x" and table[thesi] !="o":
        table[thesi] = "x"
        finding = True
        while (finding):    
         random.seed() 
         enemy =  random.randint(0,8)
         
         if table[enemy] != "o" and table[enemy] != "x":
                    table[enemy] = "o"
                    finding = False
                    show(table)
        
    else: 
        print ("please another thesi")
        show(table)
    double_check=check()
	