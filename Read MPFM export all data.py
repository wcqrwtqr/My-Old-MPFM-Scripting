#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:51:43 2017

@author: mohammedalbatati
"""

import csv
import matplotlib.pyplot as plt
import pandas 
import numpy as np
#import datetime as dt
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

filename = askopenfilename()


#====================================
def cal_cumm(list):
    '''Pass the list of flow rates per minute and this function will compute
    the cummulative as a list ( the final value is the total cummulative)
    '''
    new_list = []
    for i in range(len(list)):
        if i == 0:
            new_list.append(0)
        else:
            x = list[i]/1440
            y = new_list[i - 1]
            z = x + y
            new_list.append(z)
    return new_list
#=====================================
def zero_alist(list):
    '''Pass a cummulative list and this function will start it from zero
    '''
    new_list = []
    for x in list:
        new_list.append(x - list[0])
    return new_list
#=====================================
def average_list_every_N(a_list,N):
    new_list = []
    for i in range (0,len(a_list),N):
        x = np.average(a_list[i:i+N])
        new_list.append(x)
    return new_list
#======================================

#with open(input('Enter the file name:'),'r')as csv_file:
# with open('MPFM.log')as csv_file:
#with open('/Users/mohammedalbatati/AnacondaProjects/Read CSV files/MPFM/MPFM.log')as csv_file:
with open(filename)as csv_file:    
    csv_data = csv.reader(csv_file, delimiter='\t')
    header = next(csv_data)

    Date=[]
    Clock=[]
    Pressure=[]
    Temperature=[]
    dP=[] # in mmBar
    std_oil_flowrate=[]
    water_flowrate=[]
    std_gas_flowrate=[]
    act_gas_flowrate=[]
    GOR_std=[]
#    act_oil_flowrate=[]
#    act_watercut=[]
    std_watercut=[]
#    act_GVF=[]
#    std_GVF=[]
    oildensity=[]
    water_density=[]
    gas_density=[]
#    density=[]
#    permittivity=[]
#    Conductivity=[]
#    act_oilmassrate=[]
#    act_watermassrate=[]
#    act_gasmassRate=[]
#    std_oilmassrate=[]
#    std_watermassrate=[]
#    std_gasmassrate=[]
#    std_accumoilvol=[]
#    AccumWaterVol=[]
#    std_AccumGasVol=[]
#    std_accumgasvol=[]
    
    for line in csv_data:
        Date.append(line[0])
        Clock.append(line[1])
        Pressure.append(float(line[2]))
        Temperature.append(float(line[3]))
        dP.append(float(line[4]))
        std_oil_flowrate.append(float(line[5]))
        water_flowrate.append(float(line[6]))
        std_gas_flowrate.append(float(line[7]))
        act_gas_flowrate.append(float(line[8]))
        GOR_std.append(float(line[9]))
#        act_oil_flowrate.append(float(line[10]))
#        act_watercut.append(float(line[11]))
        std_watercut.append(float(line[12]))
#        act_GVF.append(float(line[13]))
#        std_GVF.append(float(line[14]))
        oildensity.append(float(line[15]))
        water_density.append(float(line[16]))
        gas_density.append(float(line[17]))
#        density.append(float(line[18]))
#        permittivity.append(float(line[19]))
#        Conductivity.append(float(line[20]))
#        act_oilmassrate.append(float(line[21]))
#        act_watermassrate.append(float(line[22]))
#        act_gasmassRate.append(float(line[23]))
#        std_oilmassrate.append(float(line[24]))
#        std_watermassrate.append(float(line[25]))
#        std_gasmassrate.append(float(line[26]))
#        std_accumoilvol.append(float(line[27]))
#        AccumWaterVol.append(float(line[28]))
#        std_AccumGasVol.append(float(line[29]))
#        std_accumgasvol.append(float(line[30]))


total_liquid= [x+y for x,y in zip(std_oil_flowrate,water_flowrate)]

#========================================================
# select the data range (0 first value and -1 last value)
'''
Select the range of the data
==============================
'''
n =0
m =-1
'''
==============================
'''

#print('Max value of dP is:',int(max(dP)),' and min value is:',int(min(dP)))
# calculate the averages
average_oil_rate        = np.mean(std_oil_flowrate[n:m], dtype=int)
average_water_rate      = np.mean(water_flowrate[n:m], dtype=int)
average_GOR_total       = np.mean(GOR_std[n:m], dtype=int)
average_std_gas_rate    = np.mean(std_gas_flowrate[n:m], dtype=float)
average_total_liquid    = np.mean(total_liquid[n:m], dtype=int)
average_act_gas_rate    = np.mean(act_gas_flowrate[n:m], dtype=float)
average_dP              = np.mean(dP[n:m] , dtype=int)
average_BSW             = np.mean(std_watercut[n:m], dtype=int)
last_pressure           = Pressure[m]
last_temp               = Temperature[m]
#last_dP                 = dP[m]
last_gas_density        = gas_density[m]
last_oil_density        = oildensity[m]
last_water_density      = water_density[m]
gas_cumm                = cal_cumm(std_gas_flowrate)
water_cumm              = cal_cumm(water_flowrate)
oil_cumm                = cal_cumm(std_oil_flowrate)
first_datetime          = Date[n] + ' ' + Clock[n]
last_datetime           = Date[m] + ' ' + Clock[m]
last_gas_cumm           =gas_cumm[-1]
last_water_cumm         =water_cumm[-1]
last_oil_cumm           =oil_cumm[-1]
API                     = (141.5/(last_oil_density/1000) - 131.5)
choke_size              =input('enter the choke size:')

#=====================================================
#Dictionary for the summary of results
my_summary = {'From':first_datetime,
              'To':last_datetime,
              'Delta time':'??????',
              'Choke Size':str(choke_size),
              'WHP':last_pressure,
              'WHT':last_temp,
              'Diff dP':average_dP,
              'Oil Rate':average_oil_rate,
              'Water Rate':average_water_rate,
              'Liquid Rate':average_total_liquid,
              'Gas Rate':average_std_gas_rate,
              'Actual Gas Rate':average_act_gas_rate,
              'Total GOR':average_GOR_total,
              'Gas SG':last_gas_density,
              'Oil SG':last_oil_density,
              'Oil API':API,
              'BSW':average_BSW,
              'Cumm Gas':last_gas_cumm,
              'Cumm Oil':last_oil_cumm,
              'Cumm Water':last_water_cumm}

#========================================================
fig1, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(water_flowrate[n:m],'b-', label='Water Rate')
ax1.plot(std_oil_flowrate[n:m],'k', label = 'Oil Rate')
ax2.plot(std_gas_flowrate[n:m],'y-', label='Gas Rate')

ax1.set_ylabel('Oil & Water Rate (bbl/day)',color='k')
ax1.tick_params('y', colors='k')
ax2.set_ylabel('Gas Flow Rate)',color='k')
fig1.tight_layout()
ax1.set_ylim(int(min(std_oil_flowrate)),int(max(std_oil_flowrate)))
ax2.set_ylim(int(min(std_gas_flowrate)),int(max(std_gas_flowrate)+3))
ax1.legend()
ax2.legend()


#========================================================
fig2, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(dP[n:m],'y-', label='dP')
ax1.plot(Pressure[n:m],'b', label = 'Pressure')
ax2.plot(Temperature[n:m],'r-', label='Temperature')

ax1.set_ylabel('pressure (psi) & dP (mmBar)',color='k')
ax1.tick_params('y', colors='k')
ax2.set_ylabel('Temperature (DegC)',color='k')
#fig2.tight_layout()
#ax1.set_ylim(int(min(dP[n:m])),int(max(dP[n:m])))
#ax2.set_ylim(int(min(Temperature[n:m])),int(max(Temperature[n:m])))
ax1.legend()
ax2.legend()

#========================================================
fig3, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(oil_cumm[n:m],'y-', label='Cumm Oil')
ax1.plot(water_cumm[n:m],'b-', label = 'Cumm Water')
ax2.plot(gas_cumm[n:m],'r-', label='Cumm Gas')

ax1.set_ylabel('Cumm oil and water',color='k')
ax1.tick_params('y', colors='k')
ax2.set_ylabel('Cumm gas',color='k')
#fig2.tight_layout()
#ax1.set_ylim(int(min(dP[n:m])),int(max(dP[n:m])))
#ax2.set_ylim(int(min(Temperature[n:m])),int(max(Temperature[n:m])))
ax2.set_ylim(0,5)
ax1.legend()
ax2.legend()

#========================================================
#print(min(Temperature[n:m]))
fig4, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(GOR_std[n:m],'k', label = 'GOR')
ax2.plot(std_oil_flowrate[n:m],'b-', label='Oil Rate')

ax1.set_ylabel('GOR',color='k')
#ax1.tick_params('y', colors='k')
ax2.set_ylabel('Oil Rate',color='b')
#fig.tight_layout()
ax1.set_ylim(0,int(max(GOR_std[n:m])))
ax2.set_ylim(0,int(max(std_oil_flowrate[n:m])) + 2000)
ax1.legend()
ax2.legend()
plt.show()

#======================================================
#Export data to csv files
# select the path to save the report file
fileoutputpath = askdirectory()
file_full_path_report = fileoutputpath + '/MPFM_Report.csv'

'''
# Exporting the main data with all values
pd = pandas.DataFrame(list(zip(Date[n:m],Clock[n:m],Pressure[n:m],Temperature[n:m],dP[n:m],
                               std_oil_flowrate[n:m],
                               water_flowrate[n:m],
                               total_liquid[n:m],
                               std_gas_flowrate[n:m],
                               act_gas_flowrate[n:m],
                               GOR_std[n:m],
                               gas_density[n:m],
                               oildensity[n:m],
                               std_watercut[n:m])),
                                columns = ['Date','Time','WHP',
                                'WHT','dP','Oil Rate','Water Rate','Liquid Rate',
                                'Gas Rate','Act Gas Rate','GOR',
                                'Gas Density','Oil Density','BSW'])
'''

# Exporting the main data with average reduced points:
N = 5
new_date = Date[n:m:N]
new_Clock = Clock[n:m:N]
new_pressure = average_list_every_N(Pressure[n:m],N)
new_temp = average_list_every_N(Temperature[n:m],N)
new_dP = average_list_every_N(dP[n:m],N)
new_oil_rate = average_list_every_N(std_oil_flowrate[n:m],N)
new_water_rate = average_list_every_N(water_flowrate[n:m],N)
new_liquid_rate = average_list_every_N(total_liquid[n:m],N)
new_std_gas_rate = average_list_every_N(std_gas_flowrate[n:m],N)
new_act_gas_rate = average_list_every_N(act_gas_flowrate[n:m],N)
new_GOR = average_list_every_N(GOR_std[n:m],N)
new_gas_dinsity = average_list_every_N(gas_density[n:m],N)
new_oil_dinsity = average_list_every_N(oildensity[n:m],N)
new_water_cut = average_list_every_N(std_watercut[n:m],N)
                               
pd = pandas.DataFrame(list(zip(new_date,new_Clock,new_pressure,new_temp,new_dP,new_oil_rate,new_water_rate,
                               new_liquid_rate,new_std_gas_rate,new_act_gas_rate,new_GOR,new_gas_dinsity,
                               new_oil_dinsity,new_water_cut)),
                                columns = ['Date','Time','WHP',
                                'WHT','dP','Oil Rate','Water Rate','Liquid Rate',
                                'Gas Rate','Act Gas Rate','GOR',
                                'Gas Density','Oil Density','BSW'])
#pd.to_csv('MPFM_Report.csv',line_terminator='\n')
pd.to_csv(file_full_path_report,line_terminator='\n')
#======================================================
#Export Summary sheet to csv files 

file_full_path_summary = fileoutputpath + '/summary.csv'
#with open('MPFM_Summary.csv','w') as f:
with open(file_full_path_summary,'w') as f:
    my_writer = csv.writer(f)  
    my_writer.writerow(my_summary.keys())
    my_writer.writerow(my_summary.values())
    
   
#======================================================
print('The file_________\n {} \n_________was processed'.format(filename))
print('From the time {0} to {1}'.format(first_datetime,last_datetime))

 
  
    


