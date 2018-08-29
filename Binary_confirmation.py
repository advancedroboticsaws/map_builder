import Image


name = 'map0_amcl'
file_name = name + '.pgm'

im = Image.open(file_name)


threshold = 100

im = im.point(lambda p: p > threshold and 255)

im.show()

im.save(name+'.pgm')
print("Done")