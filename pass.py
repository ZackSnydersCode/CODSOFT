import random
import string
import re

def generator(v1,v2):
   pass_pattern = string.ascii_letters
   pass_pattern += string.digits
   if v2:
    if v2 == True:
      pass_pattern += string.punctuation
   password = ''.join(random.choice
   (pass_pattern) for _ in range(v1))
   print('>>>>>Password->',password)
    
def input_some_info():
    key  = input("Enter 1 for regular theme Or Enter 0 for Command theme\t")
    if key == '0':
     print('******Custome Command = pass(length_of_password,use_of_special_chars(bollean))')
     command = input(">>>\t").strip()
     if command.startswith('pass(') and command.endswith(')'):
        ptrn_mtch = re.match(r'pass\((\d+)(?:,(\w+))?\)',command)
        if ptrn_mtch:
           val1 = int(ptrn_mtch.group(1))
           val2 = True
           if ptrn_mtch.group(2):
            val2 = ptrn_mtch.group(2).lower() == 'true' or ptrn_mtch.group(2).lower() == 'True'
           generator(val1,val2)
        else:
           print("Parameters are not correct")
     else:
        print("Invalid custom command format. Use 'pass(length_of_password,use_of_special_chars(boolean))'")

    elif '1' in key:
       pass_len = int(input("Enter length of password\t"))
       generator(pass_len,True)
       
input_some_info()
