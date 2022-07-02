#This program allows you to print files with specified extensions and their locations to .txt files.
#First, you must type a folder path for your program's folder path or you can type it later in if statements. Check the explanations.


import os

os.chdir("Where do you want your program's folder path to be?") #Type a folder path if you want to change your program's folder path.
#If you change your program's folder path here, you don't need to activate other "os.chdir" statements. Because files will be created where you typed the stament above.
#If you don't want to change your program's folder path here, you must change it other "os.chdir" statements. Because files will be created where you typed at those statements.


for folder_path, folder_names, file_names in os.walk("Where do you want to be searched"): #Type a folder path i.e. "C:/Users/user/Desktop". It will search all folders in Desktop
    for names in file_names:
        if names.endswith(".pdf"): #You can change extension which you want to be searched by the program.
            #os.chdir("Type a folder path to create your file there") #Activate this line if you want to create your pdf file in a spesific location.
            file = open(".pdf files.txt", "a", encoding="utf-8") #Type your file's name here with .txt extension.
            file.write("\nFolder path: ")
            file.write(folder_path)
            file.write("\n")
            for a in file_names:
                if a.endswith(".pdf"):
                    file.write("File name: ")
                    file.write(a)
                    file.write("\n")
            break

    for names in file_names:
        if names.endswith(".txt"): #You can change extension which you want to be searched by the program.
            #os.chdir("Type a folder path to create your file there") #Activate this line if you want to create your txt file in a spesific location.
            file = open(".txt files.txt", "a", encoding="utf-8") #Type your file's name here with .txt extension.
            file.write("\nFolder path: ")
            file.write(folder_path)
            file.write("\n")
            for a in file_names:
                if a.endswith(".txt"):
                    file.write("File name: ")
                    file.write(a)
                    file.write("\n")
            break

    for names in file_names:
        if names.endswith(".mp4"): #You can change extension which you want to be searched by the program.
            #os.chdir("Type a folder path to create your file there") #Activate this line if you want to create your mp4 file in a spesific location.
            file = open(".mp4 files.txt", "a", encoding="utf-8") #Type your file's name here with .txt extension.
            file.write("\nFolder path: ")
            file.write(folder_path)
            file.write("\n")
            for a in file_names:
                if a.endswith(".mp4"):
                    file.write("File name: ")
                    file.write(a)
                    file.write("\n")
            break