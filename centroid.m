function c=centroid(r,threshold,low,high)

# only select the x and y values in the window 
ind=find(r(:,1)>=low & r(:,1) < high);
x=r(ind,1);
y=r(ind,2);

# apply threshold to y
yth=zeros(length(y),1);

for ii=1:length(y)
  if y(ii) < threshold
    yth(ii)=0;
  else
    yth(ii)=y(ii);
  end
end

# plot the thresholded part of the spectrum
figure(2);
clf;
plot(x,yth);

# calculate the centroid
c=0;
for ii=1:length(y)
  c+=x(ii)*yth(ii);
end

c=c/sum(yth);





  


