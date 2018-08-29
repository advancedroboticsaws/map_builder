"""
Step 1. Loading the jpg file.

step 2. resize (the x, y ratio) to correct size

step 3. Binary

step 4. save as a pgm file.

Each pixel should be  5 cm

Unit: cm
"""

import Image

# 5cm for one pixel
pixel_unit = 5


def map_builder(floor):
    file_name = floor + "F.jpg"

    im = Image.open(file_name)

    wide_pixel = im.size[0]
    height_pixel = im.size[1]

    if floor == "1":
        # Insert the ratio here.
        wide_ratio = 0.1660
        height_ratio = 0.1661
        threshold = 200
    else:
        # Insert the ratio here.
        wide_ratio = 0.3333
        height_ratio = 0.3337
        threshold = 200

    wide_pixel_output = int(round(wide_pixel * wide_ratio))
    height_pixel_output = int(round(height_pixel * height_ratio))

    im_size = im.resize((wide_pixel_output, height_pixel_output), Image.BILINEAR)

    im_size = im_size.point(lambda p: p > threshold and 255)
    im_size.show()

    save_name = "map" + floor + "_200.pgm"
    im_size.save(save_name)
    print(save_name + ":Done")


floor_list = ['0', '1', '2', '4']

for floor in floor_list:
    map_builder(floor)