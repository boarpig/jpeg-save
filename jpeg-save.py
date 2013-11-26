#!/usr/bin/python

from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="Resave jpeg files multiple times")
parser.add_argument("-n", action="store", nargs=1, default=500, type=int,
                    help="How many times to resave, default=500")
parser.add_argument("filename") 

