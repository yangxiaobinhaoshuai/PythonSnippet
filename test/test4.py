




import os
import time

os.environ["CUDA_VISIBLE_DEVICES"] = "5"

import setproctitle
import time
import torch

# 确保GPU被使用
if torch.cuda.is_available():
    torch.zeros(1).cuda()

# 设置进程名称
setproctitle.setproctitle("我的GPU进程")

# 保持进程运行一段时间以便观察
print("进程名称已修改，请运行 nvidia-smi 查看")
time.sleep(300)  # 睡眠5分钟