import cv2
import matplotlib.pyplot as plt

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)
max_marker_id = 100

marker_size = 200  # Marker size in pixels
num_rows, num_cols = 5, 5
pdf_file = "aruco_markers.pdf"  

fig, axes = plt.subplots(num_rows, num_cols, figsize=(8, 6))

for row in range(num_rows):
    for col in range(num_cols):
        marker_id = row * num_cols + col
        if marker_id <= max_marker_id:
            marker_img = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)
            axes[row, col].imshow(marker_img, cmap='gray')
            axes[row, col].axis('off')

fig.tight_layout()
plt.savefig(pdf_file, format='pdf')
print(f"ArUco markers saved to {pdf_file}")
