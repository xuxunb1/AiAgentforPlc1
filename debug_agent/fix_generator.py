from datetime import datetime

class FixGenerator:
    def generate(self, errors):
        txt = "=" * 50 + "\n"
        txt += "          AI 上位机自动修复脚本\n"
        txt += f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        txt += "=" * 50 + "\n\n"

        for idx, err in enumerate(errors, 1):
            txt += f"【步骤 {idx}】{err}\n"

        txt += "\n" + "=" * 50 + "\n"
        txt += "执行说明：按步骤从上到下依次修复，完成后重启通信\n"
        txt += "=" * 50
        return txt