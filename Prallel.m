clear all
L = 1;
C= 10e-3;
R = 5;
V_0 = 5;
dvdt = 0;
Vs = 5; % source voltage
t = 0:0.01:10;


alpha = 1/(2*R*C);
omega_o = 1/sqrt(C*L);
omega_d = sqrt(omega_o^2-alpha^2);

s1 = -alpha+sqrt(alpha^2-omega_o^2);
s2 = -alpha-sqrt(alpha^2-omega_o^2);
syms A1 A2
eqn_1 = A1+A2 == 0;
eqn_2 = s1*A1+s2*A2 == Vs;
[a1,a2]=vpasolve(eqn_1,eqn_2);

if (alpha > omega_o)
    % overdamped 
   V = Vs + a1*exp(s1*t) + a2*exp(s2*t);
elseif (alpha == omega_o) 
    % crictically damped
    V = Vs + (a1 + a2*t)*exp(-alpha*t);
else 
    % underdamped
    V =  Vs+(a1.*cos(omega_d.*t)+ a2.*sin(omega_d.*t) ).*exp(-alpha.*t);
end
    
plot(t,real(V)+imag(V))