import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense

data = pd.read_csv('train_data.csv')

train_data = np.array(data[['area', 'rooms', 'floor']])
train_labels = np.array(data['price'])

model = tf.keras.Sequential()
model.add(Dense(units=64, activation='relu', input_shape=(3,)))
model.add(Dense(units=1, activation='linear'))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(train_data, train_labels, epochs=10, batch_size=32)
