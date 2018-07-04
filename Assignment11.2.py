'''In this assignment students have to compress racoon grey scale image into 5 clusters. In
the end, visualize both raw and compressed image and look for quality difference.
The raw image is available in spicy.misc package with the name face.

Hint:

import numpy as np
from sklearn import cluster, datasets
from scipy import misc

NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source​ ​code​ ​used​ ​and​'''

import numpy as np
from sklearn import cluster, datasets
from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray=True)
plt.gray()
plt.imshow(face)
plt.show()

rows = face.shape[0]
cols = face.shape[1]
kmeans = cluster.KMeans(n_clusters = 5,random_state=0)
kmeans.fit(face)

clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8) 
labels = np.asarray(kmeans.labels_,dtype=np.uint8 )  
labels = labels.reshape(rows,cols); 

np.save('codebook_tiger.npy',clusters.imsave('compressed_tiger.png',labels))