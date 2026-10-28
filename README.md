# Squid Game Banner Cycle

Animated looping GIF banners inspired by the iconic "Red Light, Green Light" sequence from *Squid Game*.

This repository provides two builds:
- **HD Version:** High-resolution ($500 \times 500$, ~30 FPS) for desktop, avatars, and web banners.
- **Badge / Wearable Version:** Highly optimized ($240 \times 240$, <1 MB, 64-color palette) designed for micro-displays and memory-constrained devices (e.g., E87X e-badge).

---

## Previews

| Build | Preview | Output Specs |
| :--- | :--- | :--- |
| **Badge (Low-Power / Small RAM)** | ![Badge Preview](squid_game_cycle_badge.gif) | 240×240, ~300 KB – 700 KB, 64 colors |
| **HD (Desktop / Web)** | ![HD Preview](squid_game_cycle_hd.gif) | 500×500, ~3 MB – 5 MB, smooth 30 FPS |

---

## Sequence Order

1. **Green Light Marquee** (`Green Light | Luz Verde |`) scrolling on forest green.
2. **Young-hee Doll facing the tree** (paused hold).
3. **Red Light Marquee** (`Red Light | Luz Roja |`) scrolling on bright red.
4. **Young-hee Doll scanning players** (paused hold).

---

## Requirements

- Python 3.x
- Pillow:
  ```bash
  pip install pillow```

---

## Usage

Ensure the screenshot assets are placed in the `assets/` folder:
- `assets/doll_tree.png`
- `assets/doll_watching.png`

### 1. Generate the Compressed Badge Version (<1 MB)
```bash
python compressed_badge_gif.py

```
*Outputs: `squid_game_cycle_badge.gif`*

### 2. Generate the High-Resolution HD Version
```bash
python squid_game_banner.py
```
echo *Outputs: `squid_game_cycle_hd.gif`*
) > README.md