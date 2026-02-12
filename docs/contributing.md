# Contributing

MMVII is open source and welcomes contributions. This page describes
the conventions and architecture you need to know to add new commands or
modify existing ones.

## Adding a new command

Every MMVII command is a class inheriting from `cMMVII_Appli`. You need to implement three methods:

```cpp
class cMyCommand : public cMMVII_Appli
{
public:
    // Execute the command
    int Exe() override;

    // Declare mandatory arguments
    cCollecSpecArg2007 & ArgObl(cCollecSpecArg2007 &) override;

    // Declare optional arguments
    cCollecSpecArg2007 & ArgOpt(cCollecSpecArg2007 &) override;
};
```

Commands are registered globally via `cSpecMMVII_Appli` so that the MMVII dispatcher can find them.

See `Doc/Programmer/IntroProg.tex` for the full guide.

## Coding conventions

### Naming

| Prefix | Usage | Example |
|--------|-------|---------|
| `c` | Classes | `cMMVII_Appli`, `cPtxd` |
| `m` | Member variables | `mCoords`, `mName` |
| `t` | Type definitions | `tREAL8`, `tPt` |
| `The` | Static / global | `TheVecAll`, `TheCptObj` |
| `e` | Enums | `eTA2007`, `eOpAff` |

### Numeric types

```cpp
tREAL4   // float (32-bit)
tREAL8   // double (64-bit)
tREAL16  // long double
tINT4    // int (32-bit)
tINT8    // long int (64-bit)
tU_INT4  // unsigned int
```

### Output

Never use `std::cout`. Use `StdOut()` for all standard output.

### Memory management

Use smart pointers (`std::unique_ptr`). MMVII provides custom memory tracking via `cMemManager` and `cMemCountable`.

## Serialization

MMVII uses a universal `AddData()` visitor pattern for serialization. Objects describe themselves once and can be automatically serialized to XML, JSON, or binary:

```cpp
void AddData(const cAuxAr2007 & anAux, cMyClass & aObj)
{
    AddData(cAuxAr2007("Name", anAux), aObj.mName);
    AddData(cAuxAr2007("Value", anAux), aObj.mValue);
}
```

See `Doc/Programmer/Serialization.tex` for details.

## Symbolic derivatives

To add a new mathematical formula with automatic differentiation:

1. Define the formula in `src/SymbDerGen/`
2. Run `make full` — the two-stage build will generate the derivative code
3. Generated code appears in `src/GeneratedCodes/`

See `Doc/Programmer/SymbolicDerivation.tex` for the full documentation.

## Directory structure

```
src/
├── Appli/              # Command framework
├── BundleAdjustment/   # Bundle adjustment
├── CodedTarget/        # Coded target processing
├── DenseMatch/         # Dense matching
├── Geoms/              # Geometric primitives
├── ImagesBase/         # Image handling
├── Matrix/             # Dense/sparse matrices
├── Mesh/               # Mesh processing
├── PoseEstim/          # Pose estimation
├── Radiom/             # Radiometry
├── Sensors/            # Camera/sensor models
├── Serial/             # Serialization
├── SymbDerGen/         # Symbolic derivative formulas
├── SysCo/              # Coordinate systems
├── TieP/               # Tie point handling
├── Topo/               # Topographic processing
└── ...                 # 30+ more modules
```

## Running tests

```bash
MMVII Bench 1
```

Test files are in `src/Bench/`. The benchmark uses custom assertions:

```cpp
MMVII_INTERNAL_ASSERT_bench(condition, "message");
MMVII_INTERNAL_ASSERT_tiny(condition, "message");
MMVII_INTERNAL_ASSERT_medium(condition, "message");
MMVII_INTERNAL_ASSERT_strong(condition, "message");
```

## Further reading

- `Doc/Programmer/IntroProg.tex` — Adding commands
- `Doc/Programmer/ProgrammingStyle.tex` — Coding standards
- `Doc/Programmer/Serialization.tex` — Serialization framework
- `Doc/Programmer/SymbolicDerivation.tex` — Symbolic derivatives
- `Doc/Programmer/NonLinearOptim.tex` — Optimization methods
- `Doc/Programmer/PythonAPI.tex` — Python bindings
