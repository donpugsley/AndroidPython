from plots import *
import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

from tkinter import filedialog as fd
import sys
sys.path.append(".")

from pathlib import Path

def latest_file(path: Path, pattern: str = "*"):
    files = path.glob(pattern)
    return max(files, key=lambda x: x.stat().st_ctime)
    
# Change this to read the most recent file, or pop up a file picker
#fn = "/storage/emulated/0/Documents/Pydroid3/serial_20230408_075114.txt"
#fn = fd.askopenfilename()

list_of_files = glob.glob('./*.txt') 
fn = max(list_of_files, key=os.path.getctime)

df = pd.read_csv(fn, delim_whitespace=True,parse_dates=True,verbose=True,header=None,names=["Time","Count","MX","MY","MZ","AX","AY","AZ","GX","GY","GZ","Bar","C"],skiprows=1,skipfooter=1,engine='python')

x = df["MX"]
y = df["MY"]
z = df["MZ"]
t = df["Time"]

threeplot(t,x,y,z,"nT","Test")

threelsd(x,y,z,200,"nT","Test","X","Y","Z",6)

#lsd(tf(x,y,z),200,"nT","Test")

#oneplot(t,tf(x,y,z),"nT","Test")





#tf = np.sqrt(df["MX"]*df["MX"]+df["MY"]*df["MY"]+df["MZ"]*df["MZ"])
#plt.scatter(df["Time"],tf)
#plt.title('VMR Total Field')
#plt.xlabel('Time')
#plt.ylabel('nT')
#plt.grid(visible=True)
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()


plt.show()
