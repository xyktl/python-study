#递归函数打印数字
def print_nums(num):
    """打印1~num的数字
  
    """
    print(num)
    if num == 1:
        return
    return print_nums(num-1)
print_nums(5)


#递归数字相加
def sum_numbers(num):
    """1~num相加的和

    """
    if num == 1:
        return num
    return sum_numbers(num - 1) + num
print(sum_numbers(10))