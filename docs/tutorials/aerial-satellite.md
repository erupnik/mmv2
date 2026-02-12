# Aerial + Satellite Fusion

!!! info "Dataset"
    `MMVII-UseCaseDataSet/Aerien-Sat/`

Demonstrates the fusion of drone (UltraCam Eagle) and satellite
(Pleiades Neo) imagery in a joint bundle adjustment. This showcases
MMVII's ability to handle heterogeneous sensor types in a common
coordinate system.

## Overview

- Import satellite RPC orientations for PNEO-3/PNEO-4 images
- Create a local RTL coordinate system
- Parametrize satellite sensors with polynomial corrections
- Process aerial (drone) imagery
- Joint bundle adjustment combining both data sources

## Satellite processing

### 1. Import satellite RPC orientations

```bash
MMVII ImportInitExtSens "PNEO.*tif" RPC WGS84
```

### 2. Create local coordinate system

```bash
MMVII SysCoCreateRTL RTL-Manosque.xml
```

Creates a local tangent frame (Right-Top-Left) at the project location for metric-scale processing.

### 3. Parametrize satellite sensors

```bash
MMVII OriParametrizeSensor "PNEO.*tif" RPC RPC-Param Degree=[0,2]
```

Adds polynomial correction layers (degree 0 and 2) on top of the vendor RPC model.

### 4. Bundle adjustment (satellite only)

```bash
MMVII OriBundleAdj "PNEO.*tif" RPC-Param OriBA-Sat \
    TiePWeight=[1,1] GCPWeight=[1,1,1]
```

## Aerial processing

Process the drone images separately with standard orientation pipeline, then convert tie points for the joint step.

## Joint adjustment

### 5. Combined bundle adjustment

```bash
MMVII OriBundleAdj ".*tif" OriInit OriBA-Mixt \
    TiePWeight=[1,1] GCPWeight=[1,1,1]
```

Joint optimization of all satellite and aerial camera parameters in a single adjustment.

### 6. Verify results

```bash
MMVII TestSensor ".*tif" OriBA-Mixt
MMVII ReportGCP ".*tif" OriBA-Mixt
```
