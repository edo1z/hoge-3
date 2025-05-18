from __future__ import annotations

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx import all as vfx


def clip_video(input_path: str, start: float, end: float, output_path: str) -> str:
    """input_path の動画から start 秒から end 秒までを切り出して output_path に保存します。"""
    with VideoFileClip(input_path) as clip:
        subclip = clip.subclip(start, end)
        subclip.write_videofile(output_path)
    return output_path


def overlay_text(
    input_path: str,
    text: str,
    start: float,
    duration: float,
    output_path: str,
) -> str:
    """input_path の動画にテキストを重ねて output_path に保存します。"""
    with VideoFileClip(input_path) as clip:
        txt_clip = TextClip(text, fontsize=24, color="white")
        txt_clip = txt_clip.set_start(start).set_duration(duration)
        txt_clip = txt_clip.set_position("center")
        result = CompositeVideoClip([clip, txt_clip])
        result.write_videofile(output_path)
    return output_path


def change_speed(input_path: str, factor: float, output_path: str) -> str:
    """factor 倍速で再生する動画を output_path に保存します。"""
    with VideoFileClip(input_path) as clip:
        new_clip = clip.fx(vfx.speedx, factor)
        new_clip.write_videofile(output_path)
    return output_path
