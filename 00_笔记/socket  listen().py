#listen(n)   中的参数表示socket 的排队数
#一般情况下，一个进程只有一个主线程（也就是单线程），那么socket允许的最大连接数为: n + 1
#如果服务器是多线程，比如代码开了2个线程，那么socket允许的最大连接数就是: n + 2

#换句话说：排队的人数(就是那个n) + 正在就餐的人数（服务器正在处理的socket连接数) = 
#允许接待的总人数（socket允许的最大连接数）


listen(1)
正在处理的socket连接数为1
单线程的情况下：socket允许的最大连接数为2

