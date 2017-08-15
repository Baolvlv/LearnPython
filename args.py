def add_end(L = None):
    if L == None:
        L = []
    L.append('END')
    return L
def calc(*num):
    sum  = 0
    for n in num:
        sum += n
        n += 1
    return sum
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
def stu(name,age,*,city='beijing',job):
    print(name,age,city,job)
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'arg=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
