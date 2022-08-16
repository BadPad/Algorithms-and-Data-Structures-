from Data_Structures.STACK.Stack_DS import stack

def convert_int_to_bin(dec_num):
  s = stack()
  while dec_num>0:
        rem = dec_num%2
        s.push(rem)
        dec_num = dec_num//2
  print(s.get_stack())
  bin1 = ""
  while not s.is_empty():
    bin1 +=str(s.pop())
  return bin1

print(convert_int_to_bin(7))
