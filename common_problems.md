

# Daily Problems Record


## Deps issues


### Pip Relative
- [Python can't find module, even after pip install](https://www.reddit.com/r/learnpython/comments/osvtik/python_cant_find_module_even_after_pip_install/)



### Conda Relative
- CondaError: Run 'conda init' before 'conda activate'
  - [Solution conda init zsh](https://stackoverflow.com/a/78101613/10247834)

### Bash
- bash xxx.sh 若 sh 中有 python xx.py ，如果此时 python 环境有问题， 可能 console 不会有任何 err output
  - 需要 python xxx.py 2>&1 将 Python 程序的 stderr 重定向到 stdout，以便在控制台上显示错误信息

## VsCode

### Rsync
- Vscode Rsync plugin failed 
  - ssh-copy-id -p 57313 root@i-1.gpushare.com
  - 复制公钥到远程服务器
  - ssh-copy-id 本质上是 cat ~/.ssh/id_rsa.pub | ssh -p 57313 root@i-1.gpushare.com "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
  - 你需要首次手动输入密码，成功后下次就不再需要输入


### Terminal stacktrace highlight
- Refer to : https://blog.csdn.net/m0_73832962/article/details/132202467 (Cursor 0.46.8 并不生效)

- | sed -E "s|(/[^[:space:]]+)|\x1b[1;34m\1\x1b[0m|g"
命令后添加下面命令
```aiignore
    #  purple color
   | sed -E "s|(/[^[:space:]]+)|\x1b[1;34m\1\x1b[0m|g"
    #  red color
   | sed -E "s|(/[^[:space:]]+)|\x1b[1;31m\1\x1b[0m|g"
    #  along with ccze
   2>&1 | ccze -A |  sed -E "s|(/[^[:space:]]+)|\x1b[1;31m\1\x1b[0m|g"

```
或

1. ：在 ~/.bashrc 末尾添加
2. 
```aiignore
    highlight_paths() {
        # "$@" 2>&1 | sed -E "s|(/[^[:space:]]+)|\x1b[1;34m\1\x1b[0m|g"
        "$@" 2>&1 | ccze -A | sed -E "s|(/[^[:space:]]+)|\x1b[1;31m\1\x1b[0m|g"
    }

alias run='highlight_paths'
```

如果命令卡住不输出：命令前 + PYTHONUNBUFFERED=1
```aiignore
# 添加 highlight_paths 函数和 run 别名到 shell 配置文件
RUN echo 'highlight_paths() {' >> /root/.bashrc && \
    echo '    PYTHONUNBUFFERED=1 "$@" 2> >(sed -E "s|(/[^[:space:]]+)|\x1b[1;31m\1\x1b[0m|g" >&2) | sed -E "s|(/[^[:space:]]+)|\x1b[1;34m\1\x1b[0m|g" || true' >> /root/.bashrc && \
    echo '}' >> /root/.bashrc && \
    echo 'alias run="highlight_paths"' >> /root/.bashrc
```

步骤 2：重新加载 ~/.bashrc
```aiignore
source ~/.bashrc
```

步骤 3：使用 run 命令执行其它任何命令


- 使用 ccze 或 lolcat 进行输出高亮
```aiignore
sudo apt install ccze  # Ubuntu/Debian
brew install ccze      # macOS

some_command | ccze
```
- Usage : some_command | lolcat


### Numpy Issues
- NumPy 的视图机制在处理大数组时，即使只取部分数据，也会保持对原始数据的引用，这可能导致内存使用效率不高
  - 注意不要在循环内使用 np.slice 


