from PIL import Image
import sys

# We follow the memory map details described here:
# https://learn.sparkfun.com/tutorials/microview-hookup-guide/oled-memory-map
# to implement our image to array conversion

def bmp_to_oled_array(bmp_filename):
    # input image can be any file format 
    image = Image.open(bmp_filename)
    # convert to monochrome
    image = image.convert("1")
    # resize to display dimensions as needed
    if image.size != (64, 48):
        image = image.resize((64,48))
    # access the image as if it were a 64x48 grid of pixels
    pixels = image.load()

    # Convert to OLED memory format
    memory = []
    for y in range(0, 48, 8):
        for x in range(64):
            byte_val = 0
            for bit in range(8):
                if y+bit < 48:
                    pixel = pixels[x, y+bit]
                    if pixel == 0:  #Assume C code has COLOR=BLACK, set the bit if 0
                        byte_val |= 1 << bit
            memory.append(byte_val)

    return memory

def main():
    filename = sys.argv[1]
    memory = bmp_to_oled_array(filename)
    c_array = ", ".join([f"0x{byte:02x}" for byte in memory])

    # Print the C array
    print(f"static uint8_t image_data[] = {{{c_array}}};")

if __name__ == "__main__":
    main()

