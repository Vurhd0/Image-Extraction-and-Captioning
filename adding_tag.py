import os
import pandas as pd
import google.generativeai as genai
from PIL import Image

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyAHnmij-4td0qpDX0B4ywHgT3AFORKj7E0")  # Replace with your real API key

# Load Gemini vision model
model = genai.GenerativeModel('gemini-1.5-flash')

# Folder with images and output CSV path
image_folder = "Extracted images"
output_csv = "gemini_image_captions.csv"
captions = []

# Loop through images and generate captions
for file in sorted(os.listdir(image_folder)):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_folder, file)

        try:
            image = Image.open(image_path)
            prompt = "Describe this image. It is from a biology textbook, so focus on identifying what figure or diagram it might be."

            response = model.generate_content([prompt, image])
            caption = response.text.strip()

            captions.append((file, caption))
            print(f"{file} -> {caption}")
        
        except Exception as e:
            print(f"Error processing {file}: {e}")
            captions.append((file, "ERROR"))

# Save captions to CSV
df = pd.DataFrame(captions, columns=["image", "caption"])
df.to_csv(output_csv, index=False)
print(f"\nCaptions saved to {output_csv}")
