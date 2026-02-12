# Python API

MMVII provides Python 3 bindings via [PyBind11](https://pybind11.readthedocs.io/),
giving access to the core C++ classes from Python scripts.

## Installation

```bash
cd micmac/MMVII/apib11
pip wheel . --no-deps -w dist/
pip install dist/mmvii*.whl
```

The Python module works independently of a system-wide MMVII installation.

## Quick example

```python
import mmvii

# Create a 2D point
pt = mmvii.Pt2dr(1.0, 2.5)
print(pt.x(), pt.y())

# Create a 3D point
pt3 = mmvii.Pt3dr(1.0, 2.0, 3.0)
print(pt3.norm())
```

## Naming conventions

The Python API follows slightly different conventions than the C++ code:

| C++ | Python | Rule |
|-----|--------|------|
| `cPtxd<tREAL8,2>` | `Pt2dr` | Drop leading `c`, use shorthand |
| `mName` | `name` | Drop `m` prefix |
| `Exe()` | `exe()` | Lowercase initial letter |

## Available bindings

The following C++ modules have Python bindings:

- **Geometric classes** — `Pt2dr`, `Pt3dr`, `Pt2di`, etc.
- **Image processing** — Image read/write, filtering
- **Matrix operations** — Dense and sparse matrices
- **Measurements** — Image measurements, GCPs
- **Sensors** — Camera models, projections
- **Pose relationships** — Rotations, transformations

## Building the bindings

The Python bindings require `pybind11`:

```bash
pip install pybind11
```

Build from the `apib11/` directory:

```bash
cd micmac/MMVII/apib11
pip wheel . --no-deps -w dist/
pip install dist/mmvii*.whl
```

!!! note "NumPy compatibility"
    MMVII matrices and images can be converted to/from NumPy arrays for
    integration with the scientific Python ecosystem.

## Examples

Additional examples are available in `apib11/examples/` in the repository.

See also the [Programming Session on Python API](https://github.com/micmacIGN/micmac/releases/tag/MMVII_Documentation)
for slides and worked examples from the March 2024 training session.
