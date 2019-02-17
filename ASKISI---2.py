# Python program to print prime factors 
  
import math 
  
#Βάζουμε τον αριθμό που θέλουμε , μικροτερος απο 10000 
n=int(input('Enter a number'))
while n > 100000:
    print('please try again')
    n=int(input('Enter a number'))
    
#Ελγχουμε αν διαιρείτε με το 2 	
while n % 2 == 0:
    print('2*')
    n = n / 2
 #Όταν σταματήσει  να διαιρείτε με το 2 έλεγχει για τους υπόλοιπυς πρώτους    
i = 3
while n>0:
  if n % i == 0:
    print( i )
    n = n / i
  else:
    i = i + 3
            