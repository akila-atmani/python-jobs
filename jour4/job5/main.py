def calcule(num1,operator,num2):
 
 if operator == "+":
  addition = num1 + num2
  return(addition)
 
 elif operator == "-":
  soustraction = num1 - num2
  return (soustraction)
 
 elif operator== "*":
  multiplication = num1* num2
  return(multiplication)
 
 elif operator == "/":
  division = num1/num2
  return(division)
 
 elif operator== "%":
  modulo = num1 % num2
  return (modulo)
 


operation1 = calcule(1,"+",3)
print(operation1)


operation2 = calcule(5,"-",3)
print(operation2)


operation3 = calcule(10,"*",10)
print(operation3)
 