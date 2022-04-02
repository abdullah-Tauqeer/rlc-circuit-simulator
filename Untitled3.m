arr = real(I) + imag(I);
time = t;
ans_(1) = arr(1);
dt = time(2)-time(1);
for k = 1: length(arr)-1
ans_(k+1) = arr(k+1)+ ans_(k);

end
