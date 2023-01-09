import os

ORIG_BASE_PATH = "D:/EPITA/Computer Vision/Project_2/raccoons"
ORIG_IMAGES = os.path.sep.join([ORIG_BASE_PATH, "images"])
ORIG_ANNOTS = os.path.sep.join([ORIG_BASE_PATH, "annotations"])
BASE_PATH = "D:/EPITA/Computer Vision/Project_2/dataset"
POSITVE_PATH = os.path.sep.join([BASE_PATH, "raccoon"])
NEGATIVE_PATH = os.path.sep.join([BASE_PATH, "no_raccoon"])
MAX_PROPOSALS = 2000
MAX_PROPOSALS_INFER = 200
MAX_POSITIVE = 30
MAX_NEGATIVE = 10
INPUT_DIMS = (224, 224)
MODEL_PATH = "D:/EPITA/Computer Vision/Project_2/output/"
ENCODER_PATH = "D:/EPITA/Computer Vision/Project_2/output/enocoder.pickle"
MIN_PROBA = 0.99
CSV = "D:/EPITA/Computer Vision/Project_2/dataset/train_labels_.csv"