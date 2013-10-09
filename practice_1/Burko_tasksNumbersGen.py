# encoding=utf-8
num = raw_input("Please enter the number from [0,9] :\n")
try:
    num = int(num)
except ValueError:
    print("incorret number")

zero ="""
  ****  
 *    *
*      *
*      *
*      *
*      *
 *    *
  ****
"""
one = """
   **
  ***
 **** 
***** 
   ** 
   **
   **
******** 
"""
two = """
   ***
 **   **
**    **
     **
    **
   **
  **
 *******
"""
three = """
   ***
 **   **
**    **
    **
    **
**    **
 **   **
   ***     
"""
four =  """
    ****
   *****
  **  **
 **   **
**    **
********
      **
      **
"""
five = """
********
**
**
******
     ***
      **
     ***
*******
"""
six = """
********
**
**
********
**    **
**    **
**    **
********
"""
seven = """
********
      **
      **
    ****
      **
      **
      **
      **
"""
eight = """
********
**    **
**    **
 ******
 ******
**    **
**    **
********
"""
nine = """
********
**    **
**    **
**    **
********
      **
      **
********
"""
if num == 0:
   print zero
elif num == 1:
   print one
elif num == 2:
   print two
elif num == 3:
   print three
elif num == 4:
   print four
elif num == 5:
   print five
elif num == 6:
   print six
elif num == 7:
   print seven
elif num == 8:
   print eight
elif num == 9:
   print nine
else:
   print "Enter number from [0,9]


