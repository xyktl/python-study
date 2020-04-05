def print_line(char,times):

    """打印单行分割线

    :param char: 分割线字符
    :param times: 打印次数
    """
    print(char * times)


def print_lines(char,times,lows):

    """打印多行分割线

    :param char: 分割线字符
    :param times: 每行打印的次数
    :param lows: 行数
    """
    low = 0
    while low <= lows - 1:
        print_line(char,times)
        low += 1
print_lines("*",50,7)