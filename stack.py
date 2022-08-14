# -*- coding: utf-8 -*-

"""
---------------------------------------------
    File name:       stack
    Description:     
    Development Env: macOS Monterey 12.4
    Version:         Python 3.8.6
    Author:         xiaoyan
    Date:           8/3/22
---------------------------------------------
"""

from pythonds.basic import Stack
import string

import List.node


def main():
    # test_stack_backend()
    # test_stack_frontend()
    '''
    t = check_parenthesis_string('(((())))'), check_parenthesis_string('(()()()(()))'), \
        check_parenthesis_string('(((((((())'), check_parenthesis_string(')))((((()()()())'), \
        check_parenthesis_string('(()(())())'), check_parenthesis_string('')
    '''
    # t = check_symbols('{{([][])}()}'), check_symbols('{{([][])}()'),check_symbols('{[]})')

    # t = O2B(233),O2B(8)
    # t = O2Base(233), O2Base(233, 16), O2Base(233, 8), O2Base(233, 10)

    # 中序转前后序同时执行的方法
    # t = inorder_change('A+B*C','postorder'),  inorder_change('A + B * C + D','postorder'), \
    #     inorder_change('(A+B)*(C+D)','postorder'),\
    #     inorder_change('(A+B)*C - (D-E) * (F+G)','postorder'),

    # 中序转后序
    # t = inorder_2_postorder('A+B*C'),  inorder_2_postorder('A + B * C + D'), \
    #     inorder_2_postorder('(A+B)*(C+D)'),\
    #     inorder_2_postorder('(A+B)*C - (D-E) * (F+G)'),\
    #     inorder_2_postorder('(A+B)*(C+D)*(E+F)'), \
    #     inorder_2_postorder('A+((B+C)*(D+E))'), \
    #     inorder_2_postorder('A*B*C*D + E+F')

    # 输出：('A B C * +', 'A B C * + D +', 'A B + C D + *',
    # 'A B + C * D E - F G + * -')

    # 中序转前序
    # t = inorder_2_preorder('A*B+C*D'), inorder_2_preorder('(A+B)*C'), \
    #     inorder_2_preorder('(A+B)*(C+D)'), inorder_2_preorder('A+B+C+D'),\
    #     inorder_2_preorder('(A+B)*C -(D-E) * (F+G)'), \
    #     inorder_2_preorder('(A+B)*(C+D)*(E+F)'),\
    #     inorder_2_preorder('A+((B+C)*(D+E))'), \
    #     inorder_2_preorder('A*B*C*D + E+F')
    # 输出：(
    # '+ * A B * C D',
    # '* + A B C',
    # '* + A B + C D',
    # '+ + + A B C D',
    # '- * + A B C * - D E + F G',
    # '* * + A B + C D + E F',
    # '+ A * + B C + D E',
    # '+ + * * * A B C D E F'
    # )

    t = compute_postorder('456*+'),  compute_postorder('78+32+/'), \
        compute_postorder('23*4+'), compute_postorder('12345*+*+'),
    # 输出 '456*+' 值为 34

    # 计算中序表达式字符串的值
    # t = compute_inorder('1+2*(5-2)'), compute_inorder('1+2+4*2'),\
    #     compute_inorder('1*2 + 6/3'),compute_inorder('2*(2+3*(4+6))'), \
    #     compute_inorder('(((1+2)*3) - (4+5+6-7) ) * 8')

    print(t)


class Stack_Backend_Operation:
    """自己写的Stack类，操作在列表尾端"""

    def __init__(self):
        self._stck = []

    def push(self, item):
        self._stck.append(item)  # O(1)

    def pop(self):
        return self._stck.pop()  # O(1)

    def peek(self):
        return self._stck[-1]

    def size(self):
        return len(self._stck)

    def is_empty(self):
        # return len(self._stck) > 0
        return self._stck == []


class Stack_Frontend_Operation:
    """自己写的Stack类，操作在列表首端。性能没有Backend好"""

    def __init__(self):
        self._stck = []

    def push(self, item):
        self._stck.insert(0, item)  # O(n)

    def pop(self):
        return self._stck.pop(0)  # O(n)

    def peek(self):
        return self._stck[0]

    def size(self):
        return len(self._stck)

    def is_empty(self):
        # return len(self._stck) > 0
        return self._stck == []


def compute_postorder(expr_str):
    s = Stack()
    for i in expr_str:
        if i == ' ':
            continue
        # if str(i).isdigit():
        if i in '0123456789':
            s.push(i)
        else:
            j = s.pop()
            k = s.pop()
            s.push(eval(f'{k} {i} {j}'))
    return s.pop()


