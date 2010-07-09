from pylab import *
import scipy.optimize

ion()

def localpeak(pos,x,y,delta):
    localx=take(x,find((x>(pos[0]-delta))&(x<(pos[0]+delta))))
    localy=take(y,find((x>(pos[0]-delta))&(x<(pos[0]+delta))))
    
    localmax=localy.max()
    localmaxpos=take(localx,find(localy==localy.max()))[0]

    return (localmaxpos,localmax)


def pickpeak(x,y):
    ii=axis()
    # XXX this is a bit dodgy
    delta=(ii[1]-ii[0])/200.0
    print('click on peak!') 
    pos=ginput(1)
    pos=pos[0]
    (localmaxpos,localmax)=localpeak(pos,x,y,delta)

    tmp=axis()
    plot(localmaxpos,localmax,'go')
    axis(tmp)

    return (localmaxpos,localmax)

    
def findallpeaks(x,y,startx,meandist,delta,threshold,minval,maxval):
    # threshold the data
    y[find(y<threshold)]=0

    # start from startpeak, go to the right until maxval and mark
    # peaks, then do the same to the left
    means=[meandist]
    p=startx+meandist
    pold=startx
    while p<maxval:
        (localmaxpos,localmax)=localpeak((p,0),x,y,delta)
        if localmax>0:
            tmp=axis()
            plot(localmaxpos,localmax,'go')
            axis(tmp)
            means.append(abs(localmaxpos-pold))
        pold=p
        p=p+(sum(means)/len(means))

    p=startx-meandist
    pold=startx
    while p>minval:
        (localmaxpos,localmax)=localpeak((p,0),x,y,delta)
        if localmax>0:
            tmp=axis()
            plot(localmaxpos,localmax,'go')
            axis(tmp)
            means.append(abs(localmaxpos-pold))
        pold=p
        p=p-(sum(means)/len(means))


    print(sum(means)/len(means))

    # for p in arange(startx,maxval,meandist):
    #     (localmaxpos,localmax)=localpeak((p,0),x,y,delta)
    #     tmp=axis()
    #     plot(localmaxpos,localmax,'go')
    #     axis(tmp)
    

d=loadtxt('HDX1.txt')
xx=d[:,0]
yy=d[:,1]

figure(1)
clf()
hold(True)
plot(xx,yy)
xlim(1490,1497)
ylim(0,8e7)
draw()
show()

pos=ginput(1)
thres=pos[0][1]
hl1=axhline(y=thres,color='r')
draw()
#thres=121875000

pos=ginput(1)
low=pos[0][0]
hl2=axvline(x=low,color='g')
draw()
#low=1213.3441

pos=ginput(1)
high=pos[0][0]
hl3=axvline(x=high,color='g')
draw()
#high=1216.8461

x=take(xx,find((xx>low)&(xx<high)))
y=take(yy,find((xx>low)&(xx<high)))

yth=zeros(len(y))

for ii in range(0,len(y)):
    if y[ii]<thres:
        yth[ii]=0
    else:
        yth[ii]=y[ii]

tmp=axis()
axvspan(low,high,alpha=0.1,color='k')
axis(tmp)

xlim(low,high)
# find three peaks: click and find location
(x1,y1)=pickpeak(x,y)
(x2,y2)=pickpeak(x,y)
meandist=(max(x1,x2)-min(x1,x2))
print(meandist)

findallpeaks(x,y,x1,meandist,meandist*0.01,thres,low,high)


# figure(2)
# clf()
# yfft=fft(y)
# plot(1.0/x,abs(yfft))
# #xlim(0,200)

# # calculate sampling interval
# dx=0
# for ii in range(0,size(x)-1):
#     dx=dx+(x[ii+1]-x[ii])

# dx=dx/float(size(x)-1)







