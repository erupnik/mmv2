# Image Development & Mesh Processing

!!! info "Dataset"
    `MMVII-UseCaseDataSet/DevlopImage/`

Demonstrates the complete pipeline from 3D mesh to unwrapped,
radiometrically corrected texture maps. Starts from MicMac v1
dense matching output and uses MMVII for mesh processing, surface
development, and radiometric equalization.

## Overview

- Convert MicMac v1 orientations to MMVII
- Validate and correct mesh topology
- Clip mesh to region of interest
- Unwrap (develop) the 3D surface to 2D
- Build and apply radiometric equalization
- Generate final developed texture

## Workflow

### 1. Convert V1 orientations

```bash
MMVII V1OriConv "P105.*JPG" RadialExtended OriV2
```

### 2. Mesh correction

```bash
MMVII MeshCheck mesh.ply MeshChecked.ply
```

Detects and fixes topological problems: non-manifold edges, degenerate triangles, and other issues that would prevent surface development.

### 3. Mesh clipping

```bash
MMVII MeshCloudClip MeshChecked.ply cloud.ply MeshClipped.ply
```

Clips the mesh to the region covered by the point cloud, removing extraneous geometry.

### 4. Surface development (unwrapping)

```bash
MMVII MeshDev MeshClipped.ply DevResult
```

Unfolds the 3D surface into a 2D plane while minimizing isometric deformation. This produces a mapping between 3D mesh coordinates and 2D texture coordinates.

### 5. Radiometric equalization

```bash
# Set camera aperture metadata
MMVII EditCalcMTDI "P105.*JPG" Aperture=11

# Build radiometric model (vignetting + per-image correction)
MMVII RadiomCreateModel "P105.*JPG" OriV2 RadiomModel
MMVII RadiomComputeEqual "P105.*JPG" OriV2 RadiomModel RadiomEqual
```

Computes corrections for sensor vignetting and per-image brightness/contrast variations so that the final texture has uniform appearance.

### 6. Generate developed texture

```bash
MMVII MeshImageDevlp "P105.*JPG" OriV2 DevResult RadiomEqual
```

Projects the radiometrically corrected images onto the unwrapped mesh to produce the final 2D texture map.
