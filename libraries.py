import os

answer = str(input("Did you install libraries? (Y/n)        "))

if answer.lower() == "n":
    os.system("pip3 install opencv-python")
    os.system("pip3 install opencv-contrib-python")
    os.system("pip3 install numpy")
    os.system("pip3 install pandas")
    os.system("pip3 install matplotlib")
    os.system("pip3 install subpixel-edges")
    os.system("pip3 install PyQt5")

else:
    print("\n")

for i in range(100):    
    answer2 = str(input("Please enter 'r' to run program.       "))

    if answer2.lower() == "r":
        os.system("python gui_2.py")


    if answer2.lower() == "r":
        break