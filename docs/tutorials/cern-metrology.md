# Industrial Metrology (CERN)

!!! info "Dataset"
    `MMVII-UseCaseDataSet/CERN-Pipelines/`

High-precision measurement of particle detector components at CERN.
This workflow demonstrates multi-camera rigid block calibration,
coded and uncoded target processing, and clinometer integration for
tilt measurement.

## Overview

- Generate and extract CERN 14-bit coded targets
- Calibrate multiple cameras via space resection and bundle adjustment
- Initialize multi-camera rigid blocks
- Process clinometer (tilt) data
- Detect uncoded targets and extract geometric lines

## Workflow

### 1. Generate target encoding

```bash
MMVII CodedTargetGenerateEncoding CERN 14
```

### 2. Extract coded targets

```bash
MMVII CodedTargetCircExtract "Calib.*JPG" CodedTarget-CERN-14b.xml
```

### 3. Pose estimation and bundle adjustment

```bash
MMVII OriPoseEstimSpaceResection "Calib.*JPG" GCP OriSR
MMVII OriBundleAdj "Calib.*JPG" OriSR OriBA
```

### 4. Initialize multi-camera rigid block

```bash
MMVII BlockCamInit "Calib.*JPG" OriBA Block
MMVII BlockInstrEdit "Calib.*JPG" Block Constraints
```

This constrains the relative geometry between cameras that are rigidly mounted on the same platform, propagating calibration across the entire measurement session.

### 5. Process clinometer data

```bash
MMVII ClinoInit "Clino.*JPG" OriBA ClinoMes
MMVII BlockInstrInitClino Block ClinoMes
```

Integrates tilt measurements from inclinometers, computing boresight matrices for the clinometer-camera relationship.

### 6. Complete uncoded targets

```bash
MMVII CodedTargetCompleteUncoded ".*JPG" OriBA GCP
```

Uses the calibrated geometry to find and measure additional targets that do not carry a code.

### 7. Extract geometric lines (optional)

```bash
MMVII ExtractLine "Fil.*JPG" OriBA Lines
```

Detects wires and lines in the images for additional geometric constraints in the CERN alignment system.
