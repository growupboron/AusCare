import os.path
from demo_opts import get_device
from PIL import Image


def main():
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'images', 'pi_logo.png'))
    logo = Image.open(img_path).convert("RGBA")
    fff = Image.new(logo.mode, logo.size, (255,) * 4)

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)

    while True:
      rot = logo.rotate(angle, resample=Image.BILINEAR)
      img = Image.composite(rot, fff, rot)
      background.paste(img, posn)
      device.display(background.convert(device.mode))


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
      pass