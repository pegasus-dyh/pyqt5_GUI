"""
senquential结构 最简化版
"""

import tensorflow as tf
import os
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPool2D, Dropout, Flatten, Dense
from tensorflow.keras import Model

np.set_printoptions(threshold=np.inf)

cifar10 = tf.keras.datasets.cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


inputs = tf.keras.Input(shape=(32,32,3))
conv1=Conv2D(filters=6,kernel_size=(5, 5), padding='same',activation='relu')(inputs)
maxp1=MaxPool2D(pool_size=(2, 2), strides=2, padding='same')(conv1)
conv2=Conv2D(filters=16, kernel_size=(5, 5),activation='sigmoid')(maxp1)
maxp2=MaxPool2D(pool_size=(2, 2), strides=2)(conv2)


flatten=Flatten()(maxp2)
d1=Dense(120, activation='sigmoid')(flatten)
d2=Dense(84, activation='sigmoid')(d1)
outputs=Dense(10, activation='softmax')(d2)
model=tf.keras.Model(inputs=inputs, outputs=outputs)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])
history=model.fit(x_train,y_train, epochs=5, batch_size=32, validation_data=(x_test,y_test),validation_freq=1)
model.summary()



###############################################    show   ###############################################

# 显示训练集和验证集的acc和loss曲线
acc = history.history['sparse_categorical_accuracy']
val_acc = history.history['val_sparse_categorical_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.subplot(1, 2, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()

