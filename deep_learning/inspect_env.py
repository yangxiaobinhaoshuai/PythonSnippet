

import torch

if torch.cuda.is_available():
    gpu_index = torch.cuda.current_device()
    print(f'当前使用的 GPU 编号: {gpu_index}')
    # 获取当前可用的 GPU 数量
    print(f'Number of GPUs: {torch.cuda.device_count()}')
    print(f'GPU 设备名称: {torch.cuda.get_device_name(gpu_index)}')
else:
    print('未检测到可用的 GPU')



counter = 0
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--proc_title", type=str, default=f'custom_proc')
    args = parser.parse_args()
    print("inspect_env args", args)


# e.g.
# 当前使用的 GPU 编号: 0
# Number of GPUs: 8
# GPU 设备名称: NVIDIA GeForce RTX 3090
# inspect_env args Namespace(proc_title='custom_proc_1')