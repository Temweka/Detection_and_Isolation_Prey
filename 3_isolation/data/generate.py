import os

image_files = []
os.chdir(os.path.join("data", "MOVI0006"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        image_files.append("data/MOVI0006/" + filename)
os.chdir("..")
with open("MOVI0006.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")