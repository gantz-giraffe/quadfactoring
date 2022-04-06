import re
from cmd import Cmd

def factor(a,b,c):
    prod = a*c
    for i in range(1,abs(prod)):
        qpi = abs(prod) / i
        out = lambda x,y : print('%d + %d = %d' % (x,y,b))
        check = lambda x : x == b
        if (prod > 0):
            if check(qpi + i):
                out(qpi,i)
                break
            elif check(-qpi - i):
                out(-qpi,-i)
                break
        elif (prod < 0):
            if check(qpi - i):
                out(qpi,-i)
                break
            elif check(-qpi + i):
                out(-qpi,i)
                break
        else:
            continue
    else:
        print("prime")


def factorcmd(str):
    terms = [int(s) for s in re.findall(r'-?\d+\.?\d*', str)]
    if terms:
        tl  = len(terms)
        if tl < 3:
            print("Not enough terms for my taste")
        elif tl > 3:
            print("Too many terms for my weak little brain :(")
        else:
            factor(terms[0],terms[1],terms[2])
    else:
        print("I'm too dumb to understand anything besides numbers :/")



class prompt(Cmd):
    intro = "What is thy bidding, my homeboy?"
    prompt = ">"
    def emptyline(self):
        pass
    def do_exit(self, inp):
        print("bye bye")
        return(True)
    def default(self, inp):
        factorcmd(inp)

prompt().cmdloop()