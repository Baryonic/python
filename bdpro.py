import os 
class BD:
    def __init__(self,content,name):
        self.content=content
        self.name=name
        self.set1={}
    def displaystrs(self):
        print(f'name: {self.name} ||')
        for x in self.content:
            print(x)
    def addstr(self,str1):
        if str1 in self.content:
            print('str already exists')
        else:
            self.content.append(str1)
            database=open(databasename,'a')
            database.write('\n')
            database.write(str1)
            print('str1 added |',str1,'| str1 added')
def main():
    while(True):
        print(f'{bd.name} Choose option ')
        choice='''
        1. Display 
        2. Add str to the end
        3. Quit program
        '''
        print(choice)
        userinput0=int(input('option?     '))
        if userinput0==1:
            bd.displaystrs()
        elif userinput0==2:
            str2=input('ADD str: ')
            bd.addstr(str2)
        elif userinput0==3:
            print('END OF PROGRAM')
            return
        else:
            print('options--> 1: Display     2: ADD     3: QUIT  ')
if __name__=='__main__':
    path=os.path.realpath(__file__)#path of this file
    dirtxts=os.path.dirname(os.path.dirname(path)).replace('python','txts')#go to parent directory and then change for /txts
    print(dirtxts)
    os.chdir(dirtxts)#change dir to /txts
    list1=[]
    #4 lines for displaying all files in dir(/txts)
    root=dirtxts#this line is unnecesary
    for path, subdirs, files in os.walk(root):
        for name in files:
            print(os.path.join(path,name))

    databasename=input('enter the name of the database file with  extension:') #the file where the strs will be stored
    bd1=open(databasename,'r')
    for c in bd1:
        list1.append(c)
    bd=BD(list1,'XD')
    main()
        
