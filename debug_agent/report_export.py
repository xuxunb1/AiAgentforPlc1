import os
from datetime import datetime

class ReportExporter:
    def export(self, log, errors, script):
        folder = "debug_reports"
        if not os.path.exists(folder):
            os.mkdir(folder)

        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = os.path.join(folder, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write("=== AI 上位机调试报告 ===\n")
            f.write(f"时间: {datetime.now()}\n\n")
            f.write("【日志片段】\n")
            f.write(log[:500] + "\n\n")
            f.write("【诊断问题】\n")
            for i, e in enumerate(errors, 1):
                f.write(f"{i}. {e}\n")
            f.write("\n【修复脚本】\n")
            f.write(script)
        return path