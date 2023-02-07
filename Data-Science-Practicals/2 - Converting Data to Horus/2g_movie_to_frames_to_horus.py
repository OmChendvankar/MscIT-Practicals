# PRACTICAL 2.  CONVERTING DATA TO HORUS
# 2G. Movie to Frames to image
# Om V Chendvankar
# University Dept of Information Technology

# Part 1 - Video to Frames

import os
import shutil
import cv2

sInputFileName='D:\\M.Sc.IT\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Dog.mp4'
print('Converting Movie to Frames')
vidcap = cv2.VideoCapture(sInputFileName)
success,image = vidcap.read()

success

image.shape


count = 0
while success:
  success,image = vidcap.read()
  sFrame=sDataBaseDir + str('/dog-frame-' + str(format(count, '04d'))+ '.jpg')
  print('Extracted: ', sFrame)
  
  cv2.imwrite(sFrame, image)
  if os.path.getsize(sFrame) == 0:
    count += -1
    os.remove(sFrame)
    print('Removed: ', sFrame)
  if cv2.waitKey(10) == 27: # exit if Escape is hit
    break
  count += 1
print('=====================================================')
print('Generated : ', count, ' Frames')
print('=====================================================')
print('Movie to Frames HORUS - Done')

# Part 2 - Frames to Horus

from skimage import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Input Agreement ============================================
sDataBaseDir='/content/output'

f=0
for file in os.listdir(sDataBaseDir):
  if file.endswith(".jpg"):
     f = f+1
     sInputFileName=os.path.join(sDataBaseDir, file)
     print('Process : ', sInputFileName)
     InputData = io.imread(sInputFileName)
     print('Input Data Values ===================================')
     print('X: ',InputData.shape[0])
     print('Y: ',InputData.shape[1])
     print('RGBA: ', InputData.shape[2])
     print('=====================================================')

     ProcessRawData=InputData.flatten()
     y=InputData.shape[2] + 2
     x=int(ProcessRawData.shape[0]/y)
     ProcessFrameData=pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
     ProcessFrameData['Frame']=file
     print('=====================================================')
     print('Process Data Values =================================')
     print('=====================================================')
     plt.imshow(InputData)
     plt.show()
     if f == 1:
       ProcessData=ProcessFrameData
     else:
       ProcessData=ProcessData.append(ProcessFrameData)

if f > 0:
  sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue','FrameName']
  ProcessData.columns=sColumns
  print('=====================================================')
  ProcessFrameData.index.names =['ID']
  print('Rows: ',ProcessData.shape[0])
  print('Columns :',ProcessData.shape[1])
  print('=====================================================')
  # Output Agreement ===========================================
  OutputData=ProcessData
  print('Storing File')
  sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Outputs\\HORUS-Movie-Frame.csv'
  OutputData.to_csv(sOutputFileName, index = False)
print('=====================================================')
print('Processed ; ', f,' frames')
print('=====================================================')
print('Movie to HORUS - Done')
print('=====================================================')
