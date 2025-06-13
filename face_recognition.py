
import argparse
import os

import torch


def face_recognition(args=None):
    return []


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", "-v", type=str, default="v0.01",
            help="version: x.mn. x is formal release version; m is verified version; n is minor version")

    parser.add_argument("--model", type=str, default="weights/yolov8n.pt")
    parser.add_argument("--cfg", type=str, default="cfg/yolov8n.yaml",)

    parser.add_argument("--database", type=str, default="weights/database.pt")
    parser.add_argument("--threshold", type=float, default=0.8) # matching threshold

    parser.add_argument("--input", type=str, default="examples/bus.jpg", help="input image file or folder")
    parser.add_argument("--ouput", type=str, default="examples/bus.jpg", help="output image file or folder")

    parser.add_argument("--batch", type=int, default=1)
    parser.add_argument("--channel", type=int, default=3)
    parser.add_argument("--height", type=int, default=224)
    parser.add_argument("--width", type=int, default=224)


    args = parser.parse_args()
    results = list()
    results.append(
        dict(
            meta = "unkown",
            indice = 0,
            )
    )

    faces = face_recognition(args=args)
    for face in faces:
        results.append(face)
    return results


if __name__ == "__main__":
    results = main()
    print(results)


