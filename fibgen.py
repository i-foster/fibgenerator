def fibcheck(z):
    value1 = int(1)
    value2 = int(1) 
    while value1 <= z:
        y = value1
        value1 += value2
        value2 = y
        if value1 == z:
            return("it is a fibanachi number")
        elif value1 > z:
            return ("it is not fibanachi number")

inputValue = int(input("please enter a number "))
x = fibcheck(inputValue)
print(x)
