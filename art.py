from PIL import Image
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

folder = r'C:\Users\hp\Desktop\Our Arts'
size = (64, 64)

image_vector = []
image_names = []

for filename in os.listdir(folder):
    if filename.endswith('.png'):
        path = os.path.join(folder, filename)
        img = Image.open(path).convert('L').resize(size)
        img_vector = np.array(img).flatten()

    image_vector.append(img_vector)
    image_names.append(filename)

image_vector = np.array(image_vector)

scaler = StandardScaler()
scaled = scaler.fit_transform(image_vector)

pca = PCA(n_components=3)
pcadata = pca.fit_transform(scaled)

model = KMeans(n_clusters=2, random_state=42)
model.fit(pcadata)

print(model.labels_)
