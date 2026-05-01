import re

class LogParser:
    def __init__(self):
        self.patterns = {
            r"timeout": "Modbus TCP 连接超时 → 检查IP/端口/防火墙",
            r"invalid crc": "CRC 校验错误 → 检查接线/波特率/干扰",
            r"device offline": "设备离线 → 检查电源/网口/PLC状态",
            r"wrong register": "寄存器地址错误 → 核对设备地址表",
            r"baudrate mismatch": "波特率不匹配 → 统一设置 9600/8/N/1",
            r"connection refused": "连接被拒绝 → PLC未运行或端口被占用",
            r"read error": "数据读取失败 → 检查从站地址与通信线路",
            r"write error": "数据写入失败 → 权限或寄存器保护"
        }

    def parse(self, content):
        errors = []
        for pattern, tip in self.patterns.items():
            if re.search(pattern, content, re.I):
                errors.append(tip)
        return list(set(errors))