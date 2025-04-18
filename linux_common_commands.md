

- linx 如何查看所有 python 进程
  - ps aux | grep pythonc


- linux 查看某个目录下一级子目录的大小 
  - du -sh */ | sort -h

- linux 普通用户 save vim file
  - :w !sudo tee %


### Docker 

- docker run -v ~/.ssh:/root/.ssh doceker镜像名
- docker build -t exp_image:0 .

- docker run -it --name exp_con -v py_projects:/work/projects -v ~/.ssh:/root/.ssh --gpus all --hostname experiments_container exp_image:0

- docker run -it --name llm_con -v local_llm:/local_llm -v ~/.ssh:/root/.ssh --gpus all --hostname llm_container base_image:4
- docker run -it --name llm_con -p 8000:8000 -v local_llm:/local_llm -v ~/.ssh:/root/.ssh --gpus all --hostname llm_container base_image:5

- docker run -it --name homework_con -v bjtu_homework:/bjtu/homework -v ~/.ssh:/root/.ssh --gpus all --hostname bjtu_homework_container exp_image:0
s

### uv
- uv add torch --extra-index-url https://download.pytorch.org/whl/cu128


### local llm
- uv run -m vllm.entrypoints.api_server --model LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --host 0.0.0.0 --port 8000 --seed 42 --tensor-parallel-size 2 --max-model-len 2048 --dtype=half --pipeline-parallel-size 1 --quantization awq --gpu-memory-utilization 0.95 --openai-api-compatible
- uv run -m vllm.entrypoints.openai.api_server --model LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --host 0.0.0.0 --port 8000 --seed 42 --tensor-parallel-size 2 --max-model-len 2048 --dtype=half --pipeline-parallel-size 1 --quantization awq --gpu-memory-utilization 0.95