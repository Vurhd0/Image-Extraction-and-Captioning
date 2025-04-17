import cv2
import os

input_folder = 'snapshots'
output_folder = 'cropped_figures'
os.makedirs(output_folder, exist_ok=True)

def crop_figures_from_image(image_path, save_prefix):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use thresholding to isolate image regions
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)


    # Find contours (likely figure boundaries)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Heuristics: Filter small blobs
        if w > 200 and h > 200 and w/h <4 and h/w < 6:
            cropped = image[y:y+h, x:x+w]
            out_path = os.path.join(output_folder, f"{save_prefix}_fig{count+1}.png")
            cv2.imwrite(out_path, cropped)
            count += 1

    print(f"{count} figures cropped from {image_path}")

# Loop over rendered pages
for file in sorted(os.listdir(input_folder)):
    if file.endswith(".png"):
        page_num = os.path.splitext(file)[0]
        crop_figures_from_image(os.path.join(input_folder, file), page_num)
