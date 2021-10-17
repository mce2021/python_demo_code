import bitshuffle.h5
import dask.array as da
import numpy as np
import napari
import h5py
import sys

f = h5py.File(sys.argv[1])
d = f["/entry/data/data"]
s = d.shape

i = d[0]

a = da.from_array(d, chunks=(1, s[1], s[2]))

viewer = napari.view_image(a, title="DIALS Image Viewer", contrast_limits=[0, 10])

napari.run()
