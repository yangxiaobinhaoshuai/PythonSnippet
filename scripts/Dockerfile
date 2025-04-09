
# docker run cmd : docker run -it --name single1 --gpus all -v py_projects:/work/projects --hostname docker_container yxb_ubuntu_image:2025_03_27_30

# Docker domestic source : https://github.com/dongyubin/DockerHub
#FROM ubuntu:24.04

FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04


RUN apt update


# NB : Python3 is alread installed.
#    Python3 is shipped with venv
RUN apt install -y --no-install-recommends \
    wget \
    curl \
    vim  

RUN apt install -y --no-install-recommends \
    python3-pip\
    sudo \
    git \
    zsh\
    bat

# pciutils for lspci
RUN apt install -y --no-install-recommends \
    python3-venv \
    gcc \
    pciutils


RUN apt install -y --no-install-recommends \
    pipx \
    speedtest-cli


RUN echo "apt install successfully!"




WORKDIR /tmp

# 复制 requirements.txt 文件
COPY requirements.txt .

# install ohmyzsh 国内镜像
# 1. 安装 Oh My Zsh
RUN wget -O /tmp/install_ohmyzsh_gitee.sh https://gitee.com/leok77s/ohmyzsh-gitee/raw/main/install.gitee.sh \
    && chmod +x /tmp/install_ohmyzsh_gitee.sh \
    && sh -c "/tmp/install_ohmyzsh_gitee.sh"

# 2. 安装 zsh-autosuggestions 插件
RUN git clone --depth=1 https://gitee.com/hailin_cool/zsh-autosuggestions.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh}/custom/plugins/zsh-autosuggestions

# 3. 修改 ~/.zshrc 文件
# 查看 .zshrc 内容 (用于调试)
RUN cat /root/.zshrc

# 尝试更宽松的 sed 命令添加插件
RUN sed -i 's/)/ zsh-autosuggestions)/' /root/.zshrc

# 添加 bindkey
RUN echo "bindkey '^I^I' autosuggest-accept" >> /root/.zshrc


# 设置 Zsh 为默认 Shell
RUN chsh -s /usr/bin/zsh root

RUN zsh -c "source ~/.zshrc"

RUN echo "Config zshrc successfully!"




# 创建 python 软链接
RUN ln -s /usr/bin/python3 /usr/bin/python


# pip 换源
# 设置 pip 全局镜像源为清华源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 设置 pip 信任清华源，避免 HTTPS 警告
RUN pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn

# 换回默认源
#pip config unset global.index-url




# Install uv 


RUN pipx install uv

# 将 pipx 的 bin 目录添加到 PATH 环境变量
ENV PATH="$PATH:/root/.local/bin"

# 因此，更推荐的方式是设置 UV_INDEX_URL：
ENV UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple/"

# 你也可以设置 UV_EXTRA_INDEX_URL 来添加额外的索引源
ENV UV_EXTRA_INDEX_URL="https://mirrors.aliyun.com/pypi/simple/"

RUN uv --version

RUN echo "Install uv successfully!"





CMD ["zsh"]
