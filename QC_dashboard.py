import streamlit as st
import os
import csv
import sys

# --- CONFIGURATION ---
FOLDER = sys.argv[1]
CSV_FILE = sys.argv[2] if len(sys.argv) > 2 else "results.csv"
OPTIONS = [0, 1, 2, 3, 4, 5]
SAVE_FULL_PATH = False  # Set True to save /path/to/img.jpg, False for img.jpg

st.set_page_config(layout="wide", page_title="Simple QC")

# --- 1. PREPARATION ---
# Initialize CSV if missing
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        csv.writer(f).writerow(["image", "label"])

# Read what is already done
done_images = set()
if os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'r') as f:
        rows = list(csv.reader(f))
        if len(rows) > 1:
            for row in rows[1:]:
                # We store whatever was saved (filename or full path) 
                # to check against later
                done_images.add(row[0])

# Get list of images to do
queue = []
if os.path.exists(FOLDER):
    all_files = sorted(os.listdir(FOLDER))
    for f in all_files:
        if f.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.abspath(os.path.join(FOLDER, f))
            
            # Check if either the filename OR the full path is in the done set
            if f not in done_images and full_path not in done_images:
                queue.append(f)
else:
    st.error(f"Folder not found: {FOLDER}")
    st.stop()

# --- 2. INTERFACE ---
if not queue:
    st.success("✅ All images completed!")
    st.stop()

current_filename = queue[0]
current_full_path = os.path.abspath(os.path.join(FOLDER, current_filename))

# Center the content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title(f"Left: {len(queue)}")
    st.image(current_full_path, caption=current_filename)
    
    st.write("### Rate this image:")
    
    # Create buttons
    cols = st.columns(len(OPTIONS))
    for idx, label in enumerate(OPTIONS):
        if cols[idx].button(str(label), width='stretch'):
            
            # Decide what to save based on config
            to_save = current_full_path if SAVE_FULL_PATH else current_filename
            
            with open(CSV_FILE, 'a', newline='') as f:
                csv.writer(f).writerow([to_save, label])
            st.rerun()