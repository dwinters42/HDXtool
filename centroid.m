function c=centroid(r)

# select threshold, low and high value with mouse
figure(1);
[cx,cy,but]=ginput(3);

threshold=cy(1);
low=cx(2);
high=cx(3);

printf("threshold: %f, using data from %f to %f]\n",threshold,low,high)

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





  


