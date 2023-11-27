from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM]

# Images config
IMAGES_DIR = ROOT / 'test' / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'weapons2.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'weapons2Detected.jpg'

# Videos config
VIDEO_DIR = ROOT / 'test' / 'videos'
VIDEO_1_PATH = VIDEO_DIR / 'beyonce-gun.gif'
VIDEO_2_PATH = VIDEO_DIR / 'knife-deep-thinking.gif'
VIDEO_3_PATH = VIDEO_DIR / 'gun-pistol.gif'
VIDEO_4_PATH = VIDEO_DIR / 'machine-gun-498-x-247-gif-jdurh7cgwvbh401x.gif'
VIDEO_5_PATH = VIDEO_DIR / 'ITna.gif'
VIDEO_6_PATH = VIDEO_DIR / 'tumblr_mus2ooy2iX1sl27r8o1_500.gif'
VIDEO_7_PATH = VIDEO_DIR / '4cfc146df61c2df780e1bb8bd3744c9a.gif'
VIDEO_8_PATH = VIDEO_DIR / 'e4fb81f935a0fec378f82c7b5c0173c6.gif'
VIDEO_9_PATH = VIDEO_DIR / 'sniper.gif'
VIDEOS_DICT = {
    'Video 1': VIDEO_1_PATH,
    'Video 2': VIDEO_2_PATH,
    'Video 3': VIDEO_3_PATH,
    'Video 4': VIDEO_4_PATH,
    'Video 5': VIDEO_5_PATH,
    'Video 6': VIDEO_6_PATH,
    'Video 7': VIDEO_7_PATH,
    'Video 8': VIDEO_8_PATH,
    'Video 9': VIDEO_9_PATH,
}

# ML Model config
MODEL_DIR = ROOT / 'runs'/'detect' / 'train' / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'

# Webcam
WEBCAM_PATH = 0
