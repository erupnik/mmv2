# Bibliography

## Core References

### MicMac / MMVII

- Rupnik, E., Daakir, M., Pierrot Deseilligny, M. (2017). **MicMac – a free, open-source solution for photogrammetry.** *Open Geospatial Data, Software and Standards*, 2(1), 14.

- Pierrot Deseilligny, M., Paparoditis, N. (2006). **A multiresolution and optimization-based image matching approach: An application to surface reconstruction from SPOT5-HRS stereo imagery.** *IAPRS*, vol. XXXVI-1/W41.

### Dense Matching

- Pierrot Deseilligny, M., Paparoditis, N. (2006). **A multiresolution and optimization-based image matching approach.** *ISPRS Archives*.

### Coded Targets

- Pierrot Deseilligny, M. (2024). **Coded target detection and refinement in MMVII.** *MMVII Documentation*.

### Pose Estimation

- Nistér, D. (2004). **An efficient solution to the five-point relative pose problem.** *IEEE TPAMI*, 26(6), 756–770.

### Bundle Adjustment

- Triggs, B., McLauchlan, P.F., Hartley, R.I., Fitzgibbon, A.W. (2000). **Bundle Adjustment — A Modern Synthesis.** *Vision Algorithms: Theory and Practice*, LNCS 1883, 298–372.

## Related Software

- [OpenCV](https://opencv.org/) — Computer vision library
- [COLMAP](https://colmap.github.io/) — General-purpose SfM and MVS
- [OpenMVG](https://github.com/openMVG/openMVG) — Open Multiple View Geometry
- [Theia](http://theia-sfm.org/) — Structure from Motion library

## Programming Sessions & Training

- [MMVII Programming Session — Bundle Adjustment (March 2024)](https://github.com/micmacIGN/micmac/releases/tag/MMVII_Documentation)
- [MMVII Programming Session — Topography (September 2024)](https://github.com/micmacIGN/micmac/releases/tag/MMVII_Documentation)
- [MMVII YouTube Playlist (November 2023)](https://www.youtube.com/playlist?list=PLO_lg_3H3aFuMamUsImMzNGPwfkAZge5m)

## External Libraries

MMVII includes the following header-only libraries:

| Library | Version | License | Purpose |
|---------|---------|---------|---------|
| Eigen | 3.4.0 | MPL2 | Linear algebra |
| Delaunator | — | MIT | Delaunay triangulation |
| happly | — | MIT | PLY file I/O |
| pybind11 | — | BSD | Python bindings |
