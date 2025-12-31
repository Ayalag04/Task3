import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  


image_path = "download.jpg"  
img = Image.open(image_path)


img_np = np.array(img)

red = img_np[:, :, 0]
green = img_np[:, :, 1]
blue = img_np[:, :, 2]

r_hist, _ = np.histogram(red, bins=256, range=(0, 256))
g_hist, _ = np.histogram(green, bins=256, range=(0, 256))
b_hist, _ = np.histogram(blue, bins=256, range=(0, 256))

plt.figure(figsize=(10,4))
plt.plot(r_hist, color='red', label='Red')
plt.plot(g_hist, color='green', label='Green')
plt.plot(b_hist, color='blue', label='Blue')
plt.title("RGB Histogram")
plt.xlabel("Color Value (0-255)")
plt.ylabel("Pixel Count")
plt.legend()
plt.show()
