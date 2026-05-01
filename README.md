# AI-PLC-Host-Commissioning-Agent
AI 驱动的工业上位机自动化调试 Agent

## 项目介绍
这是面向**工业上位机开发、PLC通信调试、自动化产线维护**的智能诊断工具。
通过AI解析设备日志、校验配置、监控通信状态，自动定位故障并生成修复方案。

## 核心功能
✅ 智能日志异常识别  
✅ 上位机配置文件自动校验  
✅ Modbus TCP/RTU 通信监控  
✅ 一键生成可执行修复脚本  
✅ 自动导出标准化调试报告  
✅ 支持 PLC / 传感器 / 伺服控制器  

## 技术栈
- Python 3.x
- 工业通信协议：Modbus TCP / RTU
- 正则异常匹配
- 自动化诊断引擎

## 运行方式
### Windows
双击 run.bat
或接入项目中
### 命令行
```bash
python main.py