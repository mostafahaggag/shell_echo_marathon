from tensorflow.python.keras.models import load_model
import numpy as np
from SpeechRecognizer.recorder import SoundRecorder
from SpeechRecognizer.sound_extractor import get_features
import os
import pickle
import tensorflow as tf
from tensorflow.python.keras import utils
cwd = os.path.abspath(os.path.join("", os.pardir))
catdir = cwd+"\\Categories.txt"
file = open(catdir, "r")
CATEGORIES = file.read().replace('\n', ',').split(',')
file.close()
second=3

class Recognizer:
    def __init__(self, from_file=False, file_name="", model="Model.h5", time=second):
        self.model = load_model(model)
        self.file = "test.wav"
        self.categories = CATEGORIES
        pickle_in = open("Z.pickle", "rb")
        x_test = pickle.load(pickle_in)
        self.x_test = np.array(x_test)


        pickle_in = open("W.pickle", "rb")
        y_test = pickle.load(pickle_in)
        y_test = np.array(y_test)
        self.y_test=utils.to_categorical(y_test)
        if from_file:
            if file_name is "":
                print("You have not put a file path so you will record one now as a test.wav ")
                self.recorder = SoundRecorder(recording_period=time)
            else:
                self.file = file_name
        else:
            self.recorder = SoundRecorder(recording_period=time)
            #3lshan a record new recording


    def test_file(self,type="DNN"):
        test_x = np.array(get_features(self.file,type))
        if type is "DNN":
            test_x = test_x.reshape((1, len(test_x)))
        elif type is "RNN":
            test_x = test_x.reshape((1, test_x.shape[1],test_x.shape[0]))
        predicted = self.model.predict(test_x)
        predicted = predicted[0]
        r,predicted = predicted[np.argmax(predicted)]*100,self.categories.__getitem__(np.argmax(predicted))
        print("The Model predicted: ", predicted,"  with :",r," accuracy")

    def start(self,type="DNN"):
        self.recorder.record_file(self.file)
        test_x = np.array(get_features(self.file,type))
        if type is "DNN":
            test_x = test_x.reshape((1, len(test_x)))
        elif type is "RNN":
            test_x = test_x.reshape((1, test_x.shape[1],test_x.shape[0]))
        predicted = self.model.predict(test_x)
        #print(predicted)
        predicted = predicted[0]
        #print(predicted)
        r, predicted = predicted[np.argmax(predicted)] * 100, self.categories.__getitem__(np.argmax(predicted))
        #Returns the indices of the maximum values along an axis. dh arg max
        print("The Model predicted: ", predicted, "  with :", r, " accuracy")

    def start_now(self,type="DNN"):
        self.recorder.record_file_now(self.file)
        test_x = np.array(get_features(self.file,type))
        if type is "DNN":
            test_x = test_x.reshape((1, len(test_x)))
        elif type is "RNN":
            test_x = test_x.reshape((1, test_x.shape[1],test_x.shape[0]))
        predicted = self.model.predict(test_x)
        predicted = predicted[0]
        r, predicted = predicted[np.argmax(predicted)] * 100, self.categories.__getitem__(np.argmax(predicted))
        return r, predicted
    def testaccuracy(self,type):
            # print(self.x_test[2])
            if type is "DNN":
                self.x_test = self.x_test.reshape((self.x_test.shape[0], len(self.x_test)))
            elif type is "RNN":
                self.x_test = self.x_test.reshape(self.x_test.shape[0], 130, 20)
            predicted =self.model.predict(self.x_test)
            testing_accuracy=0
            for index in range(0,predicted.shape[0]):
                The_prediction=np.argmax(predicted[index])
                if The_prediction == np.argmax(self.y_test[index]):
                    testing_accuracy=testing_accuracy+1
            result=(testing_accuracy/predicted.shape[0])*100
            print(result)
            loss, acc = self.model.evaluate(self.x_test, self.y_test, verbose=1)
            print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))

            print(predicted.shape[0])













