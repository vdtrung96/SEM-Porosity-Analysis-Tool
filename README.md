# SEM Porosity Analysis Tool

Automatic porosity calculation from SEM images using image processing and Otsu thresholding.

---

## Overview

This repository provides a simple and efficient Python-based tool for calculating the porosity of porous materials from SEM (Scanning Electron Microscopy) images.

The workflow automatically:

* Reads grayscale SEM images
* Applies Otsu automatic thresholding
* Segments pore and solid regions
* Calculates porosity percentage
* Generates colored binary visualization images
* Saves processed results automatically

This tool is useful for:

* Porous materials analysis
* Electrospun fibers
* Hydrogels
* Textile structures
* Battery electrodes
* Membranes
* Bio-material characterization
* Surface morphology studies

---

## Features

* Automatic pore segmentation
* Otsu adaptive thresholding
* Fast porosity calculation
* Colored binary output visualization
* High-resolution figure export
* Simple and lightweight Python implementation

---

## Method

The porosity is calculated using:

         Porosity (%) = (Pore Pixels / Total Pixels) × 100


The algorithm workflow:

1. Convert SEM image to grayscale
2. Apply Otsu thresholding
3. Detect pore regions
4. Count pore pixels
5. Calculate porosity percentage
6. Save binary-colored result image

---

## Requirements

Install required packages:

```bash
pip install opencv-python numpy matplotlib
```

---

## Usage

Update the SEM image path inside the script:

```python
image_path = r"Your SEM file path here"
```

Run the script:

```bash
python porosity_calculation.py
```

---

## Output

The program automatically generates:

* Calculated porosity value
* Binary segmented image
* Colored visualization image
* High-resolution exported figure

Example:

```text
Porosity: 42.57%
Saved to: sample_calculated.png
```

---

## Example Workflow

### 1. Original SEM Image

Input grayscale SEM image.

### 2. Binary Segmentation

Automatic pore detection using Otsu thresholding.

### 3. Colored Visualization

Pore regions and background are highlighted using different colors.

### 4. Final Porosity

Automatic quantitative porosity calculation.

---

## Applications

This tool can be applied in:

* Materials science
* Textile engineering
* Electrochemical devices
* Membrane technology
* Tissue engineering
* Energy storage materials
* Surface morphology analysis

---

## Future Improvements

Potential future developments:

* Multi-image batch processing
* GUI interface
* Machine learning segmentation
* Particle size distribution analysis
* Pore size statistics
* Real-time SEM analysis
* Adaptive morphology filtering

---

## Author

JickyTrung
