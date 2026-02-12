# RPC Satellite Processing

!!! info "Dataset"
    `MMVII-UseCaseDataSet/RPC/`

Working with satellite imagery RPC models: importing, validating,
parametrizing with polynomial corrections, and optimizing through
bundle adjustment.

## Overview

- Import reference points and vendor RPC models (SPOT satellite)
- Create a local coordinate system
- Validate initial RPC accuracy
- Add polynomial correction overlays
- Optimize via bundle adjustment

## Workflow

### 1. Import reference points

```bash
MMVII ImportM32 verif_1A.txt ImRef_1A
```

Imports reference points with image coordinates and WGS84 geographic coordinates.

### 2. Import RPC models

```bash
MMVII EditSet ".*" AllIm
MMVII ImportInitExtSens ".*" RPC WGS84
```

Imports vendor-supplied RPC (Rational Polynomial Coefficient) models for each satellite image.

### 3. Create local coordinate system

```bash
MMVII SysCoCreateRTL RTL-Local.xml
```

### 4. Test initial RPC accuracy

```bash
MMVII TestSensor ".*" RPC
```

Evaluates how well the vendor RPC model matches the reference points before any refinement.

### 5. Parametrize sensors with polynomial corrections

```bash
MMVII OriParametrizeSensor ".*" RPC RPC-Param Degree=[0,2]
```

Adds polynomial deformation layers (degree 0 = shift, degree 2 = quadratic) on top of the RPC model. This corrects systematic errors in the vendor model.

### 6. Bundle adjustment

```bash
MMVII OriBundleAdj ".*" RPC-Param OriBA GCPWeight=[1,1,1]
```

Optimizes the polynomial correction parameters using ground control points and tie points.

## Coordinate system options

The same workflow can be run in WGS84 geographic coordinates or in a local RTL frame. The `CmdWGS84.sh` and `CmdRTL.sh` scripts in the dataset demonstrate both variants.
