import imp

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_imgs, train_labels), (test_imgs, test_labels) = fashion_mnist.load_data()

# plt.imshow(train_imgs[0], cmap='gray', vmin=0, vmax=255)
# plt.show()

print('Model 1')
model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(units=128, activation=tf.nn.relu),
    keras.layers.Dense(units=10, activation=tf.nn.softmax)
])

print("model 2")

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy')

print("model 3")
model.fit(train_imgs, train_labels, epochs=5)

print("model 4")
test_loss = model.evaluate(test_imgs, test_labels)

print("Training done")

numberOfObj = 1

plt.imshow(test_imgs[numberOfObj], cmap='gray', vmin=0, vmax=255)
plt.show()

print(test_labels[numberOfObj])

prediction = model.predict(test_imgs)

print(prediction[numberOfObj])

print(list(prediction[numberOfObj]).index(max(prediction[numberOfObj])))