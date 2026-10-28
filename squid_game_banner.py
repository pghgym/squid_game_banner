import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Paths to your screenshots in OneDrive
path_watch = r"C:\Users\pghgy\OneDrive\Pictures\Screenshots\Screenshot 2026-10-28 164308.png"
path_tree  = r"C:\Users\pghgy\OneDrive\Pictures\Screenshots\Screenshot 2026-10-28 164054.png"

# Banner dimensions and timing setup
banner_size = 500
font_size = 48
scroll_speed = 4
frame_delay = 33            # ~30 fps
freeze_seconds = 2.0        # Seconds each screenshot stays on screen
freeze_frames_count = int(freeze_seconds * 1000 / frame_delay)

try:
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    font = ImageFont.load_default()

def create_banner_frames(text, bg_color, text_color):
    dummy = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    y_offset = (banner_size - text_height) // 2

    frames = []
    for shift in range(0, text_width, scroll_speed):
        frame = Image.new("RGB", (banner_size, banner_size), bg_color)
        d = ImageDraw.Draw(frame)
        x = -shift
        while x < banner_size:
            d.text((x, y_offset), text, fill=text_color, font=font)
            x += text_width
        frames.append(frame)
    return frames

def load_and_fit_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    img = Image.open(path).convert("RGB")
    return ImageOps.fit(img, (banner_size, banner_size), Image.Resampling.LANCZOS)

# 1. Green Light sequence
print("1/4: Rendering Green Light banner...")
green_frames = create_banner_frames(
    text="  Green Light | Luz Verde | ",
    bg_color=(34, 139, 34),
    text_color=(255, 255, 255)
)

# 2. Facing tree image (after Green Light)
print("2/4: Processing tree screenshot...")
tree_img = load_and_fit_image(path_tree)
tree_frames = [tree_img] * freeze_frames_count

# 3. Red Light sequence
print("3/4: Rendering Red Light banner...")
red_frames = create_banner_frames(
    text="  Red Light | Luz Roja | ",
    bg_color=(255, 0, 0),
    text_color=(255, 255, 255)
)

# 4. Facing players / doll watching (after Red Light)
print("4/4: Processing doll watching screenshot...")
watch_img = load_and_fit_image(path_watch)
watch_frames = [watch_img] * freeze_frames_count

# Combine into one complete sequence
full_sequence = green_frames + tree_frames + red_frames + watch_frames

print("Saving squid_game_cycle.gif...")
full_sequence[0].save(
    "squid_game_cycle.gif",
    save_all=True,
    append_images=full_sequence[1:],
    duration=frame_delay,
    loop=0
)

print("Finished! Saved squid_game_cycle.gif successfully.")