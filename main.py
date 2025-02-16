import os


def get_directory_description(dir_name):
    """返回每个目录的详细描述"""
    descriptions = {
        # 基础知识部分
        "01_Python介绍和环境搭建": """# Python基础入门

## 本章节内容
- Python语言简介和特点
- Python的安装和环境配置
- 集成开发环境（IDE）的选择和使用
- 第一个Python程序
- Python解释器的使用
- 基本输入输出

## 学习目标
1. 理解Python语言的特点和应用场景
2. 能够独立完成Python环境搭建
3. 掌握Python程序的基本结构
4. 熟练使用IDE开发Python程序""",

        "02_变量和数据类型": """# Python变量和数据类型

## 本章节内容
- 变量的定义和使用规则
- 基本数据类型：
  1. 数值类型（整数、浮点数）
  2. 字符串类型
  3. 布尔类型
  4. 列表（List）
  5. 元组（Tuple）
  6. 字典（Dict）
  7. 集合（Set）
- 数据类型转换
- 变量作用域

## 学习目标
1. 掌握Python各种数据类型的特点和使用方法
2. 能够进行各种数据类型之间的转换
3. 理解变量作用域的概念""",

        "03_运算符和表达式": """# Python运算符和表达式

## 本章节内容
- 算术运算符（+、-、*、/、//、%、**）
- 比较运算符（>、<、==、!=、>=、<=）
- 逻辑运算符（and、or、not）
- 赋值运算符（=、+=、-=等）
- 位运算符
- 运算符优先级
- 表达式计算规则

## 学习目标
1. 掌握各类运算符的使用方法
2. 理解运算符优先级
3. 能够编写复杂表达式""",

        "04_控制流程": """本章节介绍：
- if-elif-else条件语句
- for循环语句
- while循环语句
- break和continue
- pass语句
- 循环嵌套
- 条件表达式""",

        "05_函数基础": """本章节介绍：
- 函数的定义和调用
- 函数参数
- 返回值
- 函数文档
- 局部变量和全局变量
- 匿名函数
- 函数作为参数""",

        # 进阶概念
        "01_面向对象编程": """本章节介绍：
- 类和对象的概念
- 类的定义和实例化
- 属性和方法
- 继承和多态
- 封装和访问控制
- 魔术方法
- 类方法和静态方法""",

        "02_模块和包": """本章节介绍：
- 模块的概念和使用
- 包的创建和管理
- 模块的导入方式
- 包的结构组织
- __init__.py的作用
- 模块搜索路径
- pip包管理工具""",

        "03_文件操作": """本章节介绍：
- 文件的打开和关闭
- 文件读写操作
- 文件指针操作
- 文件和目录管理
- 文本文件和二进制文件
- with语句的使用
- 文件编码处理""",

        "04_异常处理": """本章节介绍：
- 异常的概念
- try-except语句
- 异常类型
- 自定义异常
- raise语句
- finally子句
- 异常链""",

        "05_正则表达式": """本章节介绍：
- 正则表达式基础
- 元字符
- 重复模式
- 分组和捕获
- re模块的使用
- 常用正则表达式模式
- 正则表达式优化""",

        # 实用工具
        "01_常用标准库": """本章节介绍：
- os模块
- sys模块
- datetime模块
- json模块
- random模块
- math模块
- collections模块""",

        "02_第三方库使用": """本章节介绍：
- requests库
- pandas库
- numpy库
- matplotlib库
- pillow库
- beautifulsoup4库
- 其他常用第三方库""",

        "03_虚拟环境管理": """本章节介绍：
- 虚拟环境的概念
- venv的使用
- pip包管理
- requirements.txt
- 项目依赖管理
- 开发环境隔离
- conda的使用""",

        # 项目实战
        "01_命令行工具": """本章节介绍：
- 命令行参数处理
- argparse模块使用
- 控制台输入输出
- 命令行工具开发实践
- 项目打包发布""",

        "02_网络爬虫": """本章节介绍：
- 网络爬虫基础
- HTTP请求和响应
- 数据解析方法
- 反爬虫处理
- 数据存储
- 实战项目开发""",

        "03_Web应用": """本章节介绍：
- Web开发基础
- Flask框架入门
- 路由和视图
- 模板使用
- 数据库操作
- RESTful API
- 项目部署"""
    }
    
    return descriptions.get(dir_name, "# " + dir_name + "\n\n本目录用于学习相关内容。")

def create_learning_files(directory):
    """在指定目录下创建基础学习文件"""
    dir_name = os.path.basename(directory)
    description = get_directory_description(dir_name)
    
    base_files = {
        'README.md': description,
        'code/example.py': '# 本目录存放示例代码\n\n# 示例1\n\n# 示例2',
        'exercises/practice.py': '# 本目录存放练习题\n\n# 练习1：\n\n# 练习2：',
        'notes.md': '# 学习笔记\n\n## 重要概念\n\n## 关键知识点\n\n## 注意事项'
    }
    
    for file_name, content in base_files.items():
        file_path = os.path.join(directory, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"创建文件: {file_path}")

def create_directory_structure():
    directories = [
        # 第一阶段：Python基础
        "01_Python基础/01_Python介绍和环境搭建",
        "01_Python基础/02_变量和数据类型",
        "01_Python基础/03_运算符和表达式",
        "01_Python基础/04_控制流程",
        "01_Python基础/05_函数基础",
        
        # 第二阶段：Python进阶
        "02_Python进阶/01_面向对象编程",
        "02_Python进阶/02_模块和包",
        "02_Python进阶/03_文件操作",
        "02_Python进阶/04_异常处理",
        "02_Python进阶/05_正则表达式",
        
        # 第三阶段：数据库和Web开发
        "03_数据库和Web开发/01_MySQL基础",
        "03_数据库和Web开发/02_Python操作MySQL",
        "03_数据库和Web开发/03_Django基础",
        "03_数据库和Web开发/04_Django项目实战",
        
        # 第四阶段：大数据开发
        "04_大数据开发/01_Hadoop基础",
        "04_大数据开发/02_Hive数仓",
        "04_大数据开发/03_Spark基础",
        "04_大数据开发/04_PySpark开发",
        
        # 项目实战
        "05_项目实战/01_爬虫项目",
        "05_项目实战/02_数据分析项目",
        "05_项目实战/03_Web开发项目",
        "05_项目实战/04_大数据项目",
    ]
    
    # 创建主要目录
    main_directories = [
        "exercises",      # 综合练习题
        "examples",      # 示例代码
        "resources",     # 学习资源
        "projects",      # 项目文件
        "notes"          # 学习笔记
    ]
    
    # 创建目录和文件
    for directory in directories:
        path = os.path.join(os.getcwd(), directory)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"创建目录: {path}")
            create_learning_files(path)
        except Exception as e:
            print(f"创建目录 {path} 时出错: {str(e)}")
    
    # 创建主要目录
    for directory in main_directories:
        path = os.path.join(os.getcwd(), directory)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"创建主要目录: {path}")
            with open(os.path.join(path, 'README.md'), 'w', encoding='utf-8') as f:
                f.write(f'# {directory}\n\n本目录用于存放{directory}相关内容。')
        except Exception as e:
            print(f"创建目录 {path} 时出错: {str(e)}")
            
    print("\n所有目录和文件创建完成！")

if __name__ == "__main__":
    create_directory_structure()
