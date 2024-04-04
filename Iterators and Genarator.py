Iterators-with help of  iter method to create sequences of iterators. whole object will be stored in memory at same time and then with help of next method it will be iterate one by one.
    
Generators-with help of yield keyword and function to create generator object.It will produce large sequence  at a time.Generators mainly used in memory optimization because it will iterate sequence of code.
Examples:

1.list1=[1,2,3,4]
print(iter(list1)) #<list_iterator object at 0x00000226A7451600>

2.list1=[1,2,3,'python']
x=iter(list1)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#output:
1
2
3
python


3.a=[10,20,30,40,50]
b=iter(a)

while(b):
    try:
        print(next(b))
    except StopIteration:
        print("no more values")
        break



4.class ten():
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
obj=ten()
for i in obj:
    print(i)


example for generators:

1.def num():
    yield 5
print(num()) #output:<generator object num at 0x00000200A25F9D20> - generators object because we used yield keywords it denotes generators object.


2.def num():
    yield 5
obj=num()
print(obj.__next__()) #output:5

3.def num():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

obj=num()
print(next(obj))#output:5
print(next(obj))#output:4
print(next(obj))#output:3
print(next(obj))#output:2
print(next(obj))#output:1 
print(next(obj))#Error:Stop Iteration 


4.def num():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

obj=num()
print(obj)#
for i in obj:
    print(i)
#output:
<generator object num at 0x000001AF03719E80>
5
4
3
2
1 

