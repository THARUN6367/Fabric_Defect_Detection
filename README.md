This project uses OpenCV and `matplotlib` to detect fabric defects by processing an input image of fabric and classifying it as either "Good" or "Bad." 
The script begins by loading the image from an `Images` directory and converting it to RGB and HSV color spaces. 
The V (brightness) channel from the HSV image is used for further analysis, where it is blurred to reduce noise, 
followed by denoising with Non-Local Means Denoising. Otsu's thresholding is then applied to create a binary image that highlights potential defects. 
Morphological transformations, including dilation and erosion, are used to enhance defect visibility. 
If a significant number of black pixels are detected in the binary image, the fabric is labeled "Bad," and contours of detected defects are drawn in red on the original image. 
If not, the fabric is considered "Good." The script displays images of each processing step, allowing for a visual understanding of the defect detection process. 
To run this project, install the required libraries (`opencv-python`, `numpy`, and `matplotlib`),
place the fabric image in an `Images` folder, and execute the script to view results.
