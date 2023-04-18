import numpy as np
from matplotlib.colors import ListedColormap

def turbo_w(N=2560):
    """
    modified turbo colormap with white background
    cmap = turbo_w()
    """
    cmap = np.load('white_turbo.npy')
    return ListedColormap(cmap,N=N)


def plot2d(ax, x, y, Int, colormap='jet', imshow=False, rasterized=True):
    x = np.array(x)
    y = np.array(y)
    if len(x) != np.shape(Int)[0]:
        print("wrong dimension for x, should be the same as the 1st dimension of Int\n")
    elif len(y) != np.shape(Int)[1]:
        print("wrong dimension for y, should be the same as the 2nd dimension of Int\n")
    else:
        if imshow:
            xstep = x[1] - x[0]
            ystep = y[1] - y[0]
            im = ax.imshow(np.fliplr(np.rot90(Int, k=-1)),
                           extent=[x[0]-xstep/2, x[-1]+xstep/2, y[0]-ystep/2, y[-1]+ystep/2],
                           cmap=colormap, interpolation = "none",origin = "lower", aspect = 'auto',
                          )
        else:
            x_mesh,y_mesh = np.meshgrid(x,y)
            im = ax.pcolormesh(x_mesh,y_mesh,np.fliplr(np.rot90(Int, k=-1)),
                               shading='nearest',cmap=colormap, rasterized=rasterized,
                              )
        return im
