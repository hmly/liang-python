from Stack import Stack

def parCheck(string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        paran = string[index]
        if paran in '([{':
            s.push(paran)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, paran):
                    balanced = False
        index += 1
    return balanced and s.isEmpty()
            
def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

print(parCheck('(({[]}))'))
