def cal( num1 , num2 , sign ):
    if sign ==' +':
        return num1 +num2 
    elif sign == '-':
        return num1 - num2 
    elif sign == '*':
        return num1 * num2 
    elif sign == '/':
        if num2 == 0:
            return(" cannot divide by 0 ")
        else :
            return num1 / num2 
signcheck = [ "+", "-", "*", "/"]


try:

    sign = input("enter the sign :")

    if sign not in  signcheck :
        raise ValueError(" Invalid sign ")
     
    num1 = int(input("Enter the  first number: "))
    num2 = int(input("Enter the second number: "))

    result = cal(num1 , num2 , sign)

    print(f" {num1} { sign} {num2} = {result} ")  

except ValueError as e:
    print(e)    


    
    
 