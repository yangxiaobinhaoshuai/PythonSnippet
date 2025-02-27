import os


print("I am test3")

# 2>&1 它用于将 标准错误输出（stderr）重定向到 标准输出（stdout）

# PYTHONUNBUFFERED=1 禁用 Python 的输出缓冲。
# 确保 Python 立即输出所有的标准输出（stdout）和标准错误输出（stderr），这样 tee 能及时收到数据
# 防止命令出错了，程序会卡住
os.system("PYTHONUNBUFFERED=1 python3 test2.py 2>&1 | tee ./log11.txt")