from functools import reduce
def normalize(name):
#    return name[0].upper()+name[1:len(name)].lower()
    return name.capitalize()
def prod(L):
    return reduce(lambda x,y: x*y,L)
def str2float(s):
    def char2num(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    sp = s.split('.')
    return reduce(lambda x,y:10*x+y,map(char2num,sp[0]))+reduce(lambda x,y:10*x+y,map(char2num,sp[1]))/10**len(sp[1])

