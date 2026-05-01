#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 驱动上位机自动化调试 Agent
上位机开发 + PLC 智能诊断 + 自动修复 + 报告生成
GitHub: https://github.com/xxx/AI-PLC-Host-Commissioning-Agent
"""

import os
import sys
from datetime import datetime

from debug_agent.log_parser import LogParser
from debug_agent.config_checker import ConfigChecker
from debug_agent.fix_generator import FixGenerator
from debug_agent.report_export import ReportExporter
from debug_agent.comm_monitor import CommMonitor

def print_logo():
    logo = """
    ==============================================
       AI 上位机自动化调试 Agent · v2.0
       智能诊断 | 日志解析 | 配置校验 | 自动修复
    ==============================================
    """
    print(logo)

def main():
    print_logo()
    print(f"启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # 初始化模块
    log_parser = LogParser()
    config_checker = ConfigChecker()
    fix_generator = FixGenerator()
    report_exporter = ReportExporter()
    comm_monitor = CommMonitor()

    # 1. 读取日志
    print("[1] 读取设备日志...")
    if not os.path.exists("test_device.log"):
        print("错误：未找到设备日志文件")
        return
    with open("test_device.log", "r", encoding="utf-8") as f:
        log_content = f.read()

    # 2. 解析日志
    log_errors = log_parser.parse(log_content)
    print(f"日志解析完成，发现 {len(log_errors)} 个问题")

    # 3. 校验配置
    print("[2] 校验上位机配置文件...")
    config_errors = config_checker.check("config.json")
    print(f"配置校验完成，发现 {len(config_errors)} 个问题")

    # 4. 通信状态检测
    print("[3] 检测通信状态...")
    comm_errors = comm_monitor.simulate_monitor()
    print(f"通信检测完成，发现 {len(comm_errors)} 个问题")

    # 5. 汇总所有错误
    all_errors = log_errors + config_errors + comm_errors

    if len(all_errors) == 0:
        print("\n✅ 系统正常，无异常！")
        return

    # 6. 生成修复方案
    print(f"\n[4] 共发现 {len(all_errors)} 个异常，生成修复脚本...")
    fix_script = fix_generator.generate(all_errors)

    # 7. 导出调试报告
    report_path = report_exporter.export(log_content, all_errors, fix_script)

    # 8. 输出结果
    print("\n" + "="*60)
    print("📄 修复脚本：")
    print(fix_script)
    print("="*60)
    print(f"✅ 调试报告已保存至：{report_path}")
    print("\n🎉 AI 上位机调试完成！")

if __name__ == "__main__":
    main()