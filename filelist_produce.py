import os
from os.path import dirname, basename
from os.path import dirname
import random
path = "lrs2_preprocessed"
filelist = []

for root in os.listdir(path):
    file_path = os.path.join(path, root)
    for video in os.listdir(file_path):
        filelist.append(root+ "/"+ video)
print("Number of pre-processed video files found:", len(filelist))
filelist_test_nums = int(len(filelist) * (5 / 100))

filelist_val_nums = int(len(filelist) * (5 / 100))

if filelist_test_nums > 1:
        filelist_test = random.sample(filelist, filelist_test_nums)
else:
        filelist_test = random.sample(filelist, 2)
filelist_test_not = list(set(filelist) ^ set(filelist_test))
if filelist_val_nums > 1:
        filelist_val = random.sample(filelist_test_not, filelist_val_nums)
else:
        filelist_val = random.sample(filelist_test_not, 2)
filelist_train = list(set(filelist_test_not) ^ set(filelist_val))

def filelist_save(fname, filelist):

    # write filelist content to a CSV file
    with open(fname + ".txt", 'w+') as file:
       for item in filelist:
           file.write(item + '\n')

    file.close()

    return fname + ".txt"

rslt = filelist_save("filelists/" + "train", filelist_train)
print("Filelists for train (with", len(filelist_train), "videos) written to disk:", rslt)
rslt = filelist_save("filelists/" + "val", filelist_val)
print("Filelists for val (with", len(filelist_val), "videos) written to disk:", rslt)
rslt = filelist_save("filelists/" + "test", filelist_test)
print("Filelists for test (with", len(filelist_test), "videos) written to disk:", rslt)

print("... done. Bye.")