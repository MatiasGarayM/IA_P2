from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Convertir las etiquetas a codificación one-hot
encoder = OneHotEncoder(sparse=False)
y_one_hot = encoder.fit_transform(y.reshape(-1, 1))

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal
model = Sequential()
model.add(Dense(10, input_dim=X.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo con retropropagación del error
history = model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1, validation_data=(X_test, y_test))

# Hacer predicciones sobre el conjunto de prueba
predicciones = model.predict(X_test)

# Convertir las predicciones de vuelta a etiquetas de clase
clases_predichas = np.argmax(predicciones, axis=1)

# Mostrar algunas predicciones junto con las etiquetas verdaderas
print("Predicciones:")
for i in range(10):
    print("Predicción:", clases_predichas[i], "| Etiqueta verdadera:", np.argmax(y_test[i]))

# Calcular la precisión del modelo en el conjunto de prueba
precision = model.evaluate(X_test, y_test, verbose=0)[1]
print("\nPrecisión del modelo en el conjunto de prueba:", precision)