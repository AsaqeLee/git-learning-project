#!/usr/bin/env python3
"""
Git学习项目 - Python示例文件
这个文件用于演示Git的基本操作
"""

def greet(name="World"):
    """
    问候函数
    
    Args:
        name (str): 要问候的名字，默认为"World"
    
    Returns:
        str: 问候语
    """
    return f"Hello, {name}!"

def calculate_sum(a, b):
    """
    计算两个数的和（未完成的功能）

    Args:
        a (int): 第一个数
        b (int): 第二个数

    Returns:
        int: 两数之和
    """
    # 添加输入验证
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须是数字类型")
    return a + b

def main():
    """主函数"""
    print(greet())
    print(greet("Git学习者"))
    print("欢迎来到Git学习项目！")

    # 测试计算功能
    print(f"计算结果: {calculate_sum(5, 3)}")
    print(f"计算结果: {calculate_sum(10.5, 2.5)}")

if __name__ == "__main__":
    main()
