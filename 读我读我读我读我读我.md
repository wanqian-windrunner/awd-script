# awd-script
awd's script


## 省流

按照程序反馈的来，攻击脚本写到 `attack_script.py` 中的 `attack()` 函数里。

## 文件结构

```
./awd/
├── attack_script.py
├── fast_ping.py
├── file_download.py
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

 `fast_ping.py` 是用于快速扫描 `ip` 的，可以单独运行，已经设置为交互式，而且增加了目标 `ip` 的显示

 `main.py` 用于在开赛前读取是否存在一天以内创建的 `token.txt` 如果不存在或者一天以上，则重新进行交互初始化。

然后读取 `alive_ip` 列表，如果 `ip` 数小于等于 `1` 的话重新进行扫描。

最后将初始信息打印出来进行确认。

### 攻击部分

调用一个函数，对 `alive_ip` 列表的所有 `ip`  多进程调用 `attack_script.py` 文件中的 `attack()` 函数，并立即进行提交 `flag` 并将 `flag` 存入一个列表。



### 兜底提交flag部分

对 `flag` 列表调用 `submit` 函数进行多进程提交。



### 有关 `attack_script.py` 中的 `attack()` 函数的编写要求

**此函数目的是最大程度保证主程序与攻击程序的独立性** ，要求很简单输入值只有一个 `ip` ，然后返回值是字符串类型的 `flag` ，为了减少不稳定性，最后又进行了一次类型转换。

为方便调试，单独运行此脚本需要单独交互输入攻击地址。



 


