class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty(),"Stack kosong. tidak bisa diintip"
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty(),"Stack kosong. tidak bisa di-pop"
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

class StactLL(object):
    def __init__(self):
        self.top=None
        self.size=0
    def isEmpty(self):
        return self.top is None
    def __len__(self):
        return self.size
    def peek(self):
        assert not self.isEmpty(),"Stack kosong. tidak bisa diintip"
        return self.top.item
    def pop(self):
        assert not self.isEmpty(),"Stack kosong. tidak bisa di-pop"
        node=self.top
        self.top=self.top.next
        self.size-=1
        return node.item
    def push(self,data):
        self.top= _StackNode(data,self.top)
        self.size+=1
class _StackNode(object):
    def __init__(self,data,link):
        self.item=data
        self.next=link
class Queue(object):
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self.qlist)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert self.isEmpty(),"Antrian Kosong"
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert self.isEmpty(),"Antrian Kosong"
        return self.qlist[0]
    def getRearMost(self):
        assert self.isEmpty(),"Antrian Kosong"
        a=len(self)-1
        return self.qlist[a]

class priorityQueue(Queue):
    def enqueue(self,data,priority):
        entry=priorityEntry(data,priority)
        i=0
        while i<len(self.qlist):
            if entry.priority<self.qlist[i].priority:
                self.qlist.insert(i,entry)
                return
            i+=1
        self.qlist.append(entry)
    def dequeue(self):
        assert not self.isEmpty(),"Antrian Kosong"
        return self.qlist.pop(0)
class priorityEntry(object):
    def __init__(self,data,priority):
        self.item=data
        self.priority=priority
    def __str__(self):
        return self.item

#Nomor 1
def cetakHexa(angka):
    digits="0123456789ABCDEF"
    stack=Stack()
    st=""
    if angka==0:
        stack.push(0)
    while angka>0:
        digit=angka%16
        stack.push(digits[digit])
        angka=angka//16
    while len(stack)>0:
        st+=stack.pop()
    print(st)
cetakHexa(15)

#Nomor 2
nilai=Stack()
for i in range(16):
    if i%3==0:
        nilai.push(i)

#Nomor3
nilai=Stack()
for i in range(16):
    if i%3==0:
        nilai.push(i)
    if i%4==0:
        nilai.pop()

sequensial=priorityQueue()
sequensial.enqueue("Melon",2)
sequensial.enqueue("Semangka",5)
sequensial.enqueue("Jeruk",1)
sequensial.enqueue("Apel",6)
sequensial.enqueue("Durian",3)
print(sequensial.dequeue())
print(sequensial.dequeue())
print(sequensial.dequeue())
print(sequensial.dequeue())
print(sequensial.dequeue())


