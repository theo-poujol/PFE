import sys
import argparse
import os
import torch

def main(args):
  image_folder = args.image_folder
  print(image_folder)

  # Calcul des masques

  os.system("python3 ./interactive_grabcut.py " + image_folder)

  shapes = ['carré', 'rectangle', 'triangle', 'boule']

  is_ok = False

  while(not is_ok):

    print('####################################')
    print("Choisissez quelle forme correspond le mieux à l'objet")
    print("1 - Carré")
    print("2 - Rectangle")
    print("3 - Triangle")
    print("4 - Boule")
    print('####################################')

    selected_idx_obj = input("Entrer le numéro de la forme voulue : ")


    if ( isinstance(int(selected_idx_obj), int) and int(selected_idx_obj) >= 1 and int(selected_idx_obj) <= 4 ) :
      is_ok = True

  

  print("Vous avez choisis la forme " + shapes[int(selected_idx_obj) - 1])
  

  # Calcul de la sphère unitaire

  obj_folder = "./shapes/"

  obj_file = obj_folder + selected_idx_obj + ".obj"

  print(obj_file + " va être chargé")

  command_sphere = "./spherical_harmonic/build/main " + obj_file + " ./sphere/output"

  os.system(command_sphere)


  # Calcul de la position de la caméra 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_folder", type=str)
    args = parser.parse_args()
    main(args)


