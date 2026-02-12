# MMVII — MicMac v2

**A free, open-source photogrammetry suite for 3D reconstruction**

Developed at **IGN** (French Mapping Agency) / **ENSG** / **LASTIG**

---

MMVII is a complete rewrite of [MicMac](https://github.com/micmacIGN/micmac) in modern C++17,
focused on maintainability, performance, and facilitating external contributions.
It provides a comprehensive photogrammetry pipeline: from feature extraction
and tie point matching, through pose estimation and bundle adjustment,
to dense matching and 3D reconstruction.

## Key Features

<div class="grid cards" markdown>

-   **Pose Estimation**

    ---

    Multiple algorithms including 11-point, space resection, and relative pose estimation from GCP and tie points.

-   **Bundle Adjustment**

    ---

    Comprehensive bundle adjustment with multiple observation types, constraints, and flexible parametrization.

-   **Dense Matching**

    ---

    Generic epipolar dense matching with pluggable algorithms (SGM, PSMNet) and tile-based processing for large images.

-   **Coded Targets**

    ---

    Full workflow for generation, encoding, detection, refinement, and validation of coded targets.

-   **Symbolic Derivatives**

    ---

    Automatic code generation for mathematical derivatives, simplifying development of complex models.

-   **Python API**

    ---

    Full Python 3 bindings via PyBind11 for scripting and integration with scientific workflows.

</div>

## Quick Start

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt install pkg-config libproj-dev libgdal-dev

# Clone and build
git clone https://github.com/micmacIGN/micmac.git
cd micmac/MMVII
mkdir build && cd build
cmake ../
make full -j$(nproc)

# Verify installation
MMVII Bench 1
```

## Modules

MMVII provides **120+ commands** organized into modules:

| Module | Description |
|--------|-------------|
| **Orientation** | Bundle adjustment, pose estimation, calibration |
| **Dense Matching** | Epipolar matching, evaluation, densification |
| **Coded Targets** | Generation, extraction, refinement, validation |
| **Point Clouds** | Conversion, clipping, colorization, projection |
| **Mesh Processing** | Validation, clipping, planar development |
| **Radiometry** | Model creation and equalization |
| **Import / Export** | GCP, orientations, tie points, clouds, lines |
| **Reports & Analysis** | Measurements, tie points, GCP, pose comparison |

## Citing MMVII

If you use MMVII in your research, please cite:

```bibtex
@software{mmvii,
  title  = {MMVII -- MicMac v2},
  author = {IGN / ENSG / LASTIG},
  url    = {https://github.com/micmacIGN/micmac},
  year   = {2024}
}
```
