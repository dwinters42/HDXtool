function res=readspectrum(datafile)

# load the datafile
res=load(datafile);

figure(1);
clf;
plot(res(:,1),res(:,2));



