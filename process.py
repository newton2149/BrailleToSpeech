import os
import shutil

raw_data = './raw_data/Braille Dataset'
dst_path = './'
test_percent = 10
index = int(round(100/test_percent))
s = 1

parent_test_dir = './dataset/test'
parent_train_dir = './dataset/train'

for i in range(97,123):
    path_test = os.path.join(parent_test_dir,chr(i))
    path_train = os.path.join(parent_train_dir,chr(i))
    os.mkdir(path_train)
    os.mkdir(path_test)


for file_name in os.listdir(raw_data)[0:-int(len(os.listdir(raw_data))*0.2)]:
    print(file_name)
    source = f'{raw_data}/{file_name}'
    destination = f'{parent_train_dir}/{file_name[0]}/{file_name}'
    # move only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('Moved:', file_name)

for file_name in os.listdir(raw_data)[int(len(os.listdir(raw_data))*0.2):-1]:
    print(file_name)
    source = f'{raw_data}/{file_name}'
    destination = f'{parent_test_dir}/{file_name[0]}/{file_name}'
    # move only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('Moved:', file_name)