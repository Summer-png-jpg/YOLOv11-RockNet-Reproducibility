# YOLOv11-RockNet-Reproducibility

This repository provides a **reproducibility package** for the paper:

**Borehole-Image-Based Automated BQ Rock-Mass Classification Using an Enhanced YOLOv11-RockNet**  
(submitted to *Geophysics*, SEG)

---

## 1. Scope of Reproducibility

Due to project-specific data confidentiality, the full training dataset used in the paper is not publicly released.

This repository enables:

- **Inference-level reproducibility**
- **Evaluation-level reproducibility**

Specifically, independent users can recompute the following key results reported in the paper:

- Rock Quality Designation (RQD)
- Rock integrity coefficient (Kv)
- Basic Quality index (BQ)

for representative boreholes listed in Table 2 of the manuscript.

---

## 2. Repository Structure
model/ Model architecture description and trained weights
reproducibility/ Evaluation scripts and minimal reproducibility data
environment.yml Conda environment for dependency reproduction

## 3. Quick Start

```bash
conda env create -f environment.yml
conda activate yolo-rocknet
python reproducibility/evaluation_bq.py
The script will output reproduced RQD, Kv, and BQ values and compare them with reference values reported in the paper.

4. Notes on Training Curves

Training curves (Precision–Recall, Precision–Confidence, Recall–Confidence, F1–Confidence) were generated during the training process and cannot be reconstructed from trained model weights alone. This is standard practice in deep-learning-based geophysical interpretation studies.

5. Citation
If you use this repository, please cite the corresponding paper.
