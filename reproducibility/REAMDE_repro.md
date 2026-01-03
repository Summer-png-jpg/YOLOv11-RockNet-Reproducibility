# Reproducibility Instructions (Geophysics)

This folder provides **evaluation-level reproducibility** for the manuscript.

---

## 1. Reproducible Targets

Using the provided scripts and data, users can independently recompute:

- Rock Quality Designation (RQD)
- Rock integrity coefficient (Kv)
- Basic Quality index (BQ)

for representative boreholes reported in Table 2 of the paper.

---

## 2. Minimal Reproducibility Dataset

Two representative boreholes are provided:

- **granite_SZ1**: high-integrity granite rock mass
- **slate_YZ5**: fractured slate rock mass

Each case includes:
- Borehole image (for reference)
- Joint depth labels (derived from detection results)
- Measured uniaxial compressive strength (Rc)

---

## 3. Run Evaluation

```bash
python evaluation_bq.py
