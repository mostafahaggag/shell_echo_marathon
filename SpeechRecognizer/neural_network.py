import tensorflow as tf
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.python.keras import utils
import matplotlib.pyplot as plt
import os
from tensorflow.python.keras.callbacks import Callback
import datetime
import sys
from shutil import copyfile

cwd = os.path.abspath(os.path.join("", os.pardir))
catdir = cwd+"/Categories.txt"
file = open(catdir, "r")
CATEGORIES = file.read().replace('\n', ',').split(',')
file.close()
import shutil


class DNN:
    def __init__(self, epochs=12, batch_size=16, validation_split=0.2, categories=CATEGORIES):

        pickle_in = open("X.pickle", "rb")
        #
        x_train = pickle.load(pickle_in)
        self.x_train = np.array(x_train) #mafrood dh aed number of samples fi kol categories el 3andy
        #self.x_train = tf.keras.utils.normalize(self.x_train)
        pickle_in = open("Y.pickle", "rb")
        y_train = pickle.load(pickle_in)
        y_train = np.array(y_train)#mafrood dh aed number of samples madroob fi 40. the mfcc beytala3 40
        lb = LabelEncoder()
        #LabelEncoder encode labels with a value between 0 and n_classes-1
        # where n is the number of distinct labels.
        # If a label repeats it assigns the same value to as assigned earlier.
        #The problem here is since there are different numbers in the same column,
        #  the model will misunderstand the data to be in some kind of order, 0 < 1 <2.
        #hotkey
        #beydeek ones w zeros w blaah blaah blahhh blaah
        self.y_train = utils.to_categorical(lb.fit_transform(y_train))
        #Converts a class vector (integers) to binary class matrix.
        #	Fit label encoder and return encoded labels
        #mafrood haydeek(numberof samples,number of categious)
        self.epochs = epochs
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.categories = categories

    def train(self):

        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(units=256, activation='tanh', input_dim=self.x_train.shape[1]))#number of samples, 40 el tala3a mn mfcc,
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(units=256, activation='tanh'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(units=256, activation='tanh'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(units=len(self.categories), activation='softmax'))
        model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adamax')
        history = model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epochs,
                            validation_split=self.validation_split)
        now=datetime.datetime.now()
        newdirectory=now.strftime("%Y_%m_%d-%H%M")
        newdirectory=newdirectory+"_DNN"
        os.mkdir(newdirectory)
        model.save(newdirectory+"/Model.h5")
        model.save("Model.h5")
        newtest=newdirectory+"/Categories.txt"
        shutil.copyfile(catdir, newtest)
        plot_saving(history,newdirectory)
        return history

#accuracy no3en sa
#traininging w validation
#hyperpapmaters el homa  epochs wi activation funciton batch size
#validation accuracy bey2sar validation split el betbaselha data lw 2alleet validaiton split small acurracy bet2al
class TestCallback(Callback):
    def __init__(self, test_data):
        self.test_data = test_data
        self.array=[]

    def on_epoch_end(self, epoch, logs={}):
        x, y = self.test_data
        loss, acc = self.model.evaluate(x, y, verbose=0)
        self.array.append([epoch, acc,loss])
        logs['testing_acc'] = acc
        logs['testing_loss'] = loss
        print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))
