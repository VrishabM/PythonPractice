def find_extension(filename):
    return filename.split(".")[-1]


filename = input("Enter File name : ")
print("Extension of ", filename, " -> ", find_extension(filename))