#  计算中序表达式字符串的值(有优先级问题)， 不用eval函数 '1+2*(5-2)'
#  数字放一个栈，运算符放一个栈
def compute_inorder(expr_str):
    d = {'*': 3, '/': 3, "+": 2, "-": 2, '(': 1}
    s_num = Stack()
    s_symbol = Stack()
    r = 0
    for i in expr_str:
        if i in '0123456789':
            s_num.push(i)
        elif i in d:
            s_symbol.push(i)
        elif i == ')':
            j = s_symbol.pop()
            while j != '(':
                # 先把括号里的表达式计算了
                num1 = s_num.pop()
                num2 = s_num.pop()
                r = do_math(j, int(num2), int(num1))
                s_num.push(r)
                j = s_symbol.pop()
    while s_num.size() > 1:
        # 计算最外层表达式的值(优先级最低的运算符)。
        num1 = s_num.pop()
        num2 = s_num.pop()
        symbol = s_symbol.pop()
        r = do_math(symbol, int(num2), int(num1))
        s_num.push(r)

    return s_num.pop()


def do_math(symbol, num_l, num_r):
    '''做运算'''
    if symbol == '+':
        return num_l + num_r
    elif symbol == '-':
        return num_l - num_r
    elif symbol == '*':
        return num_l * num_r
    elif symbol == '/':
        return num_l // num_r


def inorder_2_preorder(expression_str):
    """中序转前序"""
    symbol_order_dict = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        ')': 1  # 字符串反转，以这个作为子运算的开始，不存储'('，遇到'(',弹出所有直到弹出')'
    }
    s = Stack()  # 存储运算符（按照处理的优先顺序）
    ret = []  # 存储结果

    for i in expression_str[::-1]:  # 反转字符串处理
        # 循环字符串，处理每个字符
        if i == ' ':
            # 字符串空格过滤掉
            continue
        if i in string.ascii_uppercase:
            # Step 1： 如果是操作数(大写字母)，直接放入结果列表尾部
            ret.append(i)
        elif i == ')':
            # Step 2： 如果是右括号，入栈
            s.push(i)
        elif i == '(':
            # Step 3:  如果是左括号，
            # 循环从栈移除元素，直到移除右括号(，将取出的加入结果列表末尾。
            j = s.pop()
            while not s.isEmpty() and j != ')':
                ret.append(j)
                j = s.pop()
        elif i in symbol_order_dict.keys():
            # Step 4: 如果是运算符，
            # #空栈时直接入栈。
            # 栈不空时，先循环与栈顶元素比较：
            # 如果栈顶元素优先级高，则要先弹出栈顶元素放入结果列表中末尾。直到优先级低了，
            # 压当前运算符 入栈
            if s.isEmpty():
                s.push(i)
            else:
                while not s.isEmpty() and \
                    symbol_order_dict[s.peek()] > symbol_order_dict[i]:
                    ret.append(s.pop())
                s.push(i)

    # Step 5: 把栈中剩下的元素全部添加到结果列表末尾
    while not s.isEmpty():
        ret.append(s.pop())
    ret.reverse()  # 反转列表
    return ' '.join(ret)


def inorder_2_postorder(expression_str):
    """中序转后序"""
    ''''''
    symbol_order_dict = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    s = Stack()  # 存储运算符（按照处理的优先顺序）
    ret = []  # 存储结果

    for i in expression_str:
        # 循环字符串，处理每个字符
        if i == ' ':
            # 字符串空格过滤掉
            continue
        if i in string.ascii_uppercase:
            # Step 1： 如果是操作数(大写字母)，直接放入结果列表尾部
            ret.append(i)
        elif i == '(':
            # Step 2： 如果是左括号，入栈
            s.push(i)
        elif i == ')':
            # Step 3:  如果是右括号，
            # 循环从栈移除元素，直到移除左括号(，将取出的加入结果列表末尾。
            j = s.pop()
            while not s.isEmpty() and j != '(':
                ret.append(j)
                j = s.pop()
        else:
            # Step 4: 如果是运算符，
            # 入栈，但是，入栈前，循环与栈顶元素比较：
            # 如果栈顶元素优先级高，则要先取出栈顶元素放入结果列表中末尾。直到优先级低了
            # 压入当前运算符
            while not s.isEmpty() and \
                symbol_order_dict[s.peek()] >= symbol_order_dict[i]:
                ret.append(s.pop())
            s.push(i)
    # Step 5: 把栈中剩下的元素全部添加到结果列表末尾
    while not s.isEmpty():
        ret.append(s.pop())

    return ' '.join(ret)


