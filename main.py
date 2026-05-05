import os
import string
from torchvision import datasets, transforms
from torchvision.utils import save_image
import torchvision.transforms.functional as TF

# =========================
# CONFIG
# =========================
OUTPUT_DIR = "dataset_uppercase"
IMAGES_PER_CLASS = 350

# =========================
# LOAD DATASET (QUAN TRỌNG)
# =========================
transform = transforms.Compose([
    transforms.ToTensor()
])

dataset = datasets.EMNIST(
    root='./data',
    split='byclass',   # dùng byclass
    train=True,
    download=True,
    transform=transform
)

# =========================
# LABEL MAP (EMNIST byclass)
# =========================
# 0-9: digits
# 10-35: uppercase A-Z
# 36-61: lowercase a-z

uppercase_labels = {i: chr(ord('A') + i - 10) for i in range(10, 36)}

# =========================
# CREATE FOLDER
# =========================
for letter in uppercase_labels.values():
    os.makedirs(os.path.join(OUTPUT_DIR, letter), exist_ok=True)

counter = {letter: 0 for letter in uppercase_labels.values()}

# =========================
# PROCESS
# =========================
for img, label in dataset:
    if label in uppercase_labels:
        letter = uppercase_labels[label]

        # FIX XOAY
        img = TF.rotate(img, -90)
        img = TF.hflip(img)

        if counter[letter] < IMAGES_PER_CLASS:
            save_path = os.path.join(
                OUTPUT_DIR,
                letter,
                f"{letter}_{counter[letter]}.png"
            )

            save_image(img, save_path)
            counter[letter] += 1

    if all(v >= IMAGES_PER_CLASS for v in counter.values()):
        break

print("DONE!")