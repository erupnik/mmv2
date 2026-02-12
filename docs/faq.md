# FAQ

## General

### What is the difference between MicMac and MMVII?

MMVII (MicMac v2) is a complete rewrite of MicMac in modern C++17. While MicMac v1 is still available and maintained, MMVII is the actively developed version with a cleaner architecture, better documentation, and new features. MMVII can import data processed with MicMac v1 using conversion commands (`V1OriConv`, `TiePConvert`).

### What platforms are supported?

MMVII builds on **Linux**, **macOS**, and **Windows** (via Git Bash + vcpkg). Linux is the primary development platform.

### Is there a GUI?

**vMMVII** is a Qt5-based graphical interface for building MMVII command lines. It is in beta and can be enabled with `-DvMMVII_BUILD=ON` during CMake configuration.

### How do I get help on a specific command?

```bash
MMVII CommandName help
```

This displays the command's mandatory and optional arguments with descriptions.

## Building

### Why is it a "two-stage" build?

MMVII uses symbolic derivative code generation. The first compilation builds the code generator (`GenCodeSymDer`). It is then run to produce C++ derivative code in `src/GeneratedCodes/`. The second compilation includes this generated code. The `make full` target handles both stages automatically.

### Build fails with PROJ not found

Ensure PROJ >= 9.4.1 is installed:

```bash
# Ubuntu/Debian
sudo apt install libproj-dev

# Check version
pkg-config --modversion proj
```

### Build fails with GDAL not found

```bash
sudo apt install libgdal-dev
pkg-config --modversion gdal
```

## Usage

### How do I convert MicMac v1 data to MMVII?

```bash
# Convert orientations
MMVII V1OriConv ".*tif" OrientationName CameraModel

# Convert tie points
MMVII TiePConvert ".*" Pastis
```

### What image formats are supported?

MMVII uses GDAL for image I/O, so it supports all GDAL-supported formats: TIFF, JPEG, PNG, and many others. GeoTIFF metadata is preserved.

### How do I work with satellite imagery?

Import the vendor RPC model, then optionally add polynomial corrections:

```bash
MMVII ImportInitExtSens "*.tif" RPC WGS84
MMVII OriParametrizeSensor "*.tif" RPC Param Degree=[0,2]
```

See the [RPC Satellite tutorial](tutorials/rpc-satellite.md) for a complete workflow.

### Where does MMVII store project data?

In the `MMVII-PhgrProj/` directory at the project root, organized into subdirectories:

```
MMVII-PhgrProj/
├── Ori/            # Orientations
├── PointsMeasure/  # Tie points, GCPs
├── MetaData/       # Camera metadata
├── Reports/        # Generated reports
└── ...
```
