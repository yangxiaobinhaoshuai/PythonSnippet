import importlib
# mkl-service + Intel(R) MKL: MKL_THREADING_LAYER=INTEL is incompatible with libgomp.so.1 library.
#         Try to import numpy first or set the threading layer accordingly. Set MKL_SERVICE_FORCE_INTEL to force it.

# MKL_THREADING_LAYER=GNU

# Usage
# os.system("MKL_THREADING_LAYER=GNU python inspect_env.py --proc_title=st_norm")
# runpy.run_path("inspect_env.py", init_globals=params)


with open("common_functions.py","r") as f:
    file_contents = f.read()

exec(file_contents)

print("This is inspect_env.py")


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



def do_inspection():
    title = globals().get("proc_title",None) or args.proc_title
    if title:
        # noinspection PyUnresolvedReferences
        setMyProcTitle(title)
        print("current gpu index:", get_current_process_gpu())


def main():
    global args
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--proc_title", type=str, default=f'custom_proc')
    args = parser.parse_args()
    print("inspect_env args", args)
    #  Must ensure cuda usage.
    import torch
    if torch.cuda.is_available():
        torch.zeros(1).cuda()
    do_inspection()

main()

if __name__ == '__main__':
    main()

# e.g.
# 当前使用的 GPU 编号: 0
# Number of GPUs: 8
# GPU 设备名称: NVIDIA GeForce RTX 3090
# inspect_env args Namespace(proc_title='custom_proc_1')