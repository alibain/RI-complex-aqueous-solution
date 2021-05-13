# import packages
import pandas as pd
import numpy as np
import math
import sys
import os

# Input Parameters 
# Possible ions : NH4, Ca, Li, Mg, Na, K, Cl, HSO4, SO4, Br, NO3, H
# Possible organics : malonic, glutaric, citric, sucrose, mannose 
# Each speciece entered as ['name', mass fraction]
input=[['NH4',0.0546],['SO4',0.14539],['glutaric acid',0.2]]
#wavelength=np.array([0.589,0.650])
wavelength=np.linspace(0.3,0.7,5,endpoint=True)

#Output file name and location
dir_name='/Users/alisonbain/Documents/Python/'
base_filename='test1-NH42-0.0546-SO4-0.14539-GA-0.2'
outname=os.path.join(dir_name, base_filename + ".csv")
print(outname)

solutesdf = pd.DataFrame(input,columns=['solute','wBi'])
solutesdf = solutesdf.T
solute=solutesdf.iloc[0]
wBi=solutesdf.iloc[1]
wB=sum(wBi)
wA=1-wB

# Import Oscillator data for solute
file=("/Users/alisonbain/Documents/Python/oscillator-parameters.txt") #full path for file
dat=pd.read_table(file) #read file
df2 = dat.set_index("Ion", drop = True)
iondata=df2.loc[solute,:]
Bi=iondata.loc[:,"B"]
nu0i=iondata.loc[:,"v0"]

# Refractive index of pure water from Daimon and Masumura 2007
Awat=np.array([5.689093832e-1,1.719708856e-1,2.062501582e-2,1.123965424e-1])
lambda2=np.array([5.110301794e-3,1.825180155e-2,2.624158904e-2,1.067505178e1])

if len(wavelength) == 1:
    t=[]
    for j in range(len(Awat)):
        top=Awat[j]*wavelength**2
        bottom=(wavelength**2-lambda2[j])
        t1=top/bottom
        t.append(t1)
    n_water=(1+sum(t))**0.5
else:    
    n_water=[]
    for i in range(len(wavelength)):
        t=[]
        for j in range(len(Awat)):
            top=Awat[j]*wavelength[i]**2
            bottom=(wavelength[i]**2)-lambda2[j]
            t1=top/bottom
            t.append(t1)
        l=(1+sum(t))**0.5
        n_water.append(l)

# convert wavelength to frequency
def freq_to_wavelength(nu):
    return 1/nu

# Calculate n with the oscillator model
n=[]
for j in range(len(wavelength)):
    print("j=",j)
    osc=[]
    for k in range(len(solute)):
        print("k=",k)
        osci=(wBi[k]*2*Bi[k]*nu0i[k])/(math.pi*(nu0i[k]**2-freq_to_wavelength(wavelength[j])**2))
        osc.append(osci)
    oscions=sum(osc)
    if len(wavelength) == 1:
        n=1+oscions+wA*(n_water[0]-1)
    else:
        n1=1+oscions+wA*(n_water[j]-1)
        n.append(n1)
print(n)    

# Export refractive index data to csv
data = {'wavelength' : wavelength,'n' : n}
outputdf=pd.DataFrame(data)
outputdf.to_csv(os.path.join(dir_name, base_filename + ".csv"), index = False, header=True)