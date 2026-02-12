# Command Reference

MMVII provides **118 commands** organized by domain. Run `MMVII help` for a complete list.

Every MMVII command follows the same pattern:

```
MMVII CommandName MandatoryArg1 MandatoryArg2 [OptArg1=value] [OptArg2=value]
```

Get help on any command with: `MMVII CommandName help`

!!! note "Auto-generated"
    This page is auto-generated from the source code by `scripts/generate_commands.py`.

## Orientation & Bundle Adjustment

| Command | Description |
|---------|-------------|
| `___OriPoseArboTriplet` | Create arborescence of triplet (internal use essentially) |
| `BlockCamInit` | Compute initial calibration of rigid bloc cam |
| `CERN_ImportClino` | A temporary command to arrange clino format from file splited in different folders |
| `CERN_InitRep` | Initialize the repere local to wire/sphere/clino |
| `ClinoInit` | Initialisation of inclinometer |
| `ExportUndistMesIm` | Export image points measurements corrected from distorsion |
| `ExtractLine` | Extraction of lines |
| `ExtractLine` | Extraction of lines |
| `ImportAiconCalib` | Import a camera calibration from an Aicon file |
| `ImportInitExtSens` | Import an  Initial External Sensor |
| `ImportOri` | Import/Convert basic Orient file in MMVII format |
| `ImportTripletV1` | Import/Convert triplets in MMVII format |
| `OriBundleAdj` | Bundle adjusment between images, using several observations/constraint |
| `OriParametrizeSensor` | Import an External Sensor |
| `OriPoseEstim11P` | Pose estimation from GCP, uncalibrated case |
| `OriPoseEstimCheckGCPDist` | Check GCP distribution for pose estimation |
| `OriPoseEstimRel2Im` | Estimate relative orientation with different algorithms |
| `OriPoseEstimSpaceResection` | Pose estimation from GCP, calibrated case |
| `ReportBlock` | Report different measures relative to a block of cam |
| `ReportClino` | Report on Clino Calibration&Measures |
| `ReportPoseCmp` | Reports on pose comparison |
| `SimulOriPerturbRandom` | Perturbate random de orientation (for simulations) |
| `TestSensor` | Test orientation functions of a sensor : coherence Direct/Inverse, ground truth 2D/3D correspondance, generate 3d-2d corresp |
| `V1OriConv` | Convert orientation of MMV1  to MMVII |
| `V2ImportCalib` | Import a calibration from another MMVII project (just copy files) |

## Dense Matching

| Command | Description |
|---------|-------------|
| `DenseMatchEpipEval` | Evaluation of dense matching |
| `DM01DensifyRefMatch` | Create dense map using a sparse one (LIDAR) with or without images |
| `DM0BisTestHypStep` | Compute statistic to fix the relation hiden-part/step-paralax |
| `DM1ExtractVecLearn` | Extract ground truch vector to learn Dense Matching |
| `DM2CalcHistoCarac` | Compute and save histogramm on single caracteristics |
| `DM3CalcHistoNDim` | Compute and save histogramm on multiple caracteristics |
| `DM4FillCubeCost` | Fill a cube with matching costs |
| `DM4MatchMultipleOrtho` | Compute similarite of overlapping ortho images |
| `DM5StatMatch` | Make some evaluation of dense Match with a reference |

## Coded Targets

| Command | Description |
|---------|-------------|
| `CodedTargetCheckBoardExtract` | Extract coded target from images |
| `CodedTargetExtract` | Extract coded target from images |
| `CodedTargetGenerate` | Generate images for coded target |
| `CodedTargetGenerateEncoding` | Generate en encoding for coded target, according to some specification |
| `CodedTargetSimul` | Simulate images of coded targets, with ground truth |
| `SimulImageSphere` | Simulate images of spheres taking into account perspectives & distortions |

## Point Clouds & Mesh

| Command | Description |
|---------|-------------|
| `CloudMMVII2Ply` | Generate a ply version of  MMVII-Cloud |
| `CloudMMVIIClip` | Clip a MMVII-Cloud format  using a box |
| `CloudMMVIIColorate` | Generate a colorate version of  MMVII-Cloud |
| `CloudMMVIIImProj` | Generate image projections of coloured point cloud |
| `ImportStaticScan` | Import static scan cloud point into instrument raster geometry |
| `ImportTxtCloud` | Import/Convert cloud point in txt format (ply ...) |
| `MeshCheck` | Make some checking on a mesh, eventually correct it 4 easy defaults |
| `MeshCloudClip` | Clip a point mesh/cloud  using a region |
| `MeshDev` | Generate a planar devlopment minimizing deformations |
| `MeshDevGen` | Generate artificial(synthetic) devlopable surface |
| `MeshProjImage` | (internal) Project a mes on an image to prepare devlopment |
| `TestSLRE` | Make some quik&dirty test on Static Lidar Reverse Engeneering |

## Ground Control Points

