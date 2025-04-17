# Image-Extraction-and-Captioning system


## Overview

This project aims to create a system for extracting and tagging images from NCERT textbooks, where each chapter is provided in PDF format. The system involves three main steps:

1. **Snapshot**: Captures the visual content of the PDF.
2. **Image Extraction**: Extracts the images, excluding non-essential graphics such as borders, watermarks, and page numbers.
3. **Image Tagging**: Generates relevant, descriptive tags or captions for each image extracted.

The system is designed to be modular, easy to understand, and adaptable to various educational PDFs.

## Workflow

### Step 1: Capture Snapshot of PDF
In this step, the system scans the provided PDF file to identify the locations and dimensions of the images within each page. This step helps us ensure that we are capturing only relevant content and allows us to work with the images later on.

- We start by loading the PDF and using **PyMuPDF** to extract visual content.
- **OpenCV** or **Pillow** might be used to process images if any clean-up is required before tagging.

### Step 2: Extract Images from PDF
Once the snapshot of the document has been captured, the next step involves extracting the images from the PDF. 

- The system uses **PyMuPDF** to pull out the images embedded within the document.
- It excludes any unnecessary graphical elements (e.g., watermarks, page borders) by analyzing the content type.
- Each image is cropped to remove excessive whitespace, focusing on the meaningful visual content.

### Step 3: Image Tagging
After extracting the relevant images, the system generates descriptive tags or captions for each image. This can involve utilizing pre-trained **LLMs** or external APIs for context-aware caption generation.

- Tags are generated based on the image content, such as **"photosynthesis"**, **"human skeleton"**, **"map of India"**, and so on.
- These captions or tags are saved alongside the images, and a **metadata file** (either in JSON or CSV format) is generated to link each image to its corresponding tags.

## Libraries and Tools Used

- **PyMuPDF**: Extracts images and content from the PDF.
- **OpenCV** & **Pillow**: For image processing tasks like cropping and cleaning.
- **Transformers (Hugging Face)**: For generating captions or tags using LLMs.
- **Requests**: For making API calls to external services for image captioning.

## Step-by-Step Guide

### Step 1: Image Snapshot
1. **Prepare your PDF**: Place your NCERT textbook PDF in the root folder of the project.
2. **Capture Snapshot**: Run the script to extract a snapshot of the PDF content. This step will prepare the document for the next phase.

   ```bash
   python snapshot_extractor.py your_pdf_file.pdf

