#!/bin/bash
pip install -r requirements.txt
python snap.py
python ext.py
python addingtag.py
echo "Extraction completed"