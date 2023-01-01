from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.utils import get_file
import os
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

imagegen = ImageDataGenerator(rescale=1./255., rotation_range=30, horizontal_flip=True, validation_split=0.1)

path_to_zip = get_file('weatherData.zip', origin="https://static.junilearning.com/ai_level_2/weatherData.zip", extract=True)
PATH = os.path.join(os.path.dirname(path_to_zip), 'weatherData')
train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')
test_dir = os.path.join(PATH, 'test')

train_generator = imagegen.flow_from_directory(train_dir, class_mode="categorical", shuffle=True, batch_size=128, target_size=(224, 224))
validation_generator = imagegen.flow_from_directory(validation_dir, class_mode="categorical", shuffle=True, batch_size=128, target_size=(224, 224))
test_generator = imagegen.flow_from_directory(test_dir, class_mode="categorical", shuffle=False, batch_size=128, target_size=(224, 224))


model = Sequential()

# 3 convolutional layers
model.add(Conv2D(32, (3, 3), input_shape=(224, 224, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("leaky_relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

# 2 hidden layers
model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))

model.add(Dense(128))
model.add(Activation("leaky_relu"))

# The output layer with 4 neurons (1 per class)
model.add(Dense(4))
model.add(Activation("softmax"))

# compile model
model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
# fit on data for 10 epochs
history = model.fit_generator(train_generator, epochs=30, validation_data=validation_generator)

def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')

  # Examine more closely
  #plt.ylim([1000,4000])

  plt.xlabel('Epoch')
  plt.ylabel('Error')
  plt.legend()
  plt.grid(True)


plot_loss(history)

accuracy = model.evaluate(test_generator)[1]
print(accuracy)


def plot_acc(history, ax=None, xlabel='Epoch #'):
  if hasattr(history, 'history_'):
    history = history.history_
  else:
    history = history.history
  history.update({'epoch': list(range(len(history['val_accuracy'])))})
  history = pd.DataFrame.from_dict(history)

  best_epoch = history.sort_values(by='val_accuracy', ascending=False).iloc[0]['epoch']

  if not ax:
    f, ax = plt.subplots(1, 1)
  sns.lineplot(x='epoch', y='val_accuracy', data=history, label='Validation', ax=ax)
  sns.lineplot(x='epoch', y='accuracy', data=history, label='Training', ax=ax)
  ax.axhline(0.5, linestyle='--', color='red', label='Chance')
  ax.axvline(x=best_epoch, linestyle='--', color='green', label='Best Epoch')
  ax.legend(loc=7)
  ax.set_ylim([0.4, 1])

  ax.set_xlabel(xlabel)
  ax.set_ylabel('Accuracy (Fraction)')

  plt.show()


plot_acc(history)