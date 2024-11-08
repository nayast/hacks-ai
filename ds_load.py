import os
from PIL import Image
import splitfolders

# путь к скачанному датасету
directory = r"dataset" 
# путь к уменьшеному (размер картинок) датасету 
directory2 = r"ds_small"                                                                    

# находим все папки в папке dataset
for content in os.walk(directory): 
    # для каждой из этих папок
    for folder in content[1]:
        # создаем папку с таким же названием в папке с уменьшенным датасетом
        os.mkdir(os.path.join(directory2,folder)) 
        # для каждого файла
        for name in os.listdir(os.path.join(directory,folder)):
            # открываем картинки
            img = Image.open(os.path.join(directory,folder,name))
          
            # изменяем их размер
            if img.height > 300 or img.width > 300: 
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(f'{directory2}\{folder}\{name}')

# путь к уменьшенному (размер картинок) датасету
input_folder = r'ds_small' 
# делим картинки на train (80%) и test (20%), кладем в папку ds_splited
splitfolders.ratio(input_folder, r'ds_splited', ratio=(0.8, 0, 0.2), seed=2, group_prefix = None) 
