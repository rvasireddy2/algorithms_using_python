"""Recursive Karatsuba Multiplier"""
# Number-1: 3141592653589793238462643383279502884197169399375105820974944592
# Number-2: 2718281828459045235360287471352662497757247093699959574966967627
# Formula -> 10^n(ac)+10^(n/2)(ad+bc)+bd || a,b,c,d are n/2 digit numbers.

"""Get the input numbers (num1, num2)"""
number1 = input("Enter the first number:")
number2 = input("Enter the second number:")

"""karatsuba_main: inputs - num1, num2 || returns computed output."""
def karatsuba_main(num1,num2):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1*num2
    else:
        len_max = max(len(str(num1)),len(str(num2)))
        const_multiplier = len_max // 2

        a = num1 // 10**(const_multiplier)
        b = num1 % 10**(const_multiplier)
        c = num2 // 10**(const_multiplier)
        d = num2 % 10**(const_multiplier)
        print("a:"+str(a)+" b:"+str(b)+" c:"+str(c)+" d:"+str(d))
        pdt_bd = karatsuba_main(b,d)
        pdt_abcd = karatsuba_main((a+b),(c+d))
        pdt_ac = karatsuba_main(a,c)
        return (pdt_ac * 10**(2*const_multiplier)) + ((pdt_abcd - pdt_ac - pdt_bd) * 10**(const_multiplier)) + (pdt_bd)

# Invoke karat using user provided inputs:
multiplied_output = karatsuba_main(int(number1), int(number2))
print("Multiplier Result:"+str(multiplied_output))