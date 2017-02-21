import pandas as pd
import numpy as np
import scipy.io
import random, math

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def Plot2D(T, title, x, y, num_to_plot=40):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  x_size = (max(T[:,x]) - min(T[:,x])) * 0.08
  y_size = (max(T[:,y]) - min(T[:,y])) * 0.08
  for i in range(num_to_plot):
    img_num = int(random.random() * num_images)
    x0, y0 = T[img_num,x]-x_size/2., T[img_num,y]-y_size/2.
    x1, y1 = T[img_num,x]+x_size/2., T[img_num,y]+y_size/2.
    img = df.iloc[img_num,:].reshape(num_pixels, num_pixels)
    ax.imshow(img, aspect='auto', cmap=plt.cm.gray, interpolation='nearest', zorder=100000, extent=(x0, x1, y0, y1))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.',alpha=0.7)



# A .MAT file is a .MATLAB file. The faces dataset could have came
# in through .png images, but we'll show you how to do that in
# anither lab. For now, you'll see how to import .mats:
mat = scipy.io.loadmat('Datasets/face_data.mat')
df = pd.DataFrame(mat['images']).T
num_images, num_pixels = df.shape
num_pixels = int(math.sqrt(num_pixels))

# Rotate the pictures, so we don't have to crane our necks:
for i in range(num_images):
  df.loc[i,:] = df.loc[i,:].values.reshape(num_pixels, num_pixels).T.reshape(-1)


#
# TODO: Implement PCA here. Reduce the dataframe df down
# to THREE components. Once you've done that, call Plot2D.
#
# The format is: Plot2D(T, title, x, y, num_to_plot=40):
# T is your transformed data, NDArray.
# title is your chart title
# x is the principal component you want displayed on the x-axis, Can be 0 or 1
# y is the principal component you want displayed on the y-axis, Can be 1 or 2
#
# .. your code here ..

from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(df)
 
T=pca.transform(df)
#print(T)

plt.figure()

Plot2D(T, title='chart2 title', x=0, y=1, num_to_plot=40)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to THREE components. Once you've done that, call Plot2D using
# the first two components.
#
# .. your code here ..
from sklearn import manifold
#from manifold import manifold.isomap

isp=manifold.Isomap(n_neighbors=8,n_components=3)
isp.fit(df)
T1=isp.transform(df)
#print(T1)

Plot2D(T1, title='chart2 title1', x=0, y=1, num_to_plot=40)



#
# TODO: If you're up for a challenge, draw your dataframes in 3D
# Even if you're not, just do it anyway.
#
# .. your code here ..
plt.style.use('ggplot')

fig=plt.figure()
plt.suptitle('0 and 1 and 2')
ax=fig.add_subplot(111, projection='3d')
ax.set_xlabel('0')
ax.set_ylabel('1')
ax.set_zlabel('2')
ax.set_title('PCA')
ax.scatter(T[:,0],T[:,1],T[:,2],c='r', marker='o')

fig=plt.figure()
plt.suptitle('0 and 1 and 2')
ax=fig.add_subplot(111, projection='3d')
ax.set_xlabel('0')
ax.set_ylabel('1')
ax.set_zlabel('2')
ax.set_title('ISOMAP')
ax.scatter(T1[:,0],T1[:,1],T1[:,2],c='b', marker='^')


plt.show()
