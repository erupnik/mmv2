# Building MMVII

## Dependencies

| Library | Min. Version | Purpose |
|---------|-------------|---------|
| CMake | 3.15 | Build system |
| PROJ | 9.4.1 | Coordinate transformations |
| GDAL | 3.4 | Image I/O and geospatial formats |
| Xerces-C | 3.2 | XML parsing |

**Optional:** Qt5 (GUI), pybind11 (Python API), OpenMP (parallelism), ccache (faster rebuilds), Doxygen (HTML docs).

## Linux / macOS

### Install dependencies (Ubuntu/Debian)

```bash
sudo apt install pkg-config cmake g++ \
    libproj-dev libgdal-dev libxerces-c-dev
```

### Build

```bash
# Clone the repository
git clone https://github.com/micmacIGN/micmac.git
cd micmac/MMVII

# Build (two-stage: compile + code generation + recompile)
mkdir build && cd build
cmake ../
make full -j$(nproc)

# Add to PATH
echo 'export PATH='$(pwd)'/../bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Build types

```bash
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ../   # default: -O3 -g
cmake -DCMAKE_BUILD_TYPE=Debug ../              # -g
cmake -DCMAKE_BUILD_TYPE=Release ../            # -O3 -DNDEBUG
```

## Windows

```bash
# Using vcpkg and Git Bash
cmake -DCMAKE_TOOLCHAIN_FILE=[VCPKG_DIR]/scripts/buildsystems/vcpkg.cmake ..
cmake --build . --target full --config Release
```

## Verifying the Installation

```bash
# Run the self-verification benchmark
MMVII Bench 1
```

If all tests pass, MMVII is correctly installed and ready to use.

## Make Targets

| Target | Description |
|--------|-------------|
| `make full` | Two-stage build: compile, generate symbolic derivatives, recompile |
| `make rebuild` | Clean + full rebuild |
| `make clean` | Remove build artifacts |
| `make distclean` | Clean + remove generated code |
