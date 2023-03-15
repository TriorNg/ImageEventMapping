# Image Processing Packages
from PIL import Image
import glob
from PIL.ExifTags import TAGS

# Directory Control Packages
import os
import shutil
import errno

# Date Time Control Packages
from datetime import datetime
from datetime import date

images = glob.glob("*.jpg") # Grab the files
image_dict=dict() # Dictionary for all the images' metadata

# Get paths to move files later
parent_path = os.getcwd()
try:
    day1_path = os.mkdir(os.path.join(parent_path,"Day 1"))
    day2_path = os.mkdir(os.path.join(parent_path,"Day 2"))
    day2_path = os.mkdir(os.path.join(parent_path,"Day 3"))
except OSError as e:
    if e.errno == errno.EEXIST:
        print('Directory already there.')
    else:
        raise
# Set path if folders are created
day1_path = os.path.join(parent_path,"Day 1")
day2_path = os.path.join(parent_path,"Day 2")
day3_path = os.path.join(parent_path,"Day 3")


# Time Conversion for date comparison
timeFormat = "%Y:%m:%d %H:%M:%S" #Time Format
day1 = datetime.strptime("2023:02:24 09:00:00",timeFormat) # Limit for day 1 
day2 = datetime.strptime("2023:02:25 09:00:00",timeFormat) # Limit for day 1 and day 2, beyond this is day 3
for i in images:
    image = Image.open(i)
    info_dict={
        "Filename" : image.filename,
        "Date": image.getexif().get(306)
    }
    image_dict[info_dict['Filename']] = datetime.strptime(info_dict['Date'],timeFormat)


for label,value in image_dict.items():
    if value < day1:
        print(f"Day 1: {label :25}: {value}< {day1}")
    elif value > day1 and value < day2:
        print(f"Day 2: {label :25}: {value}< {day2}")
    else:
        print(f"Day 3: {label :25}: {value}> {day2}")
