#!/bin/bash
pip install -r requirements.txt
python snap.py
python ext.py
python adding_tag.py
echo "Extraction completed"
