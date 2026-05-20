#!/usr/bin/env python3
"""
示例模块 - 用于演示TestForge功能
这个文件包含了一些典型的Python函数和类
"""


def add(a: int, b: int) -> int:
    """
    计算两个整数的和
    
    Args:
        a: 第一个整数
        b: 第二个整数
    
    Returns:
        两个整数的和
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """计算两个整数的差"""
    return a - b


def multiply(a: int, b: int) -> int:
    """计算两个整数的乘积"""
    return a * b


def divide(a: float, b: float) -> float:
    """
    计算两个数的商
    
    Args:
        a: 被除数
        b: 除数
    
    Returns:
        商的浮点结果
    
    Raises:
        ValueError: 当除数为零时
    """
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def is_even(n: int) -> bool:
    """判断一个数是否为偶数"""
    return n % 2 == 0


def is_prime(n: int) -> bool:
    """
    判断一个数是否为质数
    
    Args:
        n: 待检测的整数
    
    Returns:
        如果是质数返回True，否则返回False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    生成斐波那契数列的前n项
    
    Args:
        n: 需要生成的项数
    
    Returns:
        包含前n项斐波那契数的列表
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def find_max(numbers: list) -> int:
    """找到列表中的最大值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return max(numbers)


def find_min(numbers: list) -> int:
    """找到列表中的最小值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return min(numbers)


def average(numbers: list) -> float:
    """计算列表的平均值"""
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)


def reverse_string(s: str) -> str:
    """反转字符串"""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """判断字符串是否为回文"""
    clean = s.lower().replace(" ", "")
    return clean == clean[::-1]


class Calculator:
    """
    简单的计算器类
    
    这个类提供基本的数学运算功能
    """
    
    def __init__(self):
        """初始化计算器"""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """加法"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """减法"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """乘法"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """获取计算历史"""
        return self.history.copy()
    
    def clear_history(self):
        """清空计算历史"""
        self.history.clear()


class StringHelper:
    """字符串处理辅助类"""
    
    @staticmethod
    def count_words(text: str) -> int:
        """统计单词数量"""
        return len(text.split())
    
    @staticmethod
    def capitalize_words(text: str) -> str:
        """首字母大写"""
        return text.title()
    
    @staticmethod
    def remove_punctuation(text: str) -> str:
        """移除标点符号"""
        import string
        return text.translate(str.maketrans("", "", string.punctuation))
