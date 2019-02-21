from sound_extractor import SoundExtraction
from neural_network import RNN,DNN,plot
from recognizer import Recognizer
from editing_voice import changing_wav_files
y=changing_wav_files()
# # # #you can change min and max and step change in the pitch and the magnitude from the function it self, no need to open the class
# # # #use the parameters of the object like
# # y.play_with_pitch(min_pitch=0.2,max_pitch=1,step_pitch=0.2)
# y.change_in_magnitude(min_mag=2,max_mag=8,step_mag=2)
# # # # # #the min and max and step are used to tell the function how much to change in the signal
# # # # # #the default parameters are set inside of the class so if you want you may not enter anything
# S = SoundExtraction()
# S.create_training_data(type='RNN',pitch=False, magnitude =True)
# # #it is a must to set parameter pitch=true, magnitude =true to use the data which has a different magnitude or frequency
# T = RNN()
# history = T.train()
# plot(history)
# the_dnn_model="Model.h5"
the_rnn_model="ModelRNN.h5"
test = Recognizer(model=the_rnn_model)
test.start("RNN")
# test.testaccuracy(type="RNN")
# import tensorflow as tf
# import pickle
# from tensorflow.python.keras.models import load_model

# import numpy as np
# from tensorflow.python.keras import utils
# pickle_in = open("Z.pickle", "rb")
# x_train = pickle.load(pickle_in)
# x_train = np.array(x_train) #mafrood d0h aed number of samples fi kol categories el 3andy
# x_train = x_train.reshape(x_train.shape[0], 130, 20)
# x_train = tf.keras.utils.normalize(x_train)
# pickle_in = open("W.pickle", "rb")
# y_train = pickle.load(pickle_in)
# y_train = np.array(y_train)#mafrood dh aed number of samples madroob fi 40. the mfcc beytala3 40
# y_train = utils.to_categorical(y_train)#lb.fit_transform(y_train))
# model= load_model(the_rnn_model)
# loss, acc = model.evaluate(x_train, y_train, verbose=1)
# print('\nTesting loss: {}, acc: {}\n'.format(loss, acc))