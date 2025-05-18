import numpy as np
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import VideoClip
from PIL import Image, ImageDraw

WIDTH, HEIGHT = 640, 480
DURATION = 20  # seconds
FPS = 24


def make_frame(t: float):
    """Generate a frame with moving square and circle."""
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Red square moves left to right
    square_size = 50
    x_pos = int((WIDTH + square_size) * t / DURATION) - square_size
    y_pos = HEIGHT // 3
    draw.rectangle([x_pos, y_pos, x_pos + square_size, y_pos + square_size], fill=(255, 0, 0))

    # Blue circle moves right to left
    circle_radius = 25
    x_c = int(WIDTH - (WIDTH + circle_radius * 2) * t / DURATION)
    y_c = HEIGHT * 2 // 3
    draw.ellipse([x_c - circle_radius, y_c - circle_radius,
                  x_c + circle_radius, y_c + circle_radius], fill=(0, 0, 255))

    return np.array(img)


def main() -> None:
    clip = VideoClip(make_frame, duration=DURATION)
    clip.write_videofile("shapes.mp4", fps=FPS)


if __name__ == "__main__":
    main()
