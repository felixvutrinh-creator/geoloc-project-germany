from typing import Any


import argparse as ap
import json 
import math 
import pathlib as pl
import numpy as np
import cv2 as cv
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator


def shadow_suggestion_mask(image_path: str, output_path: str):
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    _, mask = (cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU))
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv.contourArea(contour) > 100:
            cv.drawContours(image, [contour], -1, (0, 0, 255), 2)
    cv.imwrite(output_path, image)
    # Adaptiv thresholding
    adaptive_threshold = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 101, 2)
    cv.imwrite(f"{output_path}_adaptive_threshold.png", adaptive_threshold)
    return adaptive_threshold

def shaodow_suggestion_mask_sam(image_path: str, output_path: str):
    image = cv.imread(image_path)
    sam = sam_model_registry["vit_b"](checkpoint="sam_vit_b_01ec64.pth")
    mask_generator = SamAutomaticMaskGenerator(sam)
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    masks = mask_generator.generate(image_rgb)
    for i, mask in enumerate(masks[:10]):
        mask_image = mask["segmentation"]
        mask_image = (mask["segmentation"] * 255).astype(np.uint8)
        cv.imwrite(f"{output_path}_mask_{i}.png", mask_image)

        


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    args = parser.parse_args()
    shaodow_suggestion_mask_sam(args.input_path, args.output_path)

    print(f"Shadow suggestion mask saved to {args.output_path}")