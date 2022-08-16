from Data_Structures.STACK.Stack_DS import stack

def rev_str(act_str):
     s = stack()
     for i in range(len(act_str)):
         s.push(act_str[i])

     rever_str = ""

     while not s.is_empty():
        rever_str += s.pop()

     return rever_str

input_str = "Hello World!"

print("string to rever is Hello World!", rev_str(input_str))
