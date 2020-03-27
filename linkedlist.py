class node:
    def __init__(self,data=None):
        self.__data=data
        self.__next=None

    def __isempty(self):
        if self.__data==None:
            return True
        else:
            return False

    def length(self):
        if self.__isempty()==True:
            return 0
        elif self.__next==None:
            return 1
        else:
            temp=self
            count=0
            while temp!=None:
                temp=temp.__next
                count=count+1
            return count

    def __append(self,value):
        if self.__isempty()==True:
            self.__data=value
            return()

        temp=self
        while temp.__next!=None:
            temp=temp.__next

        newnode=node(value)
        temp.__next=newnode
        return()

    def __insert(self,value):
        if self.__isempty()==True:
            self.__data=value

        newnode=node(value)
        self.__data,newnode.__data=newnode.__data,self.__data
        newnode.__next=self.__next
        self.__next=newnode

    def insertpos(self,pos,value):
        if int(pos)==0:
            self.__insert(value)                    #inserts value at first position
            return ()
        elif int(pos)>=self.length():
            self.__append(value)                    #appends value at the end
            return ()
        else:
            temp=self
            for i in range(1,int(pos)-1):          #inserts value at nth position
                temp=temp.__next

            newnode=node(value)
            newnode.__next=temp.__next
            temp.__next=newnode
            return ()

    def display(self):
        if self.__isempty()==True:
            return ()
        else:
            temp=self
            while temp!=None:
                print(temp.__data,end=' ')
                temp=temp.__next
            print ('\n')

    def remove(self,value):
        if self.__isempty()==True:
            return ()
        if self.__data==value:
            if self.__next==None:
                self.__data=None
            else:
                self.__data=self.__next.__data
                self.__next=self.__next.__next
                return ()
        else:
            temp=self
            while temp.__next!=None:
                if temp.__next.__data==value:
                    temp.__next=temp.__next.__next
                else:
                    temp=temp.__next
            return ()

if __name__=='__main__':
    llist=node()
    for i in range(0,10):
        llist.insertpos(i,i)

    llist.display()

    llist.insertpos(0,99)
    llist.display()
    llist.insertpos(99,55)
    llist.display()
    llist.insertpos(4,36)
    llist.display()
    llist.remove(99)
    llist.display()

