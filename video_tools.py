from __future__ import annotations

import subprocess
import os
import shutil
from pathlib import Path
import tempfile

def clip_video(input_path: str, start: float, end: float, output_path: str) -> str:
    """input_path の動画から start 秒から end 秒までを切り出して output_path に保存します。"""
    # FFmpegを使って直接切り出し
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-ss", str(start),
        "-to", str(end),
        "-c", "copy",
        output_path
    ]
    subprocess.run(cmd, check=True)
    return output_path


def overlay_text(
    input_path: str,
    text: str,
    start: float,
    duration: float,
    output_path: str,
) -> str:
    """input_path の動画にテキストを重ねて output_path に保存します。"""

    # フォントパス
    font_path = "C\\:/Windows/Fonts/msgothic.ttc"

    # 直接テキスト指定のシンプルな方法（引用符でテキストを囲む）
    # エスケープ文字を追加
    escaped_text = text.replace(":", "\\:").replace("'", "\\'")

    # フィルター指定（クォーテーションの扱いに注意）
    vf = f'drawtext=text="{escaped_text}":fontfile={font_path}:fontcolor=black:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2'

    # 実行
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vf", vf,
        "-c:a", "copy",
        output_path
    ]

    subprocess.run(cmd, check=True)
    return output_path


def change_speed(input_path: str, factor: float, output_path: str) -> str:
    """factor 倍速で再生する動画を output_path に保存します。"""

    # FFmpegを使って直接速度変更
    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-filter:v", f"setpts={1/factor}*PTS",
        output_path
    ]

    subprocess.run(cmd, check=True)
    return output_path
