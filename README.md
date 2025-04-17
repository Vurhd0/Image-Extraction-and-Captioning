# Image Extraction and Tagging System

This repository provides an automated system to **extract images** and **generate relevant tags** for NCERT textbook chapters provided in PDF format. The system consists of the following key steps:

1. **Snapshot Creation**: Capture snapshots of each page in the PDF document.
2. **Image Extraction (Contour-based)**: Extract images from the PDF using a contour-based approach using openCV.
3. **Tagging**: Generate descriptive tags for the extracted images based on their content using Huggingface Blip model / google gemini api key.

These steps are all automated by the `run.sh` script, which runs the necessary scripts in sequence.

## Workflow Overview

The process follows this order:

1. **Step 1: Snapshot Creation**  
   The first step involves creating a snapshot of each page in the provided PDF. This allows the system to capture and isolate the relevant images from the page content.

2. **Step 2: Image Extraction Using Contour-based Approach**  
   After creating the snapshots, the next step is to use a contour-based approach to detect and extract the images. This technique helps isolate the images and removes unnecessary elements such as watermarks, page borders, and patterns.

3. **Step 3: Tagging the Extracted Images**  
   Once the images are extracted, the system generates descriptive tags for each image. These tags help categorize the images and can reflect their content, such as "photosynthesis," "human skeleton," "map of India," etc.

4. **Step 4: Automation with `run.sh`**  
   The `run.sh` script automates the entire process. It calls each Python script in the correct order—capturing snapshots, extracting images, and adding tags.

## Getting Started

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.x
- Required libraries: PyMuPDF, OpenCV, Pillow, transformers, pandas,google-generativeai

Installing of necessary libraries is being handaled by run.sh you just need to add the library name in requirements.txt file

### To run and get output of tagged images with tags in csv file


