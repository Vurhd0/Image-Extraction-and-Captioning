import fitz  # PyMuPDF
import os

pdf_path = 'chapter_4.pdf'
output_folder = 'snapshots'
os.makedirs(output_folder, exist_ok=True)

pdf = fitz.open(pdf_path)

for i in range(len(pdf)):
    page = pdf[i]
    pix = page.get_pixmap(dpi=300)  # High-res snapshot
    image_path = os.path.join(output_folder, f"page_{i+1}.png")
    pix.save(image_path)

print("PDF pages saved as high-resolution images.")
