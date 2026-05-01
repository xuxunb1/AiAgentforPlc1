import json
import os

class ConfigChecker:
    def check(self, path):
        errors = []
        if not os.path.exists(path):
            errors.append("配置文件不存在")
            return errors

        try:
            with open(path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except:
            errors.append("配置文件JSON格式错误")
            return errors

        if not cfg.get("ip") or "." not in cfg.get("ip", ""):
            errors.append("IP地址格式错误 → 例：192.168.1.100")
        if not cfg.get("port") or int(cfg.get("port", 0)) <= 0:
            errors.append("端口无效 → Modbus TCP 推荐 502")
        if cfg.get("baudrate") not in [9600, 19200, 38400, 57600, 115200]:
            errors.append("波特率不标准 → 常用 9600 / 115200")
        return errors