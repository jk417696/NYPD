import os
import random
import csv

directory = "/home/students/mat/j/jk417696/PycharmProjects/homework_21XI/days/"

folders = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
subfolders = ["morning", "evening"]
model = ["A", "B", "C"]

for i in range(7):
    path = os.path.join(directory, folders[i])
    os.makedirs(path, exist_ok=True)
    for j in range(2):
        path_sub = os.path.join(path, subfolders[j])
        os.makedirs(path_sub, exist_ok=True)
        filepath = os.path.join(path_sub, "Solutions.csv")
        f = open(filepath, "w+")
        f.write(" Model; Output value; Time of computation; \n")
        random_model = model[random.randint(0, 2)]
        random_out = str(random.randint(0, 1000))
        random_toc = str(random.randint(0, 1000))
        f.write(random_model+"; "+random_out+"; "+random_toc+"s")
        f.close()

sum = 0
for fold in os.listdir(directory):
    fold_directory = os.path.join(directory, fold)
    for subfold in os.listdir(fold_directory):
        sub_directory = os.path.join(fold_directory, subfold)
        for files in os.listdir(sub_directory):
            file_path = os.path.join(sub_directory, files)
            with open(file_path,"r") as csv_file:
                csv_reader = list(csv.reader(csv_file, delimiter=";"))
                if csv_reader[1][0] == "A":
                    sum+=int(csv_reader[1][2][:-1])
print("Total time of computation for model A: "+str(sum)+"s")



