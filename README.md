# Image Extraction and Tagging System

This repository provides an automated system to **extract images** and **generate relevant tags** for NCERT textbook chapters provided in PDF format. The system consists of the following key steps:

1. **Snapshot Creation**: Capture snapshots of each page in the PDF document.
2. **Image Extraction (Contour-based)**: Extract images from the PDF using a contour-based approach using openCV.
3. **Tagging**: Generate descriptive tags for the extracted images based on their content using Huggingface Blip model / google gemini api key.

These steps are all automated by the `run.sh` script, which runs the necessary scripts in sequence.

## Files description

1.**requirements.text**
  It contains name of all the required libraries required for system

2. **snap.py**
   This python script generates snapshots of each page of pdf as image and store them in snapshots folder

3 **ext.py**
   This script uses opencv to extract images out of the snapshots and store them in Extracted images folder

4 **adding_tag.py**
   This script add tags to the images using the google gemini api and stores them in csv file gemini_cations.csv

5 **adding_tag_transformer.py**
   This code is an alternative code for the gemini api key tag generation as it fails on some images due to free tier not being available . Here we use the microsoft git image captioning model to caption the 
   images
6 **run.sh**
   This is the shell script to run the whole system . you just need to place the files in same folder with pdf and can run all scripts using the run.sh (explained below)

   
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

## Image Tagging Using Google API and HuggingFace Gemini Model

### Overview
In this project, the image tagging process is carried out using the **Google API Key** and the **HuggingFace Microsoft Git Image Captioning Model**. However, due to limitations in the free version of the Google API, I encountered issues while trying to tag all the images. Specifically, the Google API free tier does not allow processing an unlimited number of images, which caused some of the captions to fail.

To work around this limitation, I leveraged the **Microsoft'S Git Captioning Model** available on HuggingFace for the image captioning task. This model serves as an alternative as the Google API is unable to process certain images due to the free-tier restrictions.

### Challenges with the Google API
The Google API for image captioning is powerful, but the free version has certain usage limits, including restrictions on the number of images that can be captioned within a specific time period or quota. As a result, some of the images failed to get tagged, leading to errors in the captions. These errors are typically a result of API restrictions that prevent further captioning after reaching the limit.

### Solution: HuggingFace Gemini Model
To address the issue of incomplete image tagging, I integrated the **Gemini Image Captioning Model** available on **HuggingFace**. The model provides an alternative method for generating captions when the Google API is unavailable or when the quota is exhausted.

While the HuggingFace model does not always provide captions with the same level of accuracy or context as the Google API, it offers a practical solution for tagging the images . As a result, some images may have captions that are less descriptive or inaccurate due to api key service being not available and the hugging face model being not that good.



## Getting Started

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.x
- Required libraries: PyMuPDF, OpenCV, Pillow, transformers, pandas,google-generativeai

Installing of necessary libraries is being handaled by run.sh you just need to add the library name in requirements.txt file

### To run and get output of tagged images with tags in csv file

The entire process of image extraction and tagging is automated with the run.sh script. The script will perform the following steps in sequence:

Create snapshots of each page of the PDF.

Extract images using the contour-based approach.

Generate relevant tags for each image.

To run the system, replace the pdf filename in the snap.py script and use the following command:
bash
```
./run.sh
```
