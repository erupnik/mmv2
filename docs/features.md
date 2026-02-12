# Features

MMVII provides a comprehensive photogrammetry pipeline from image acquisition to 3D reconstruction.

## Camera Models

MMVII supports multiple sensor models for different acquisition setups:

- **Central Perspective Cameras** — Full mathematical model of the camera obscura with intrinsic calibration (focal length, principal point, distortion). Supports both physical and non-physical distortion models with polynomial and radial parametrizations.

- **Pushbroom / Line Scanner Sensors** — Time-dependent camera models for satellite imagery. Handles the continuously varying position and orientation of the sensor during line-by-line acquisition.

- **RPC (Rational Polynomial Coefficients)** — Import and refinement of vendor-supplied RPC models for satellite imagery (Pleiades, SPOT, WorldView, etc.), with optional polynomial correction overlays.

- **Multi-Instrument Blocks** — Rigid blocks of multiple instruments (cameras, clinometers, targets, GNSS, IMU) with unified rigid-body transformations and joint calibration.

## Pose Estimation

Multiple algorithms for determining camera position and orientation:

- **11-Parameter Linear Estimation** — Fast initial pose from 2D-3D correspondences using a linear formulation.
- **Space Resection** — Calibrated pose estimation from ground control points with non-linear refinement.
- **Relative Pose** — Two-image relative orientation using tie points, with multiple algorithmic variants.
- **Global Pose Initialization** — Combining multiple pairwise relative poses into a consistent global coordinate system through graph-based registration.

## Bundle Adjustment

Comprehensive non-linear optimization of the entire photogrammetric network:

- Gauss-Newton minimization with Schur complement for efficient handling of large systems
- Multiple observation types: tie points, GCPs, clinometer readings, distances, angles
- Flexible constraint system for fixing or weighting any parameter subset
- Joint adjustment of heterogeneous data (aerial + satellite, legacy + modern)
- Comprehensive reporting: residuals, sigma0, parameter uncertainty

## Dense Matching

Pixel-wise correspondence between image pairs for 3D surface reconstruction:

- **Generic Epipolar Framework** — Pluggable algorithm architecture supporting multiple matching methods.
- **SGM (Semi-Global Matching)** — MicMac v1-compatible cost aggregation with multi-directional optimization.
- **Deep Learning Integration** — PSMNet and other CNN-based stereo methods can be plugged in as backends.
- **Tile-Based Processing** — Automatic tiling for large images with configurable worker count for parallel execution.

## Tie Point Detection & Matching

Automated feature detection and matching between images:

- AIME descriptor: custom Gaussian-pyramid-based feature descriptor optimized for photogrammetry
- Multi-scale processing with automatic scale estimation
- Bit-vector descriptors for fast comparison
- Import support for external matchers (SuperGlue, LightGlue, etc.)

## Coded Targets

Full workflow for artificial marker-based measurement:

- **Generation** — Generate printable target images with configurable encoding (CERN 14-bit, IGN Indoor, IGN Drone variants).
- **Detection** — Automatic extraction and decoding of circular coded targets from images with sub-pixel refinement.
- **Validation** — Hamming-code-based error detection and geometric consistency checks.
- **Uncoded Target Completion** — Use known geometry to identify and measure uncoded targets.

## Mesh Processing

- **MeshCheck** — Detect and correct topological problems (non-manifold edges, degenerate triangles).
- **MeshCloudClip** — Clip meshes using 3D regions defined by point clouds.
- **MeshDev** — 2D surface development (unwrapping) with isometric deformation minimization.
- **MeshImageDevlp** — Generate developed (unwrapped) texture maps from images.

## Coordinate Systems

Full integration with the [PROJ](https://proj.org) library for coordinate reference system transformations:

- Local, geocentric, Euclidean, and RTL (Right-Top-Left) tangent frames
- EPSG code support for standard projections
- Automatic WGS84 ↔ local frame conversions
- Custom RTL frame creation at any geographic location

## Radiometry

Empirical radiometric correction for multi-image mosaicking and texture generation:

- Sensor-level vignetting correction (radial model)
- Per-image radiometric equalization using low-order polynomials
- Homologous-point-based radiometric matching across overlapping images

## Symbolic Derivative Code Generation

A unique feature of MMVII: automatic generation of C++ derivative code from mathematical formula specifications.

- Tree/DAG representation of formulas with shared sub-expression optimization
- Generates exact analytic Jacobians — no numerical approximation
- Two-stage build: formulas are compiled, then derivative code is generated and recompiled
- Simplifies development of new mathematical models (distortion, cost functions, etc.)

## Additional Features

- **Topographic Adjustment** — Least-squares network adjustment for surveying (distances, angles, coordinates).
- **Line Detection** — Gradient-based and Hough-transform line extraction, including anti-parallel wire detection for industrial metrology.
- **Lidar-Image Registration** — Fine registration between Lidar point clouds and photogrammetric images using radiometric similarity.
- **Clinometer Calibration** — Boresight calibration of tilt sensors within bundle adjustment.
- **Point Cloud Processing** — PLY export, clipping, colorization, and image projection.
