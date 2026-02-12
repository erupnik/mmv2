# Legacy + Modern Imagery

!!! info "Dataset"
    `MMVII-UseCaseDataSet/Argentique-Sat/`

Combining historical aerial film photography (1971 IGN archives) with
contemporary Pleiades HR satellite data. Demonstrates MicMac v1 → MMVII
format conversion and joint processing of very different sensor types.

## Overview

- Convert MicMac v1 tie points and orientations to MMVII format
- Import satellite RPC models for Pleiades HR images
- Perform joint bundle adjustment of legacy + modern imagery

## Workflow

### 1. Convert V1 tie points

```bash
MMVII TiePConvert ".*" Pastis
```

Converts MicMac v1 Pastis-format tie points to MMVII format.

### 2. Convert V1 orientations

```bash
MMVII V1OriConv "OIS.*tif" Campari Conic
```

Imports orientations computed by MicMac v1's Campari (bundle adjustment) with the conic camera model used for film-based aerial photography.

### 3. Import satellite RPC models

```bash
MMVII ImportInitExtSens "PHR.*tif" RPC WGS84
```

Imports Pleiades HR satellite orientations from vendor-supplied RPC files.

### 4. Validate sensors

```bash
MMVII TestSensor ".*tif" OriInit
```

Verifies that all sensor models (historical and satellite) are functioning correctly before adjustment.

### 5. Joint bundle adjustment

```bash
MMVII OriBundleAdj ".*" OriInit OriBA-Joint
```

Optimizes all parameters jointly, bridging the 50-year gap between the two datasets.
