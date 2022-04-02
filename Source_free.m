V_0 = 23; % voltage at which capacitor is charged
I_0 = 0.023; % current flowing through inductor

L = 5;
C= 2e-3;
R = 10;
V_0 = 0;
dvdt = 0;
Vs = 20; % source voltage
t = 0:0.01:10;


alpha = R/(2*L);
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
   disp("Overdamped")
   I =  a1*exp(s1*t) + a2*exp(s2*t);
elseif (alpha == omega_o) 
    % crictically damped
    disp("Critically damped")
   I = (a1 + a2*t)*exp(-alpha*t);
else 
    % underdamped
   disp("Underdamped")
   I = (a1.*cos(omega_d.*t)+ a2.*sin(omega_d.*t) ).*exp(-alpha.*t);
end
plot(t,real(I)+imag(I))

