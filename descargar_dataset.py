import kagglehub

# Descargar la última versión del dataset
path = kagglehub.dataset_download("charitarth/maskedfacenet")

print("Path to dataset files:", path)
