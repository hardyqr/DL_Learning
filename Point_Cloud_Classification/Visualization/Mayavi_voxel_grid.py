'''
mport numpy as np
from mayavi import mlab


data = (100, 100, 100)
data = np.zeros(data)
data[0:50, 50:70, 0:50] = 1
data[0:50, 0:20, 0:50] = 1

src = mlab.pipeline.scalar_field(data)
outer = mlab.pipeline.iso_surface(src)

mlab.show()


'''
import mayavi.mlab
import numpy

data = (100, 100, 100)
data = numpy.zeros(data)

data[0:50, 50:70, 0:50] = 1
data[0:50, 0:20, 0:50] = 1

xx, yy, zz = numpy.where(data == 1)

mayavi.mlab.points3d(xx, yy, zz,
                     mode="cube",
                     color=(0, 1, 0),
                     scale_factor=1)

mayavi.mlab.show()
