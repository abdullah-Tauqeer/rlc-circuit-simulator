import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import cmath
from sympy import symbols, Eq, solve
def calc_series(L,C,R,V_0,dV_dt,Vs,t) :
    alpha = R/(2*L);
    omega_o = 1/np.sqrt(C*L);
    omega_d = np.sqrt(omega_o**2-alpha**2);

    s1 = -alpha+cmath.sqrt(alpha**2-omega_o**2);
    s2 = -alpha-cmath.sqrt(alpha**2-omega_o**2);

    A1, A2 = symbols('A1 A2')
    eq1 = Eq(s1*A1+s2*A2-Vs - dV_dt,0)
    eq2 = Eq(A1+A2 +Vs- V_0 ,0)
    sol = solve((eq1, eq2),(A1, A2))
    a1= complex(sol[A1].as_real_imag()[0]+sol[A1].as_real_imag()[1]*1j )
    a2 =complex(sol[A2].as_real_imag()[0]+sol[A2].as_real_imag()[1]*1j )
    if (alpha > omega_o) :
        V = Vs + a1*np.exp(s1*t) + a2*np.exp(s2*t);
    elif (alpha == omega_o) :
        # crictically damped
        V = Vs + (a1 + a2*t)*np.exp(-alpha*t);
    else :
        # underdamped
        V =  Vs+np.multiply((a1*np.cos(np.multiply(omega_d,t))+ a2*np.sin(np.multiply(omega_d,t)) ),np.exp(np.multiply(-alpha,t)))

    I = np.diff(V)
    I=np.append(0,I)*C
    return I,t