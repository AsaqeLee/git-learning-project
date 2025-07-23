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

def main():
    """主函数"""
    print(greet())
    print(greet("Git学习者"))
    print("欢迎来到Git学习项目！")

if __name__ == "__main__":
    main()
