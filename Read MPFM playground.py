#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:51:43 2017

@author: mohammedalbatati
"""

import csv
#import matplotlib.pyplot as plt
#import pandas 
import numpy as np
#import datetime as dt
#from tkinter.filedialog import askopenfilename

#filename = askopenfilename()

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
#with open(input('Enter the file name:'),'r')as csv_file:
with open('MPFM.log')as csv_file:
#with open(filename)as csv_file:    
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
    GOR_std=[]
    std_watercut=[]




    
    for line in csv_data:
        Date.append(line[0])
        Clock.append(line[1])
        Pressure.append(float(line[2]))
        Temperature.append(float(line[3]))
        dP.append(float(line[4]))
        std_oil_flowrate.append(float(line[5]))
        water_flowrate.append(float(line[6]))
        std_gas_flowrate.append(float(line[7]))
        GOR_std.append(float(line[9]))
        std_watercut.append(float(line[12]))


def average_list_every_N(a_list,N):
    new_list = []
    for i in range (0,len(a_list),N):
        x = np.average(a_list[i:i+N])
        new_list.append(x)
    return new_list

GOR_averege = average_list_every_N(GOR_std,5)

#print(len(GOR_averege))
#print(len(GOR_std))
#
#
#print(np.average(GOR_std[-8:-1]))
#print(GOR_averege[-1])


for idx , val in enumerate(GOR_averege[0:20]):
    print(idx,format(val,'0.2f'))



#========================================================
# select the data range (0 first value and -1 last value)
#n =400
#m =750
#print('Max value of dP is:',int(max(dP)),' and min value is:',int(min(dP)))
# calculate the averages
#average_oil_rate        = np.mean(std_oil_flowrate[n:m], dtype=int)
#average_water_rate      = np.mean(water_flowrate[n:m], dtype=int)
#average_GOR_total       = np.mean(GOR_std[n:m], dtype=int)
#average_std_gas_rate    = np.mean(std_gas_flowrate[n:m], dtype=float)
#average_total_liquid    = np.mean(total_liquid[n:m], dtype=int)
#average_act_gas_rate    = np.mean(act_gas_flowrate[n:m], dtype=float)
#average_dP              = np.mean(dP[n:m] , dtype=int)
#average_BSW             = np.mean(std_watercut[n:m], dtype=int)
#last_pressure           = Pressure[m]
#last_temp               = Temperature[m]
##last_dP                 = dP[m]
#last_gas_density        = gas_density[m]
#last_oil_density        = oildensity[m]
#last_water_density      = water_density[m]
#gas_cumm                = cal_cumm(std_gas_flowrate)
#water_cumm              = cal_cumm(water_flowrate)
#oil_cumm                = cal_cumm(std_oil_flowrate)
#first_datetime          = Date[n] + ' ' + Clock[n]
#last_datetime           = Date[m] + ' ' + Clock[m]
#last_gas_cumm           =gas_cumm[-1]
#last_water_cumm         =water_cumm[-1]
#last_oil_cumm           =oil_cumm[-1]
#API                     = (141.5/(last_oil_density/1000) - 131.5)
#choke_size              =input('enter the choke size:')

#=====================================================
#Dictionary for the summary of results
#my_summary = {'From':first_datetime,
#              'To':last_datetime,
#              'Delta time':'??????',
#              'Choke Size':str(choke_size),
#              'WHP':last_pressure,
#              'WHT':last_temp,
#              'Diff dP':average_dP,
#              'Oil Rate':average_oil_rate,
#              'Water Rate':average_water_rate,
#              'Liquid Rate':average_total_liquid,
#              'Gas Rate':average_std_gas_rate,
#              'Actual Gas Rate':average_act_gas_rate,
#              'Total GOR':average_GOR_total,
#              'Gas SG':last_gas_density,
#              'Oil SG':last_oil_density,
#              'Oil API':API,
#              'BSW':average_BSW,
#              'Cumm Gas':last_gas_cumm,
#              'Cumm Oil':last_oil_cumm,
#              'Cumm Water':last_water_cumm}

'''
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

ax1.plot(std_watercut[n:m],'k', label = 'GOR')
ax2.plot(std_oil_flowrate[n:m],'b-', label='Oil Rate')

ax1.set_ylabel('BSW',color='k')
#ax1.tick_params('y', colors='k')
ax2.set_ylabel('Oil Rate',color='b')
#fig.tight_layout()
#ax1.set_ylim(0,int(max(std_watercut[n:m])))
#ax2.set_ylim(0,int(max(std_oil_flowrate[n:m])) + 2000)
ax1.legend()
ax2.legend()
plt.show()
'''
#======================================================
#print('The file_________\n {} \n_________was processed'.format(filename))
#print('From the time {0} to {1}'.format(first_datetime,last_datetime))



    
    
    
  
    


