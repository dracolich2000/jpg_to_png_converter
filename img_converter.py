import sys
import os
from PIL import Image


#take arguments from terminal
image_folder = sys.argv[1] #folder path/name from which you want to convert images
output_folder = sys.argv[2] #output folder name/path

if not os.path.exists(image_folder): #check whether image folder exists or not
    print('please enter valid folder name/path')
    sys.exit()

#check whether output folder exists or not. if not create one
if not os.path.exists(output_folder):
    os.mkdir(output_folder) #create output folder
    
png_list = [] 
conv_items = 0
#read images and convert them from 'jpg' to 'png'
for filename in os.listdir(image_folder):
    try:
        img = Image.open(f'{image_folder}{filename}')
    except PermissionError:
        continue
    clean_name = os.path.splitext(filename)[0] #get image name
    extension = os.path.splitext(filename)[1] #get image extension
    if extension == '.jpg':
        conv_img = img.convert('RGBA') #convert image from 'RGB' to 'RGBA'
        conv_img.save(f'{output_folder}{clean_name}.png', 'png')
        print('done!!!')
        conv_items += 1
    elif extension == '.png':
        print('image is already in png format!!!')
        png_list.append(filename)
    elif extension != '.jpg' or '.png':
        print('unsupported format!')

print(f'converted {conv_items} files')
png_files = len(png_list)

while True:
    resp = input(f'{png_files} files are in png format. do you want to save them in output folder ? (y/n)')
    if resp == 'y':
        for filename in png_list:
            img = Image.open(f'{image_folder}{filename}')
            img.save(f'{output_folder}{filename}', 'png')
            print('done!!!')
        sys.exit()    
    elif resp == 'n':
        sys.exit()
    else:
        print('please enter y/n.')   


