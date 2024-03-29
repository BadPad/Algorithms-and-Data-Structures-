from Data_Structures.STACK.Stack_DS import stack

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced == True:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False

        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

#print("is it balanced bracket, (){}[]{}(){{{(((}}})))", is_paren_balanced("(){}[]{}(){{{(((}}})))"))

#print("is it balanced brackets, }}}}((((())))){}{}[][][[[[]]]]]", is_paren_balanced("}}}}((((())))){}{}[][][[[[]]]]]"))

print("is it balanced brackets, ", is_paren_balanced("(((({}))))"))
