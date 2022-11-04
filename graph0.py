import math
def sp0():
    print(' ')
    print('ozozozozozozozozozozozozozozozozozozozozozozozozozozo')
    print(' ')

cmdlen=5

class Graph:
    def __init__(self):
        pass
    def plotvalue(self,x,y,length):
        s1='__'
        s2=' |'
        s3='_|'
        s4='  '
        l2=math.floor(length/2)
        for j in range(length):
            line=' '
            if j!=l2:
                for i in range(length):
                    if i!=l2:
                        line=line+s4
                    else:
                        line=line+s2
                print(line)
            else:
                for k in range(length):
                    if k!=l2:
                        line=line+s1
                    else:
                        line=line+s3
                print(line)





def debugger0():
    print('debugger 0')
    s1='__'
    s2=' |'
    s3='_|'
    s4='  '
    sxy='WM'
    length=35
    x=2
    y=4
    l2=math.floor(length/2)
    for j in range(length):
            line=' '
            if j!=l2:
                for i in range(length):
                    if i!=l2 and i!=x:
                        line=line+s4
                    elif i!=l2 and i==x:
                        line=line+sxy
                    else:
                        line=line+s2
                print(line)
            else:
                for k in range(length):
                    if k!=l2 and k!=y:
                        line=line+s1
                    elif k!=l2 and k==y:
                        line=line+sxy
                    else:
                        line=line+s3
                print(line)
#debugger0()
def debugger1():
        print('debugger 1')
        length=35
        x=3
        y=7
        s1='__'
        s2=' |'
        s3='_|'
        s4='  '
        sxy='WM'
        l2=math.floor(length/2)
        for j in range(length):
            line=' '
            if j!=l2 and j!=x:
                for i in range(length):
                    if i!=l2:
                        line=line+s4
                    else:
                        line=line+s2
                print(line)
            elif j==l2 and j!=x:
                for k in range(length):
                    if k!=l2:
                        line=line+s1
                    else:
                        line=line+s3
                print(line)
            elif j!=l2 and j==x:
                for i in range(length):
                    if i!=l2 and i!=y:
                        line=line+s4
                    elif i==l2 and i!=y:
                        line=line+s2
                    elif i!=l2 and i==y:
                        line=line+sxy
                    elif i==l2 and i==y:
                        line=line+sxy
                print(line)
#debugger1()

def debugger2():
        print('debugger 2')
        length=35
        x=17
        y=10
        s1='__'
        s2=' |'
        s3='_|'
        s4='  '
        sxy='WM'
        l2=math.floor(length/2)
        for j in range(length):
            line=' '
            if j!=x:
                if j!=l2:
                    for i in range(length):
                        if i!=l2:
                            line=line+s4
                        else:
                            line=line+s2
                    print(line)
                else:
                    for k in range(length):
                        if k!=l2:
                            line=line+s1
                        else:
                            line=line+s3
                    print(line)
            else:
                for i in range(length):
                    if i!=y:
                        if i!=l2:
                            line=line+s1
                        else:
                            line=line+s2
                    else:
                        if i!=l2:
                            line=line+sxy
                        else:
                            line=line+sxy
                print(line)
#debugger2()
def debugger3():
        print('debugger 3')
        length=35
        x=0#da igual
        m=1
        c=0
        y=m*math.sqrt(x)+c
        s1='__'
        s2=' |'
        s3='_|'
        s4='  '
        sxy='WM'
        l2=0
        for j in range(-length,length*cmdlen):
            x=math.fabs(j)
            if x >=0:
                y1=m*math.sqrt(x)+c
                y2=-m*math.sqrt(x)+c
            else: #beta
                y=x
            line='  '
            if j!=x:
                if j!=l2:
                    for i in range(-length,length):
                        if i!=l2:
                            line=line+s4
                        else:
                            line=line+s2
                    print(line)
                else:
                    for k in range(-length,length):
                        if k!=l2:
                            line=line+s1
                        else:
                            line=line+s3
                    print(line)
            else:
                for i in range(-length,length):
                    if i!=y1 and i!=y2:
                        if i!=l2 and j!=l2:
                            line=line+s4
                        elif i!=l2 and j==l2:
                            line=line+s1 
                        else:
                            line=line+s2
                    else:
                        if i!=l2:
                            line=line+sxy
                        else:
                            line=line+sxy
                print(line)
#debugger3()
def debugger4():
        print('debugger 4')
        length=35
        x=0#da igual
        m=1
        c=2
        y=m*x+c
        s1='__'
        s2=' |'
        s3='_|'
        s4='  '
        sxy='WM'
        l2=0
        for j in range(-length,length):
            x=j
            y=-1*(m*x+c)
            line='  '
            if j!=x:
                if j!=l2:
                    for i in range(-length,length):
                        if i!=l2:
                            line=line+s4
                        else:
                            line=line+s2
                    print(line)
                else:
                    for k in range(-length,length):
                        if k!=l2:
                            line=line+s1
                        else:
                            line=line+s3
                    print(line)
            else:
                for i in range(-length,length):
                    if i!=y:
                        if i!=l2 and j!=l2:
                            line=line+s4
                        elif i!=l2 and j==l2:
                            line=line+s1 
                        else:
                            line=line+s2
                    else:
                        if i!=l2:
                            line=line+sxy
                        else:
                            line=line+sxy
                print(line)
#debugger2()
def debugger5():
        print('debugger 5')
        length=35
        x=0#da igual
        m=1
        c=6
        y=0#da igual
        s1='__'
        s2=' |'
        s3='_|'
        s4='  '
        sxy='WM'
        l2=math.floor(length/2)
        for j in range(length):
            x1=j
            x2=-j
            y=m*math.sqrt(x)+c
            line='  '
            if j!=x1 and j!=x2:
                if j!=l2:
                    for i in range(length):
                        if i!=l2:
                            line=line+s4
                        else:
                            line=line+s2
                    print(line)
                else:
                    for k in range(length):
                        if k!=l2:
                            line=line+s1
                        else:
                            line=line+s3
                    print(line)
            elif j==x1 and j!=x2:
                for i in range(length):
                    if i!=y:
                        if i!=l2 and j!=l2:
                            line=line+s4
                        elif i!=l2 and j==l2:
                            line=line+s1 
                        else:
                            line=line+s2
                    else:
                        if i!=l2:
                            line=line+sxy
                        else:
                            line=line+sxy
                print(line)
            elif j!=x1 and j==x2:
                for i in range(length):
                    if i!=y:
                        if i!=l2 and j!=l2:
                            line=line+s4
                        elif i!=l2 and j==l2:
                            line=line+s1 
                        else:
                            line=line+s2
                    else:
                        if i!=l2:
                            line=line+sxy
                        else:
                            line=line+sxy
            elif j==x1 and j==x2:
                for i in range(length):
                    if i!=y:
                        if i!=l2 and j!=l2:
                            line=line+s4
                        elif i!=l2 and j==l2:
                            line=line+s1 
                        else:
                            line=line+s2
                    else:
                        if i!=l2:
                            line=line+sxy
                        else:
                            line=line+sxy
                print(line)
#debugger3()
def debugger():
    #Graph.plotvalue(0,2,5,35)
    #debugger0()
    debugger1()
    sp0()
    debugger2()
    sp0()
    debugger4()
    sp0()
    debugger3()
    sp0()
    #debugger5()
debugger()
