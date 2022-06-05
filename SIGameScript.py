from pyscreenshot import grab
import keyboard

print('Ready!')

while True:
    if keyboard.read_key() in ("q", "Q", "й", "Й"):
        image = grab(childprocess=False)
        R, G, B = image.getpixel((960, 2))
        if R == 255 and G == 255 and B == 255:
            keyboard.send("space")

    if keyboard.read_key() in ("p", "P", "з", "З"):
        break

print('Finish')