import numpy as np
from PIL import Image

list_im = ['/home/pi/winecellar/img/todayTemp.png', '/home/pi/winecellar/img/todayHumid.png']
imgs    = [ Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]

imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( '/home/pi/winecellar/img/today.png' )
