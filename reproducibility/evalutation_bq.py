```python
import numpy as np
import pandas as pd
from pathlib import Path

# -----------------------------
# Paper-defined formulas
# -----------------------------
def compute_rqd(joint_depths_cm, total_length_cm, threshold=10):
    """
    Compute RQD following the paper definition.
    """
    joint_depths_cm = np.sort(joint_depths_cm)
    spacings = np.diff(joint_depths_cm)
    valid_segments = spacings[spacings >= threshold]

    if total_length_cm <= 0:
        return 100.0

    return 100.0 * valid_segments.sum() / total_length_cm


def compute_kv(rqd):
    """
    Equation (20) in the paper
    """
    return 0.00896 * rqd - 0.03773


def compute_bq(rqd, rc):
    """
    Equation (21) in the paper
    """
    return 80.57 + 3.0 * rc + 2.24 * rqd


# -----------------------------
# Load minimal reproducibility data
# -----------------------------
base_dir = Path("reproducibility/data_minimal")

cases = ["granite_SZ1", "slate_YZ5"]
records = []

for case in cases:
    joint_file = base_dir / case / "label.txt"
    rc_file = base_dir / case / "Rc.txt"

    joint_depths = np.loadtxt(joint_file)  # unit: cm
    rc = float(rc_file.read_text())

    rqd = compute_rqd(joint_depths, total_length_cm=100)
    kv = compute_kv(rqd)
    bq = compute_bq(rqd, rc)

    records.append([case, rqd, kv, bq])

df = pd.DataFrame(records, columns=["Case", "RQD", "Kv", "BQ"])

print("\nReproduced Results:")
print(df)

df.to_csv("reproducibility/results_reproduced.csv", index=False)