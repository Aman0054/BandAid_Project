# AI Band-Aid Overlay using OpenCV

This project demonstrates a simple **computer vision application** that detects a wound in an arm image and digitally places a band-aid on it. The system uses **Python and OpenCV** to identify the wound area and overlay a band-aid image so that it appears naturally placed.

The program processes multiple images, detects the wound region using color-based segmentation, and automatically applies a resized band-aid over the detected wound.

---

# 📌 Features

* Detects wound regions in arm images
* Automatically overlays a band-aid on the detected wound
* Uses **HSV color segmentation** for wound detection
* Resizes and positions the band-aid based on wound location
* Displays both **original and modified images**
* Saves processed images to an output folder
* Works with **multiple images in a loop**

---

# 🛠 Technologies Used

* **Python**
* **OpenCV**
* **NumPy**

These libraries are used for image processing, contour detection, and pixel manipulation.

---

# 📂 Project Structure

```
BandAid_Project/
│
├── bandaid.py
├── requirements.txt
│
├── images/
│   ├── arm1.jpg
│   ├── arm2.jpg
│   ├── arm3.jpg
│   └── bandaid.png
│
└── output/
```

**bandaid.py** → Main program for wound detection and band-aid overlay
**images/** → Contains input arm images and band-aid image
**output/** → Stores processed results

---

# ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/bandaid-overlay.git
```

2. Navigate to the project folder

```bash
cd bandaid-overlay
```

3. Install required dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the Python script:

```bash
python bandaid.py
```

The program will:

1. Load the arm images
2. Detect the wound region
3. Place a band-aid on the wound
4. Display the original and modified images
5. Save the results in the **output folder**

---

# 🧠 Approach

The system uses **HSV color segmentation** to detect red regions that correspond to wounds. After converting the image to HSV color space, a color mask is applied to isolate red pixels. Contours are then detected to identify the wound region. The largest contour is assumed to represent the wound.

A bounding rectangle is calculated around this region, and the center coordinates are used to position the band-aid image. The band-aid is resized proportionally to cover the wound and overlaid using **alpha blending**, which ensures smooth integration with the original image.

---

# ⚠️ Assumptions

* The wound area has visible **red coloration**.
* The **largest red region** corresponds to the wound.
* The arm orientation is relatively **horizontal**.

---

# 🚀 Future Improvements

* Use **deep learning models (YOLO)** for more accurate wound detection
* Detect **arm orientation** using Mediapipe
* Automatically adjust **band-aid rotation and placement**
* Improve blending for more realistic results

---

# 📷 Example Output

| Original Image | Band-Aid Applied          |
| -------------- | ------------------------- |
| Arm with wound | Arm with band-aid overlay |



