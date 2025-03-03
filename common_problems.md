

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

### Rsync
- Vscode Rsync plugin failed 
  - ssh-copy-id -p 57313 root@i-1.gpushare.com
  - 复制公钥到远程服务器
  - ssh-copy-id 本质上是 cat ~/.ssh/id_rsa.pub | ssh -p 57313 root@i-1.gpushare.com "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
  - 你需要首次手动输入密码，成功后下次就不再需要输入

