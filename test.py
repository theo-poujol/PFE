# You may need to restart your runtime prior to this, to let your installation take effect
# Some basic setup:
# Setup detectron2 logger
import sys
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import cv2
import torch
import matplotlib.pyplot as plt

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import MetadataCatalog
coco_metadata = MetadataCatalog.get("coco_2017_val")

# import PointRend project
from detectron2.projects import point_rend
from detectron2.data import transforms as T
from detectron2.projects.point_rend.mask_head import calculate_uncertainty
from detectron2.projects.point_rend.point_features import get_uncertain_point_coords_with_randomness

from detectron2.layers import interpolate
from detectron2.projects.point_rend.mask_head import calculate_uncertainty
from detectron2.projects.point_rend.point_features import (
    get_uncertain_point_coords_on_grid,
    point_sample,
    point_sample_fine_grained_features,
)




idx = 1

window_name = 'test mask'

img_list = sys.argv[1:]


'''def plot_mask(mask, title="", point_coords=None, figsize=10, point_marker_size=5):
  H, W = mask.shape
  plt.figure(figsize=(figsize, figsize))

  fig = plt.figure(frameon=False)
  fig.set_size_inches(W, H)
  ax = plt.Axes(fig, [0., 0., 1., 1.])
  ax.set_axis_off()
  fig.add_axes(ax)
  ax.imshow(mask,interpolation="nearest", cmap=plt.get_cmap('gray') ,aspect='auto')
  #plt.imshow(mask, interpolation="nearest", cmap=plt.get_cmap('gray'))

  newpath = "./mask" + str(idx) + ".png"
  fig.savefig(newpath)


  #plt.savefig('./mask.png', bbox_inches='tight')
  #if point_coords is not None:
    #plt.scatter(x=point_coords[0], y=point_coords[1], color="red", s=point_marker_size, clip_on=True) 
  #plt.xlim(-0.5, W - 0.5)
  #plt.ylim(H - 0.5, - 0.5)
  plt.show()
'''

cfg = get_cfg()
# Add PointRend-specific config
point_rend.add_pointrend_config(cfg)
# Load a config from file
cfg.merge_from_file("detectron2/projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_50_FPN_3x_coco.yaml")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
# Use a model from PointRend model zoo: https://github.com/facebookresearch/detectron2/tree/master/projects/PointRend#pretrained-models
cfg.MODEL.WEIGHTS = "detectron2://PointRend/InstanceSegmentation/pointrend_rcnn_R_50_FPN_3x_coco/164955410/model_final_edd263.pkl"
predictor = DefaultPredictor(cfg)

def getMask(im):

  outputs = predictor(im)

  v = Visualizer(im[:, :, ::-1], coco_metadata, scale=1.2, instance_mode=ColorMode.IMAGE_BW)
  point_rend_result = v.draw_instance_predictions(outputs["instances"].to("cpu")).get_image()
  print("Mask R-CNN with PointRend")
  cv2.imshow(window_name, point_rend_result)
  cv2.waitKey(0) 
    
  #closing all open windows 
  cv2.destroyAllWindows()


for img in img_list:
  print('coucou')
  path = "./" + img

  im = cv2.imread(path)
  getMask(im)

  idx = idx + 1