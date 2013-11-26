#!/usr/bin/python

from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(description="Resave jpeg files multiple times")
parser.add_argument("-n", "--number", default=500, type=int,
        help="Number of resaves, default: 500")
parser.add_argument("-q", "--quality", default=95, type=int,
        help="Image quality between 1 and 95, default: 95")
parser.add_argument("-k", "--keep", action="store_true",
        help="Keep all intermediate files, default: no")
parser.add_argument("filename") 

args = parser.parse_args()

if args.quality < 1 or args.quality > 95:
    print("Error: Quality should be between 1 and 95")
    exit(1)

name = args.filename
name = name.split(".")[0]

img = Image.open(args.filename)
for i in range(args.number):
    new_name = name + "_" + str(i) + ".jpg" 
    img.save(new_name, quality=args.quality)
    img = Image.open(new_name)
    if not (args.keep or i == args.number - 1):
        os.remove(new_name)


