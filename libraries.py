import os

answer = str(input("Did you install libraries? (Y/n)        "))

if answer.lower() == "n":
    os.system("python -m pip install --upgrade pip")
    os.system("pip install numpy")
    os.system("pip install matplotlib")
    os.system("pip install PyQt5")
    os.system("pip install pandas")
    os.system("pip install opencv-python")
    os.system("pip install opencv-contrib-python")
    os.system("pip install subpixel-edges")
    os.system("pip install mplot3d-dragger")
    os.system("pip install scipy")
    os.system("pip install elementpath")
    os.system("pip install tqdm")
    os.system("pip install imageio")
    os.system("pip install -U scikit-learn")
    os.system("pip install sklearn")
    os.system("pip install ipywidgets")
    os.system("pip install pytest-warnings")
    os.system("pip install DateTime")

else:
    print("\n")

for i in range(100):    
    answer2 = str(input("Please enter 'r' to run program.       "))

    if answer2.lower() == "r":
        os.system("python gui_2.py")


    if answer2.lower() == "r":
        break
