import os
from PIL import Image

directory = r"dataset"
directory2 = r"ds_small"

for content in os.walk(directory):
    for folder in content[1]:
        os.mkdir(os.path.join(directory2,folder))
        for name in os.listdir(os.path.join(directory,folder)):
            img = Image.open(os.path.join(directory,folder,name))

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(f'{directory2}\{folder}\{name}')
