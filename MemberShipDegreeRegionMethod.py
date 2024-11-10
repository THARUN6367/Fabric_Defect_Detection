import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("Images\Fabric1.jpg")
if image is None:
    print("Error: Image not found or unable to open.")
else:
    # Convert BGR to RGB and display
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.show()

    # Convert to HSV and display
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    plt.imshow(hsv)
    plt.show()

    # Extract V channel and display
    v = hsv[:, :, 2]
    plt.imshow(v, cmap="gray")
    plt.show()

    # Blur the V channel and display
    blr = cv2.blur(v, (5, 5))
    plt.imshow(blr, cmap="gray")
    plt.show()

    # Apply denoising and display
    dst_blr = cv2.fastNlMeansDenoising(blr, None, 10, 7, 21)
    plt.imshow(dst_blr, cmap="gray")
    plt.show()

    # Apply thresholding and display
    _, binary = cv2.threshold(dst_blr, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imshow(binary, cmap="gray")
    plt.show()

    # Define kernel
    kernel = np.ones((5, 5), np.uint8)

    # Dilation and display
    dilation = cv2.dilate(binary, kernel, iterations=1)
    plt.imshow(dilation, cmap="gray")
    plt.show()

    # Erosion and display
    erode = cv2.erode(binary, kernel, iterations=1)
    plt.imshow(erode, cmap="gray")
    plt.show()

    # Detect defects
    if (dilation == 0).sum() > 1:
        print("Bad Fabric")
        contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in contours:
            if cv2.contourArea(i) < 5000.0:
                cv2.drawContours(rgb, [i], -1, (0, 0, 255), 3)
    else:
        print("Good Fabric")

    # Show final result
    plt.imshow(rgb)
    plt.show()
