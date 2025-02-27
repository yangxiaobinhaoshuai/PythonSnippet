


# 查看当前 pip packages 位置
import sysconfig

#  /root/miniconda3/envs/auto_homework/lib/python3.8/site-packages
# e.g. pip3 --target=/root/miniconda3/envs/auto_homework/lib/python3.8/site-packages install <some module>
print("where install python packages.")
print(sysconfig.get_paths()["purelib"])


# 设置进程名
from setproctitle import setproctitle
setproctitle("yxb_testing")



# 检查 GPU 可用性
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")




import torch

if torch.cuda.is_available():
    gpu_index = torch.cuda.current_device()
    print(f'当前使用的 GPU 编号: {gpu_index}')
    # 获取当前可用的 GPU 数量
    print(f'Number of GPUs: {torch.cuda.device_count()}')
    print(f'GPU 设备名称: {torch.cuda.get_device_name(gpu_index)}')
else:
    print('未检测到可用的 GPU')



import subprocess

# 运行 nvidia-smi 命令并打印输出
result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE)
print(result.stdout.decode())

