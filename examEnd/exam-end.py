def function1():
    return 100 * 10


def function2():
    amount = 1 
    list1 = []
    for i in range(0,10):
        
        list1.append(amount)
        amount *= 2
    
    total =sum(list1)
    return total

    

def main():
    answer = ""
    var1 = function1()
    var2 = function2()
    

    if var1 == var2:
        answer = "Function 1 and Function 2 pay the same amount."
    if var1 < var2:
        answer = "Option 2 pays more"
    else:
        answer = "Option 1 pays more"
    print(answer)
    
    


var1 = function1
var2 = function2
main()

