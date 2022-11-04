import os 

class Path:
    def displaytodo():
        path=os.path.realpath(__file__)#the path of this file
        dir0=os.path.dirname(path)#directory containing this file
        dir1=dir0.replace('python','txts')#change directory to sybling directory
        os.chdir(dir1)#changes current directory to dir1(/txts)
        f0=open('todo.txt','r') #6file reader
        list0=[]
        c0=0
        for c in f0:
            c0=c0+1
            if c0%2==1:
                print(list0)
                print('_______________')
                list0=[]
                list0.append(c)
            else:
                list0.append(c) 
        print(list0)
        f0.close()
    def musicpath():
        path=os.path.realpath(__file__)
        dir0=os.path.dirname(path)
        dir1=dir0.replace('python','music') 
        return dir1
print(Path.musicpath())
#Path()
#Path.f0()


