import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import plotly.express as px
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from Calc import *
from Calc_pa import *
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import matplotlib

plt.switch_backend('agg')







def integrate(arr,t) :
    ad = np.zeros([len(arr)])
    print(len(arr),ad)
    ad[0] = arr[0];
    for i in range(len(arr)-1) :
        ad[i+1] =arr[i+1] + ad[i] 
    # ad = ad*(t[1]-t[0])
    return ad





# path
path_S_o = "Series_open.png"
path_S_c = "Series_close.png"  
path_P_o = "Parallel_open.png"
path_P_c = "Parallel_close.png"
# Using cv2.imread() method
img_S1 = cv.imread(path_S_o)
img_S2 = cv.imread(path_S_c)
img_P1 = cv.imread(path_P_o)
img_P2 = cv.imread(path_P_c)





# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig1 = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .15])

# Plot!






# add_selectbox = st.sidebar.text_input("Your name", key="name")

# Add a slider to the sidebar:
a1 = st.sidebar.selectbox(
    'Select the type of circuit :',
    ('Series', 'Parallel'),key="Circuit_type")
a2 = st.sidebar.selectbox(
    'Select Switch Position:',
    ('On', 'Off'),key='Switch_position')

if (a1 == 'Series' ) and (a2 == 'Off' ) :
    st.image(img_S1, channels="BGR",width=650)
    swi = 1;
if (a1 == 'Series' ) and (a2 == 'On' ) :
    st.image(img_S2, channels="BGR",width=650);swi = 2
if (a1 == 'Parallel' ) and (a2 == 'Off' ) :
    st.image(img_P1, channels="BGR",width=650);swi = 3
if (a1 == 'Parallel' ) and (a2 == 'On' ) :
    st.image(img_P2, channels="BGR",width=650);swi = 4



R =  st.sidebar.slider('Select resistor Value :', 1.00, 100.0, 2.0)

L =  st.sidebar.slider('Select inductor Value :', 0.01, 10.00, 1.00)
C =  st.sidebar.slider('Select capacitor value :', 10e-6, 0.1, 0.05)
Vs =  st.sidebar.slider('Volatage source Value :', 0.00, 100.00, 24.00)
increment =  st.sidebar.slider('time Value :', 0.00, 100.00, 10.00)


s = 0

if s == 0 :
    xs = [];ys = [];itt= 0; V_0 =  0;t0=0;s= s+1;Ltemp = 0;Rtemp = 0;Ctemp = 0;Vstemp = 0; t_= 0;t = np.linspace(0,increment,1000); 
else :
    V_0 = V[-1]
dV_dt = V_0/C;
check = (L == Ltemp) and (C==Ctemp) and (R==Rtemp) and (Vs==Vstemp)
if check :
    t0 = t[-1]
    t = np.linspace(t0,t0+increment,1000)
elif (t_ != 0) :
    t0 = 0
    t = np.linspace(t0,t0+increment,1000)
    
if swi == 2:
    [I,t] =calc_series(L,C,R,V_0,dV_dt,Vs,t)
    print(t)
    V = integrate(I/C,t); 

elif (swi == 4) :
    print(t)
    [V,I,t] =calc_parallel(L,C,R,V_0,dV_dt,Vs,t)
else :
    V = np.zeros(len(t));I = V; 
xs.append(t);ys.append(I);
if len(xs) > 2000 :
    xs = xs[-2000:];ys = ys[-2000:]
    

C = Ctemp;L = Ltemp; R=Rtemp;Vs=Vstemp;t_= 1;



ys_r = np.real(ys)+np.imag(ys)
xs = xs[0];ys = ys[0];

col1, col2 = st.columns(2)
with col1:
    st.header("Current")
    fig, ax = plt.subplots()
    ax.plot(xs,ys)
    st.pyplot(fig)
with col2:
    st.header("Voltage")
    fig, ax = plt.subplots()
    ax.plot(xs,V)
    st.pyplot(fig)
