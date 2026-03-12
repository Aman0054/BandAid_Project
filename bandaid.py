import cv2
import numpy as np
import os

image_folder = "images"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_list = ["arm1.jpg", "arm2.jpg", "arm3.jpg"]

bandaid = cv2.imread(os.path.join(image_folder, "bandaid.png"), cv2.IMREAD_UNCHANGED)

for img_name in image_list:

    img_path = os.path.join(image_folder, img_name)
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error loading {img_name}")
        continue

    original = image.copy()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        # Wound center
        center_x = x + w // 2
        center_y = y + h // 2

        # Increase bandaid size
        scale_w = int(w * 4)
        scale_h = int(h * 3)

        bandaid_resized = cv2.resize(bandaid, (scale_w, scale_h))

        bh, bw = bandaid_resized.shape[:2]

        # Center placement
        x1 = max(0, center_x - bw // 2)
        y1 = max(0, center_y - bh // 2)
        x2 = min(image.shape[1], x1 + bw)
        y2 = min(image.shape[0], y1 + bh)

        bandaid_crop = bandaid_resized[0:(y2-y1), 0:(x2-x1)]

        b, g, r, a = cv2.split(bandaid_crop)
        alpha = a / 255.0

        for i in range(3):
            image[y1:y2, x1:x2, i] = (
                alpha * bandaid_crop[:, :, i] +
                (1 - alpha) * image[y1:y2, x1:x2, i]
            )

    output_path = os.path.join(output_folder, f"output_{img_name}")
    cv2.imwrite(output_path, image)

    cv2.imshow(f"Original - {img_name}", original)
    cv2.imshow(f"Band-Aid Applied - {img_name}", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Processing Completed! Check output folder.")
