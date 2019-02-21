import librosa
import numpy as np
import os
import pickle
import random
import tensorflow as tf
from sklearn.model_selection import train_test_split
cwd = os.path.abspath(os.path.join("", os.pardir))
Dir = cwd+"/audio"
pitch_directory=cwd+"/custom_audio"
magitude_directory=cwd+"/custom_magnitude"
catdir = cwd+"/Categories.txt"
f = open(catdir, "r")
CATEGORIES = f.read().replace('\n', ',').split(',')
f.close()

class SoundExtraction:
    def __init__(self, categories=CATEGORIES, directory=Dir,pitch_directory=pitch_directory,magitude_directory=magitude_directory):
        self.training_data = []
        self.categories = categories
        self.dir = directory
        self.pitch_directory=pitch_directory
        self.magitude_directory=magitude_directory

    def create_training_data(self,type='DNN',pitch=False, magnitude =False):
        for category in self.categories:
            path = os.path.join(self.dir, category)
            path2 = os.path.join(self.pitch_directory, category)
            path3 = os.path.join(self.magitude_directory, category)
            class_num = self.categories.index(category)
            #badeey li kol category a kind of an index mo3yan fa maslan close the light 3anadah category 4
            for file in os.listdir(path):
                file = self.dir+"/"+category+"/"+file
                try:
                    feature_vector = get_features(file, type)
                    self.training_data.append([feature_vector, class_num])
                    #ba7oot gowa ab ig list a small list made of eature vector and class number
                except Exception as e:
                    pass
            if pitch is True :
                for file in os.listdir(path2):
                    file = self.pitch_directory+"/"+category+"/"+file
                    try:
                        feature_vector = get_features(file, type)
                        self.training_data.append([feature_vector, class_num])
                        #ba7oot gowa ab ig list a small list made of eature vector and class number
                    except Exception as e:
                        pass
            if magnitude is True:
                    for file in os.listdir(path3):
                        file = self.magitude_directory+"/"+category+"/"+file
                        try:
                            feature_vector = get_features(file, type)
                            self.training_data.append([feature_vector, class_num])
                            #ba7oot gowa ab ig list a small list made of eature vector and class number
                        except Exception as e:
                            pass
        random.shuffle(self.training_data)
        x = []
        y = []

        for features, label in self.training_data:
            x.append(features)
            y.append(label)

        x_training,x_test,y_training,y_test=train_test_split(x,y,test_size=0.2,shuffle=True)
        pickle_out = open("X.pickle", "wb")
        pickle.dump(x_training, pickle_out)
        pickle_out.close()
        # print(len(x_test[2]))
        pickle_out = open("Y.pickle", "wb")
        pickle.dump(y_training, pickle_out)
        pickle_out.close()

        pickle_out = open("Z.pickle", "wb")
        pickle.dump(x_test, pickle_out)
        pickle_out.close()

        pickle_out = open("W.pickle", "wb")
        pickle.dump(y_test, pickle_out)
        pickle_out.close()

        print("Done Extracting data")
def get_features(file, type='DNN'):
    audio, sr = librosa.load(file,mono=True)
    # we extract mfcc feature from data
    if type is 'DNN':
        mfcc = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40).T, axis=0)
    elif type is 'RNN':
        mfcc = librosa.feature.mfcc(y=audio, sr=sr)
    return mfcc
#numpy.pad(array, pad_width, mode, **kwargs)
#array  input arra y
#pad_width number of values padded to the edges of each axis

#mode usually constant value padding

#dh mainly used to get features acccording lw rnn aw dnnn
#these are two different onditions
#ba load el file using librosa
