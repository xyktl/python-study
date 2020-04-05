#关键字 yield 的作用就是把一个函数变成一个生成器（generator），带有 yield 的函数不再是一个普通函数，
#Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 
#iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到
# yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句
#继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，
#直到再次遇到 yield

#斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个
#数都可由前两个数相加得到。用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题

#生成器和迭代器很类似
#!/usr/bin/python
# coding:utf-8
def fib(max):
    n,a,b = 0,0,1   
    while n <= max:
        print(b)
        a,b = b,a+b
        n+=1
fib(5) 


#上面函数返回的是None ,函数的可复用性差
#下面用一个列表接受返回的值
def fib_list(max):
    n,a,b = 0,0,1
    list = []
    while n <= max:
        list.append(b)
        a,b = b,a+b
        n+=1
    print(list)
fib_list(5)
#但是列表会随着max的增大而占用较大的内存，这时候
#来保存中间结果，而是通过 iterable 对象来迭代  
#同时实现__iter__(self)  和 __next__(self)的对象为迭代器

class Fib(object): 
 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 
 
    def __iter__(self): 
        return self 
 
    def __next__(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
for n in Fib(5):
    print(n)

print("\r")
#yield 可以简单的实现迭代器的功能
#yield不但可以返回一个值，它还可以接收调用者发出的参数。"
def fib_iterable(max):
    n,a,b = 0,0,1   
    while n <= max:
        yield b
        a,b = b,a+b
        n+=1
for n in fib_iterable(5):
    print(n)

 





