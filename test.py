# You may need to restart your runtime prior to this, to let your installation take effect
# Some basic setup:
# Setup detectron2 logger
import sys
import argparse
import os

def main(args):
  image_folder = args.image_folder
  print(image_folder)

  os.system("python3 ./interactive_grabcut.py " + image_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_folder", type=str)
    args = parser.parse_args()
    main(args)