class RNN:
    def __init__(self, epochs=40, batch_size=16, validation_split=0.2, categories=CATEGORIES):

        pickle_in = open("X.pickle", "rb")
        x_train = pickle.load(pickle_in)
        self.x_train = np.array(x_train)#(54, 20, 130)(number of samples,20,130)
        self.x_train = self.x_train.reshape(self.x_train.shape[0], 130, 20)
        #x.shape beydelek length of the zeor dimension
        #130
        #20
        #(sample rate/chunck)*seconds
        self.x_train = tf.keras.utils.normalize(self.x_train)
        pickle_in = open("Y.pickle", "rb")
        y_train = pickle.load(pickle_in)
        y_train = np.array(y_train)
        #lb = LabelEncoder()
        self.y_train = utils.to_categorical(y_train)#lb.fit_transform(y_train))
        self.epochs = epochs ## feedforward plus back propagation
        self.batch_size = batch_size #number of training examples utilized in one iteration
        self.validation_split = validation_split
        self.categories = categories
        pickle_in = open("Z.pickle", "rb")
        x_test = pickle.load(pickle_in)
        self.x_test = np.array(x_test)
        self.x_test=self.x_test.reshape(self.x_test.shape[0],130,20)
        self.x_test=tf.keras.utils.normalize(self.x_test)
        pickle_in = open("W.pickle", "rb")
        y_test = pickle.load(pickle_in)
        y_test = np.array(y_test)
        self.y_test=utils.to_categorical(y_test)
        model = tf.keras.models.Sequential()
        self.model=model
    def train(self):
        #.add to add a new layer
        #The model needs to know what input shape it should expect.
        # For this reason, the first layer in a Sequential model
        # (and only the first, because following layers can do automatic shape inference)
        #  needs to receive information about its input shape
        #input_shape
        self.model.add(tf.keras.layers.LSTM(units=256, input_shape=self.x_train.shape[1:],return_sequences=True))
        #bad5aaal el 130
        # avoid over fitting
        #dropout consists in rando1mly setting a fraction rate of input units to 0 at each update
        #during training time preventing overfitting
        # self.model.add(tf.keras.layers.LSTM(units=256,return_sequences=True))
        self.model.add(tf.keras.layers.Dropout(0.2))
        self.model.add(tf.keras.layers.LSTM(units=256, return_sequences=True))
        self.model.add(tf.keras.layers.Dropout(0.2))
        self.model.add(tf.keras.layers.LSTM(units=256, return_sequences=True))
        self.model.add(tf.keras.layers.Dropout(0.2))
        # self.model.add(tf.keras.layers.LSTM(units=256,return_sequences=True))
        # self.model.add(tf.keras.layers.LSTM(units=256,return_sequences=True))
        self.model.add(tf.keras.layers.LSTM(units=256))
        self.model.add(tf.keras.layers.Dropout(0.2))
        # self.model.add(tf.keras.layers.Flatten())
        adam = tf.keras.optimizers.Adam(lr=0.001)
        self.model.add(tf.keras.layers.Dense(units=len(self.categories), activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=adam)
        # score, acc = self.model.evaluate(self.x_test, self.y_test,
        #                             batch_size=self.batch_size)
        # print('Test score:', score)
        # print('Test accuracy:', acc)
        #Configures the model for training.
        #metric 3ayz a evaluate eh during trainning and testing
        print(self.model.summary())
        history = self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epochs
                            , validation_split=self.validation_split
                            , verbose=1, callbacks = [TestCallback((self.x_test, self.y_test))])
        loss, acc = self.model.evaluate(self.x_test, self.y_test, verbose=0)
        print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))

      #  , callbacks = [TestCallback((self.x_test, self.y_test))]
        # loss, acc = self.model.evaluate(self.x_test, self.y_test, verbose=1)
        # self.model.evaluate(self.x_test, self.y_test, verbose=0)        #Trains the model for a given number of epochs (iterations on a dataset).
        #fit(x=None, y=None, batch_size=None, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0, steps_per_epoch=None, validation_steps=None)
        #x nump array of training data.
        #y numpy array of labels.
        #Number of samples per gradient update
        #epoch number of epoch to train the model
        #verbose verbose=1 will show you an animated progress bar like this:
        # Its History.history attribute is a record of training loss values
        # and metrics values at successive epochs,
        # as well as validation loss values and validation metrics values (if applicable).
        now=datetime.datetime.now()
        newdirectory=now.strftime("%Y_%m_%d-%H%M")
        newdirectory=newdirectory+"_RNN"
        os.mkdir(newdirectory)
        self.model.save(newdirectory+"/ModelRNN.h5")
        self.model.save("ModelRNN.h5")
        plot_saving(history,newdirectory)
        newtest=newdirectory+"/Categories.txt"
        shutil.copyfile(catdir, newtest)
        return history



def plot(history):
    # Plot training & validation accuracy values
    plt.clf()
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.plot(history.history['testing_acc'])

    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation','Testing'], loc='upper left')
    plt.show()
    plt.clf()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.plot(history.history['testing_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation','Testing'], loc='upper left')
    plt.show()
def plot_saving(history,folder):
    # Plot training & validation accuracy values
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.plot(history.history['testing_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation','Testing'], loc='upper left')
    plt.savefig(folder+'/accuracy.png')
    plt.clf()
    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.plot(history.history['testing_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation','Testing'], loc='upper left')
    plt.savefig(folder+'/loss.png')
