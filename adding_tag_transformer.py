import os
from PIL import Image
import pandas as pd
from transformers import AutoProcessor, AutoModelForImageTextToText
import torch

# Load the model and processor
processor = AutoProcessor.from_pretrained("microsoft/git-base")
model = AutoModelForImageTextToText.from_pretrained("microsoft/git-base")

# Folder with images and output CSV file
image_folder = "Extracted images"
output_csv = "git_image_captions.csv"
captions = []

# Loop through and caption each image
for file in sorted(os.listdir(image_folder)):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            image_path = os.path.join(image_folder, file)
            image = Image.open(image_path).convert("RGB")

            # Preprocess image and generate caption
            inputs = processor(images=image, return_tensors="pt")
            pixel_values = inputs.pixel_values

            generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
            caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

            captions.append((file, caption))
            print(f"{file} -> {caption}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

# Save to CSV
df = pd.DataFrame(captions, columns=["image", "caption"])
df.to_csv(output_csv, index=False)
print(f"\nCaptions saved to {output_csv}")
