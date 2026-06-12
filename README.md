# Simple QC Dashboard (Streamlit)

This tool has been designed by Mattia Cazzolla for the MeCA team.
A minimal Streamlit-based Quality Control (QC) tool for manually rating images in a folder.
Images are presented one at a time and labeled using predefined numeric options.
Progress is saved continuously in a CSV file, allowing seamless interruption and resumption.

---

## Features

- Displays images sequentially from a target folder
- Discrete rating options (0–5)
- Automatic CSV creation if missing
- Safe resume: already-labeled images are skipped
- Option to save either **image filenames** or **full image paths**
- No external dependencies beyond Streamlit

---

## Requirements

- Python ≥ 3.8
- Required packages:
  - `streamlit`

Install Streamlit if needed:

```
pip install streamlit
```

---

## Usage

```
streamlit run QC_dashboard.py /path/to/image_folder [results.csv]
```

### Arguments

1. **Image folder (required)**
    Path to a folder containing images to be rated.
    Supported formats:
   - `.png`
   - `.jpg`
   - `.jpeg`
2. **CSV file (optional)**
    Path to the output CSV file
    Defaults to:

```
results.csv
```

---

## Configuration Options

Inside the script:

```
OPTIONS = [0, 1, 2, 3, 4, 5]
SAVE_FULL_PATH = False
```

- `OPTIONS`
   Labels available for rating each image.
- `SAVE_FULL_PATH`
  - `False` → saves only the filename (e.g. `image_01.jpg`)
  - `True` → saves the full absolute path (e.g. `/data/qc/image_01.jpg`)

Choose based on whether portability or traceability is more important for your workflow.

---

## Output CSV Format

If the CSV file does not exist, it is automatically initialized with:

```
image,label
```

Each rating appends one row:

- `image` → filename or full path (depending on configuration)
- `label` → selected rating value

Example:

```
image,label
img_001.jpg,4
img_002.jpg,2
```

---

## Resume Behavior

- On startup, the CSV file is scanned
- Images already present in the CSV are skipped
- If the session is interrupted, restarting resumes from the next unlabeled image
- Completion message is shown when all images are labeled

---

## Example

```
streamlit run QC_dashboard.py snapshots/ qc_labels.csv
```

