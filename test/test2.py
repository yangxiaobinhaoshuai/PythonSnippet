from deep_learning.common_functions import format_now

print("I am test2")



# Choose gpu
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"




def get_current_process_gpu():
    import os
    import subprocess
    pid = os.getpid()  # 获取当前进程ID

    # 获取进程和GPU UUID的关联
    try:
        result = subprocess.check_output(['nvidia-smi', '--query-compute-apps=pid,gpu_uuid', '--format=csv,noheader'])
    except subprocess.CalledProcessError:
        return f"无法获取PID {pid}的GPU信息"

    target_gpu_uuid = None

    # 寻找当前PID使用的GPU UUID
    for line in result.decode('utf-8').strip().split('\n'):
        if line:
            parts = [part.strip() for part in line.split(',')]
            if len(parts) >= 2 and parts[0] == str(pid):
                target_gpu_uuid = parts[1]
                break

    if not target_gpu_uuid:
        return f"找不到PID {pid}关联的GPU"

    # 获取所有GPU的信息（索引和UUID）
    try:
        gpu_info = subprocess.check_output(['nvidia-smi', '--query-gpu=index,uuid,name,memory.used', '--format=csv,noheader'])
    except subprocess.CalledProcessError:
        return f"找到GPU UUID {target_gpu_uuid}，但无法获取详细信息"

    # 根据UUID找到对应的索引号和名称
    for line in gpu_info.decode('utf-8').strip().split('\n'):
        if line:
            parts = [part.strip() for part in line.split(',')]
            if len(parts) >= 2 and parts[1] == target_gpu_uuid:
                return f"PID {pid} 正在使用物理GPU {parts[0]}: {parts[2]}, 内存使用: {parts[3] if len(parts) > 3 else '未知'}"

    return f"找到UUID {target_gpu_uuid}，但无法在GPU列表中匹配"

# 确保GPU已分配
import torch
if torch.cuda.is_available():
    torch.zeros(1).cuda()

print(get_current_process_gpu())

now = format_now()
print("now", now)

# while True:
#     now = format_now()
#     print("now", now)
