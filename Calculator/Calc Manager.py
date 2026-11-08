from math_calculator import run_calculator as math_calc
from tax_calculator import run_calculator as tax_calc
from unit_calculator import run_calculator as unit_calc

while True:
    userinp = int(input("Which Calculator would you like to use? : \n 1. Math Calculator \n 2. Tax Calculator \n 3. Unit Calculator \n 4. Quit \n Choice -  "))
    if userinp == 1:
         math_calc()
    elif userinp == 2:
         tax_calc()
    elif userinp == 3:
         unit_calc()
    elif userinp == 4:
        break
    else:
        print("Invalid Input")
