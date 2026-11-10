class stack():
    def __init__(self,*args):
        self.array=[]
        for i in args:
            self.array.append(i)
    def push(self,ele):
        self.array.append(ele)
    def pop(self):
        n=len(self.array)
        if(n==0):
            print('stack is empty')
        else:
            self.array.pop()
    def display(self):
        print(self.array)      
p= stack(1)
p.display()
p.push(10)
p.display()
p.pop()
p.display()
p.pop()
p.pop()
p.pop()