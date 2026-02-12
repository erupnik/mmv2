# Topographic Survey Adjustment

!!! info "Dataset"
    `MMVII-UseCaseDataSet/TopoMini/`

A minimal example of topographic network adjustment: import a set
of control points and observations (distances, angles), transform
to a local coordinate system, and perform a least-squares adjustment.

## Overview

- Import control point coordinates in Lambert-93
- Convert to a local RTL coordinate frame
- Import distance and angle observations
- Perform least-squares network adjustment
- Convert results back to Lambert-93

## Workflow

### 1. Import control point coordinates

```bash
MMVII ImportGCP coords.txt ANXYZ SysCo=IGNF:LAMB93
```

Imports 4 control points (PtA through PtD) with their Lambert-93 easting, northing, and elevation.

### 2. Convert to local RTL frame

```bash
MMVII GCPChSysCo GCP L93 RTL
```

Transforms coordinates from the national projection to a local tangent frame suitable for metric-scale least-squares adjustment.

### 3. Import observations

```bash
MMVII ImportOBS meas.obs
```

Imports 14 observations: distances (in meters) and angles (in degrees) between the survey points, each with an associated uncertainty.

### 4. Least-squares adjustment

```bash
MMVII TopoAdj GCP-RTL Obs AdjResult
```

Performs a rigorous least-squares adjustment of the topographic network, estimating adjusted coordinates and their uncertainties.

### 5. Convert results back to Lambert-93

```bash
MMVII GCPChSysCo AdjResult RTL L93
```

Transforms the adjusted coordinates back to the national coordinate system for delivery.