def inorder_change(expression_str, order_type='preorder'):
    """中序转前或后序，（前序后序有4点不同，详细见下注释"不同的地方1/2/3/4"）
    @:param order_type, preorder 前序；
                        postorder 后序
    """

    # 不同的地方 1 （中序转前序、后序） - ：括号的起始和结束不一样，程序中出现4处
    # 表达式的子运算()里的处理, 如(A+B)*C里的(A+B)：
    # 前序: 是对真个表达式的反转串操作，故)为起始字符，入栈。
    # 等遇到(右括号即子运算结束字符时，循环弹出栈里的元素， 直到弹出)
    # 后序，(为子表达式的起始字符，入栈,其它操作符、运算符等接连入栈。
    # 等遇到)时循环弹出栈里的元素直到弹出(。
    order_info = {
        'preorder': {
            'sub_expr_start_flag': ')',
            'sub_expr_end_flag': '('
        },
        'postorder': {
            'sub_expr_start_flag': '(',
            'sub_expr_end_flag': ')'
        }
    }

    # 处理出栈优先级，栈里存的运算符优先级高时，弹出栈并加入结果集尾
    symbol_order_dict = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        order_info[order_type]['sub_expr_start_flag']: 1
    }

    s = Stack()  # 存储运算符（按照处理的优先顺序）
    ret = []  # 存储结果

    # 不同的地方 2（中序转前序、后序） - ： 前序 处理反串
    if order_type == 'preorder':
        expression_str = expression_str[::-1]

    for i in expression_str:
        # 循环字符串，处理每个字符
        if i == ' ':
            # 字符串空格过滤掉
            continue
        if i in string.ascii_uppercase:
            # Step 1： 如果是操作数(大写字母)，直接放入结果列表尾部
            ret.append(i)
        elif i == order_info[order_type]['sub_expr_start_flag']:
            # Step 2： 如果是左括号，入栈
            s.push(i)
        elif i == order_info[order_type]['sub_expr_end_flag']:
            # Step 3:  如果是右括号，
            # 循环从栈移除元素，直到移除左括号(，将取出的加入结果列表末尾。
            j = s.pop()
            while not s.isEmpty() and \
                j != order_info[order_type]['sub_expr_start_flag']:
                ret.append(j)
                j = s.pop()
        else:
            # 不同的地方 3（中序转前序、后序） - ： 栈里运算符优先级比较，前序同级别的不弹出
            # Step 4: 如果是运算符，
            # 入栈，但是，入栈前，循环与栈顶元素比较：
            # 如果栈顶元素优先级高，则要先取出栈顶元素放入结果列表中末尾。直到优先级低了
            # 压入当前运算符
            if order_type == 'preorder':
                while not s.isEmpty() and \
                    symbol_order_dict[s.peek()] > symbol_order_dict[i]:
                    ret.append(s.pop())
            else:
                while not s.isEmpty() and \
                    symbol_order_dict[s.peek()] >= symbol_order_dict[i]:
                    ret.append(s.pop())

            s.push(i)
    # Step 5: 把栈中剩下的元素全部添加到结果列表末尾
    while not s.isEmpty():
        ret.append(s.pop())

    # 不同的地方 4（中序转前序、后序） - ： 前序 再反转
    if order_type == 'preorder':
        ret.reverse()

    return ' '.join(ret)


def O2Base(num, base=2):
    """十进制到其它进制"""

    digits = '0123456789ABCDEF'
    s = Stack()  # Python自带Stack类，栈底在列表左侧

    while num > 0:
        tmp = num % base
        s.push(tmp)
        num = num // base

    # 看的 书上
    base_str = ''
    while not s.isEmpty():
        base_str = base_str + digits[s.pop()]

    return base_str


def O2B(num):
    """十进制到二进制"""
    s = Stack()  # Python自带Stack类，栈底在列表左侧

    while num > 0:
        tmp = num % 2
        s.push(tmp)
        num = num // 2

    # 看的 书上
    binary_str = ''
    while not s.isEmpty():
        binary_str = binary_str + str(s.pop())

    return binary_str


def check_parenthesis_string(parenthesis_str):
    """检测括号是否匹配正确"""
    stck = Stack()
    # 标志第一个先匹配到的圆括号串，如果是右括号)，直接退出返回False，否则pop抛异常
    no_left_parenthesis_shown = True
    for i in parenthesis_str:
        if i == '(':
            no_left_parenthesis_shown = False
            stck.push(i)
        elif i == ')':
            if no_left_parenthesis_shown:
                # 第一个匹配到) 退出
                return False
            stck.pop()
    return stck.isEmpty()


def check_symbols(symbor_str):
    """检测符号({[和]})是否匹配正确"""
    stck = Stack()
    # 标志第一个先匹配到的圆括号串，如果是右括号)，直接退出返回False，否则pop抛异常
    no_left_symbol_shown = {'(': True, '{': True, '[': True}
    symbol_map = {')': '(', ']': '[', '}': '{'}
    index = 0
    while index < len(symbor_str):
        symbol = symbor_str[index]
        if symbol in '({[':
            no_left_symbol_shown[symbol] = False
            stck.push(symbol)
        elif symbol in ')}]':
            if no_left_symbol_shown[symbol_map[symbol]]:
                # 先匹配到结束符号)]}， 退出
                return False
            top = stck.pop()
            if not match(top, symbol):
                # 匹配不对，如 (}。一出现右边的符号，必与物理位置前一个是配对的，否则整个匹配失败。
                return False
        index += 1
    return stck.isEmpty()


def match(open_char, close_char):
    opens = '({['
    closes = ')}]'
    return opens.index(open_char) == closes.index(close_char)


def test_stack_backend():
    s = Stack_Backend_Operation()
    test_stack(s)


def test_stack_frontend():
    s = Stack_Frontend_Operation()
    test_stack(s)


def test_stack(s):
    print(s.is_empty())  # True

    s.push(4)
    s.push('dog')
    print(s.peek())  # dog

    s.push(True)
    print(s.size())  # 3

    print(s.is_empty())  # False

    s.push(8.4)
    print(s.pop())  # 8.4

    print(s.pop())  # True
    print(s.size())  # 2


main()
