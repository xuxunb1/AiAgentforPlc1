import random

class CommMonitor
    def simulate_monitor(self)
        # 模拟ModbusTCP串口通信检测
        errors = []
        check_items = [
            TCP 端口未开放 → 开启 502 端口,
            从站无响应 → 检查设备地址,
            数据丢包 → 降低通信速率,
            网络延迟过高 → 优化局域网
        ]
        # 随机模拟2个通信问题（真实项目可对接真实网卡）
        errors = random.sample(check_items, 2)
        return errors