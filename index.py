def series(n):  
   if n <= 1:  
       return n  
   else:  
       return(series(n-1) + series(n-2))  
term = int(input("enter limit"))  
  
if term <= 0:  
   print("enter a number")  
else:  
   print("series:")  
   for i in range(term):  
       print(series(i))  