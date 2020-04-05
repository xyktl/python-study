# 质数：又称素数，除了1和它本身没有其他的因数
# 求 1~100的质数
import time
start_time = time.time()
i = 2
while i <= 100:
    j = 2
    flags = True
    while j <= i ** 0.5:
        if i % j == 0:
            flags = False
            break
        j += 1
    if flags:
        pass
        print(i)
    i += 1
end_time = time.time()
use_time = end_time - start_time
print(use_time)
