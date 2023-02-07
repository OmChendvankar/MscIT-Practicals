
# PRACTICAL 2 - CONVERTING DATA TO HORUS
# 2D. AUDIO TO HORUS
# OM V CHENDVANKAR - 17-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_info(aname, a,r):
    print ('----------------')
    print ("Audio:", aname)
    print ('----------------')
    print ("Rate:", r)
    print ('----------------')
    print ("shape:", a.shape)
    print ("dtype:", a.dtype)
    print ("min, max:", a.min(), a.max())
    print ('----------------')
    plot_info(aname, a,r)

def plot_info(aname, a,r):        
    sTitle= 'Signal Wave - '+ aname + ' at ' + str(r) + 'hz'
    plt.title(sTitle)
    sLegend=[]
    for c in range(a.shape[1]):
        sLabel = 'Ch' + str(c+1)
        sLegend=sLegend+[str(c+1)]
        plt.plot(a[:,c], label=sLabel)
    plt.legend(sLegend)
    plt.show()

sInputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\2ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)


show_info("2 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Outputs\\Audio2chtoHORUS.csv'
OutputData.to_csv(sOutputFileName, index = False)


# 4ch-sound.wav
sInputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\4ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)


show_info("4 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2', 'Ch3', 'Ch4']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Outputs\\Audio4chtoHORUS.csv'
OutputData.to_csv(sOutputFileName, index = False)


# 6ch-sound.wav
sInputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\6ch-sound.wav'
print('=====================================================')
print('Processing : ', sInputFileName)
print('=====================================================')
InputRate, InputData = wavfile.read(sInputFileName)


show_info("6 channel", InputData,InputRate)
ProcessData=pd.DataFrame(InputData)
sColumns= ['Ch1','Ch2','Ch3','Ch4','Ch5','Ch6']
ProcessData.columns=sColumns
OutputData=ProcessData
sOutputFileName='D:\\M.Sc.IT\\Sem 1\\Data Science\\PRACTICAL\\2 CONVERTING DATA TO HORUS\\Outputs\\Audio6chtoHORUS.csv'
OutputData.to_csv(sOutputFileName, index = False)