| Command | Description |
|---------|-------------|
| `ImportGCP` | Import/Convert basic GCP file in MMVII format |
| `ImportM32` | Import/Convert Set of 3d-2d corresspondances |
| `ImportMesImGCP` | Import/Convert basic image point measures into MMVII format |
| `MergeMesImGCP` | Merge different files of image measur of GCP |
| `MMV2_MesIm_2_MMV1` | Export image measurements format from MicMac v2 to MicMac v1 |
| `ReportGCP` | Reports on GCP projection |
| `ReportMesIm` | Reports on Images measures compared to a reference |
| `V1ConvertGCPIm` | Convert image & gound measures from v1 to v2 format |

## Tie Points

| Command | Description |
|---------|-------------|
| `CompPIB` | This command is used compute Parameter of Binary Index |
| `ImportTiePMul` | Import/Convert basic TieP mult file in MMVII format |
| `PseudoIntersect` | Pseudo Intersect: 2D points to 3D coords |
| `ReportSegIm` | Reports on SegImage comparison |
| `ReportTieP` | Reports on TieP projection |
| `TieP-AimeBasicMatch` | Match caracteristic points and descriptors computed with Aime method |
| `TieP-AimePCar` | Compute caracteristic points and descriptors, using Aime method |
| `TieP2PMul` | Convert TieP from by-pair  to multiple |
| `TiePConvert` | Convert homologous point |

## Lines

| Command | Description |
|---------|-------------|
| `ImportLine` | Import/Convert Set of lines extracted |
| `ImportMeasuresClino` | Import/Convert file of clinometers from raw to MMVII format |

## Coordinate Systems

| Command | Description |
|---------|-------------|
| `GCPChSysCo` | Change SysCo of GCP |
| `OriChSysCo` | Chang coord system of an orientation |
| `OriCreateCalib` | Create initial internal calibration |
| `SysCoCreateAlias` | Create a coordinate system in the standard folder |
| `SysCoCreateRTL` | Create RTL (local tangent repair) |
| `TestProj` | Test Proj |

## Radiometry

| Command | Description |
|---------|-------------|
| `RadiomComputeEqual` | Estimate radiometric model for equalization |
| `RadiomCreateModel` | Create an initial neutral radiometric model |

## Topography

| Command | Description |
|---------|-------------|
| `ImportOBS` | Import Obs file in MMVII project |
| `TopoAdj` | Topo adjustment |

## Block Instruments

| Command | Description |
|---------|-------------|
| `BlockInstrEdit` | Create/Edit a block of instruments |
| `BlockInstrInitCam` | Init  camera poses inside a block of instrument |
| `BlockInstrInitClino` | Init  camera poses inside a block of instrument |
| `BlockInstrReport` | Make a report on a block of instrument confronted to data |

## Image Processing

| Command | Description |
|---------|-------------|
| `CodedTargetCircExtract` | Extract coded target from images |
| `CodedTargetCompleteUncoded` | Complete detection, with uncoded target |
| `CodedTargetRefineCirc` | Refine circ target with shape-distorsion using 3d-predict |
| `DeplStack` | Stack a serie multi date displacment |
| `ExifData` | Display Exif metadata from image file |
| `ExtractBubbles` | Extraction of Bubbles |
| `ImageCalcDisc` | Compute value of discontinuities in images |
| `ImageScale_Basic` | Down scale an image, basic Gauss-Filter + integer decimation, for backwrad compatibility |
| `ImageScale_Std` | Down scale an image, basic Gauss-Filter + integer decimation, for backwrad compatibility |
| `ImageStack` | Stack a serie of images |
| `MeshImageDevlp` | Compute devlopped images from 3d-mesh, 2d-dev-mesh and ori |
| `SimulDispl` | Generate smooth displacement and deformed image |

## Project Management

| Command | Description |
|---------|-------------|
| `EditCalcMTDI` | Edit the calculator of Meta-Data images |
| `EditRel` | This command is used to edit set of pairs of files |
| `EditSet` | This command is used to edit set of file |
| `GenerateSpecifSerial` | Generate specification+some sample for serialization |
| `TutoFormalDeriv` | Tutorial for serialization |
| `TutoSerial` | Tutorial for serialization |
| `UtiDicoRename` | This command create a dictionnary after parsing a file, can be used for renaming |

## MMVII Management

| Command | Description |
|---------|-------------|
| `GenArgsSpec` | This command is used to generate arguments specifications |
| `GenCodeSymDer` | Generation of code for symbolic derivatives |

## Testing

| Command | Description |
|---------|-------------|
| `Bench` | This command execute (many) self verification on MicMac-V2 behaviour |
| `Cpp11` | This command execute some test for to check my understanding of C++11 |
| `TestAPBI` | Internal only !! Used by APBI bench |
| `TestCovProp` | Test on covariance propagation |
| `TestEigen` | This command execute some experiments eigen (matrix manipulation) library |
| `TestMPD` | This used a an entry point to all quick and dirty test by MPD ... |
| `TestRecall` | Use in Bench to Test Recall of MMVII by itself |

## Personal / Experimental

| Command | Description |
|---------|-------------|
| `MediaCat` | This command is used for concatening medias (interface to ffmpeg) |
| `MediaDaisy` | This command is used to generate audio book to daisy format from mp3 files |
| `MediaReduceVideo` | This command is used for reducing the size of video files |
| `MediaWalkman` | This command is used to make a random selection of music |
| `TestGraphPart` | This command is to make some test on graph partionning |
