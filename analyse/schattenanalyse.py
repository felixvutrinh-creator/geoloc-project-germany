import argparse as ap
import json 
import math 
import pathlib as pl
import numpy as np
import cv2 as cv

def shadow_suggestion_mask(image_path: str, output_path: str):
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.ColorConversionCodes.BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    _, mask = (cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU))
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv.contourArea(contour) > 100:
            cv.drawContours(image, [contour], -1, (0, 0, 255), 2)
    cv.imwrite(output_path, image)
    return mask
if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    args = parser.parse_args()
    shadow_suggestion_mask(args.input_path, args.output_path)
    print(f"Shadow suggestion mask saved to {args.output_path}")

