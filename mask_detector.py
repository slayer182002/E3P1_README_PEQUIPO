import os
import cv2
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar imágenes
def load_data(directory, label):
    data = []
    labels = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        img = cv2.imread(path)
        if img is None:
            continue
        img = cv2.resize(img, (100, 100))
        data.append(img)
        labels.append(label)
    return data, labels

# Cargar datos con y sin cubrebocas
with_mask, labels_with_mask = load_data("dataset/with_mask", 0)
without_mask, labels_without_mask = load_data("dataset/without_mask", 1)

# Unir los datos
data = with_mask + without_mask
labels = labels_with_mask + labels_without_mask

# Convertir los datos a un arreglo de numpy
data = np.array(data)
labels = np.array(labels)

# Normalizar los datos
data = data / 255.0

# Aplanar las imágenes para ser usadas con un clasificador
data = data.reshape((data.shape[0], -1))  # Aplanar cada imagen

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.60)

# Crear un clasificador SVM
clf = svm.SVC(kernel='linear', C=1)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones
y_pred = clf.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión: {accuracy * 100:.2f}%")

# Guardar el modelo entrenado
import joblib
joblib.dump(clf, 'mask_detector_svm.pkl')
