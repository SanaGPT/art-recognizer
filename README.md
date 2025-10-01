# art-recognizer
a program with unsupervised learning utilized in to seperate my friend's & my art styles 

Features : 
Image Preprocessing: Converts images to grayscale and resizes for consistency

Dimensionality Reduction: Uses PCA to reduce image data to 3 principal components

Automated Clustering: K-means clustering to group similar artworks

Batch Processing: Handles entire folders of PNG images automatically

Requirements : 
python
PIL (Pillow)
os
numpy
scikit-learn

Usage : 
Set the folder path to your art directory

Run the script to process all images

Get cluster labels showing how images are grouped by visual similarity
