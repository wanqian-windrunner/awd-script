

## 省流

按照程序反馈的来，攻击脚本写到 `attack_script.py` 中的 `attack()` 函数里。

## 文件结构

```
./awd/
├── attack_script.py
├── data_process.py
├── fast_ping.py
├── file_download.py
├── flag_submit.py
├── info
│   ├── alive_ips.txt
│   ├── api.txt
│   ├── attack_address.txt
│   └── token.txt
├── main.py
└── 读我读我读我读我读我读我读我读我读我读我读我读我.md
```

## 说明

### 信息初始化与扫描部分

 `fast_ping.py` 用于快速扫描 `ip` 的，可以单独运行，已经设置为交互式，而且增加了目标 `ip` 的显示

 `data_process.py` 用于处理已知数据，包括 `alive_ip` 列表，`flag` 列表，`token` 信息等，`Init` 类用于交互初始化存储数据到本地。`Config` 用于读取文件并存储数据，会读取是否存在 `12h` 以外修改的 `token.txt` 询问使用者是否重新进行交互初始化，还根据 `ip` 列表长度决定是否重新扫描。

 `main.py` 调用以上函数

然后读取 `alive_ip` 列表，如果 `ip` 数小于等于 `1` 的话重新进行扫描。

最后将初始信息打印出来进行确认。

### 攻击部分

调用一个函数，对 `alive_ip` 列表的所有 `ip`  多进程调用 `attack_script.py` 文件中的 `attack()` 函数，并立即进行提交 `flag` 并将 `flag` 存入一个列表。



### 兜底提交flag部分

对 `flag` 列表调用 `submit` 函数进行多进程提交。



### 有关 `attack_script.py` 中的 `attack()` 函数的编写要求

**此函数目的是最大程度保证主程序与攻击程序的独立性** ，要求很简单输入值只有一个 `ip` ，然后返回值是字符串类型的 `flag` ，为了减少不稳定性，最后又进行了一次类型转换。

为方便调试，单独运行此脚本需要单独交互输入攻击地址。



 



