# Coded Target Detection

!!! info "Dataset"
    `MMVII-UseCaseDataSet/Circ-Code-Target/`

High-precision measurement using circular coded targets. This tutorial
covers the full pipeline from target encoding to pose estimation with
NIKON D5600 images.

## Overview

- Generate a CERN 14-bit Hamming-coded target specification
- Extract coded targets from 40+ calibration images
- Import 3D target positions as ground control points
- Estimate camera poses (linear 11-parameter, then space resection)
- Refine with bundle adjustment
- Complete uncoded targets using known geometry

## Workflow

### 1. Generate target encoding

```bash
MMVII CodedTargetGenerateEncoding CERN 14
```

This creates a specification file (`CodedTarget-CERN-14b.xml`) defining the binary encoding of each target.

### 2. Extract coded targets from images

```bash
MMVII CodedTargetCircExtract "043_.*tif" CodedTarget-CERN-14b.xml
```

Detects and decodes circular coded targets with sub-pixel center measurement.

### 3. Import 3D target positions

```bash
MMVII ImportGCP Positions-3D-14bit_lookup.txt ANXYZ
```

Imports the known 3D coordinates of each coded target.

### 4. Initial pose estimation (11-parameter linear)

```bash
MMVII OriPoseEstim11P "043_.*tif" GCP Ori11P
```

Fast linear estimation of camera pose from 2D-3D correspondences.

### 5. Space resection refinement

```bash
MMVII OriPoseEstimSpaceResection "043_.*tif" GCP Ori11P OriSR
```

Non-linear refinement of the initial pose.

### 6. Bundle adjustment

```bash
MMVII OriBundleAdj "043_.*tif" OriSR OriBA
```

Joint optimization of all camera poses and calibration parameters.

### 7. Complete uncoded targets (optional)

```bash
MMVII CodedTargetCompleteUncoded "043_.*tif" OriBA GCP
```

Uses the calibrated geometry to identify and measure targets without codes.

## Multi-camera block

If working with multiple rigidly mounted cameras (e.g., cameras 043 and 671):

```bash
MMVII BlockCamInit ".*tif" OriBA Block
```

This constrains the relative poses between cameras in a rigid block.
