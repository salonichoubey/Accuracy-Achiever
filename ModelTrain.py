# keras imports for the dataset and building our neural network
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
from keras.utils import np_utils
from keras.callbacks import Callback
# to calculate accuracy
from sklearn.metrics import accuracy_score
import numpy as np

# class for writing the accuracy in a file
class myCallback(Callback):
      def on_epoch_end(self, epoch, logs={}):

            file='/root/output.txt'
            var=logs.get('accuracy')
            with open(file, 'w') as filetowrite:
                filetowrite.write(np.array2string(var))




callbacks = myCallback()
# loading the dataset
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# building the input vector from the 28x28 pixels
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# normalizing the data to help with the training
X_train /= 255
X_test /= 255

# one-hot encoding using keras' numpy-related utilities
n_classes = 10
print("Shape before one-hot encoding: ", y_train.shape)
Y_train = np_utils.to_categorical(y_train, n_classes)
Y_test = np_utils.to_categorical(y_test, n_classes)
print("Shape after one-hot encoding: ", Y_train.shape)

# building a linear stack of layers with the sequential model
model = Sequential()
model.add(Flatten())
model.add(Dense(256, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))



#hyperparameters
epoch=5

# compiling the sequential model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
# training the model for 5 epochs
history = model.fit(
            X_train,Y_train, epochs=epoch,callbacks=[callbacks]
    )
