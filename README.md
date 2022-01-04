# Radius Measurement Of Parts With Circular Geometry


The aim of this program is to make diameter measurements of parts with circular geometry using 5 different methods currently available in the literature. These methods are given below.

   1 - Pixel Counting

   2 - Circle Fitting

   3 - Canny/Devernay Subpixel Edge Detection Method [1]

   4 - Accurate Subpixel Edge Location Method [2]

   5 - Zernike-Moments Based Edge Detection With Sub-Pixel Accuracy [3]

In the Pixel Counting Method, the pixels of the largest connected component on the image are counted and the diameter of the part is obtained from the formula A=π.(r^2).

In the Circle Fitting Method, the edge coordinates of the part are found and the diameter of the circle most suitable for these coordinates is obtained. In fact, the same principle was used in the other three methods, but in this method, pixel-sized operations were performed.

In the Canny/Devernay Subpixel Edge Detection Method, a software that can make very powerful and sensitive measurements in subpixel level is used.
(https://www.ipol.im/pub/art/2017/216/)

The Accurate Subpixel Edge Location Method has been used with the help of a library called subpixel-edges, which is currently available on PyPI.
(https://pypi.org/project/subpixel-edges/ and https://www.mathworks.com/matlabcentral/fileexchange/48908-accurate-subpixel-edge-location)

Zernike-Moments Based Edge Detection With Sub-Pixel Accuracy Method was created with the help of a repository available on GitHub.
(https://github.com/tobiasosswald/zernike-detection)

.

.


------ USER GUIDE --------------------------------------------------------------------------------------------

Python Version: 3.7.0

![image](https://user-images.githubusercontent.com/52501795/148018520-1db6ae1c-0174-46a2-a8ca-a84bf28ff4e5.png)

First, the libraries.py file can be run to ensure that the necessary libraries for the program are installed and the program can run in the same code.


![image](https://user-images.githubusercontent.com/52501795/148018218-7eb48b1e-042b-449e-aeb0-a8300dc1c05d.png)

• In the "Preparations" tab, initial settings will be made so that the program can work properly.

• In the first step, click on the "Excel Files Folder" button and select the folder where the result files of the measurements will be located with .csv extension.

• Then click the "Snapshots Folder" button and select the folder where the images for which diameter values are to be obtained are located.

• It provides configuration of folders to be created for Devernay Method and Accurate Subpixel Edge Detection (Matlab Code) Method via "Create Environment" button. These files will be stored in the folder where the Excel files are located.

• The "RESET" button should be used to clear the cookies of previous operations.


![image](https://user-images.githubusercontent.com/52501795/148019335-860ea68e-d719-491a-bda8-3a4fdbd7e429.png)



• Then, by coming to the "Methods" tab, any desired method can perform diameter measurements by simply pressing the relevant button.

• Each measurement method has its own separate parameters and they can be easily adjusted via the UI.

![image](https://user-images.githubusercontent.com/52501795/148019570-9d070889-cd98-4317-9b83-0b12f60e9616.png)


The diameter values obtained after pressing the relevant button are stored in the folder selected for excel files.

.

.

[1] Grompone von Gioi, R y Randall, G. "A sub-pixel edge detector: an implementation of the Canny/Devernay Algorithm". Image Processing On Line. 2017, vol. 7, pp. 347–372.

[2] Agustín Trujillo-Pino, Karl Krissian, Miguel Alemán-Flores, Daniel Santana-Cedrés "Accurate Subpixel Edge Location Based On Partial Area Effect". Image and Vision Computing. 2013, Volume 31, Issue 1, Pages 72-90.

[3] T.Osswald "Zenike Moments Based Edge Detection User Manual", 2021
