



# 设置进程名
from setproctitle import setproctitle
setproctitle("yxb_testing")



# 检查 GPU 可用性
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")



