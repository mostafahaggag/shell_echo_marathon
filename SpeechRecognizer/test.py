# import librosa
# from pydub import AudioSegment
# from pydub.playback import play
# import numpy as np
# # y, sr = librosa.load('test.wav') # y is a numpy array of the wav file, sr = sample rate
# # y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=0)# shifted by 4 half steps
# #
# from SpeechRecognizer.audio_player import AudioFile
# # # AudioSegment.
# # [-25,-20,-15,-10,-5,5,10,15]
# #======================================
# from pydub import AudioSegment
#
# song = AudioSegment.from_wav("test.wav")
# # but let's make him *very* quiet
# song = song + 15
#
# # save the output
# play(song)
# song.export("test3.wav", "wav")
##=========================================================
#
# # #TODO
# from pydub import AudioSegment
# from pydub.playback import play
#
# sound = AudioSegment.from_file('test.wav', format="wav")
#
# # shift the pitch up by half an octave (speed will increase proportionally)
# octaves = 0.9
#
# new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
#
# # keep the same samples but tell the computer they ought to be played at the
# # new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
# hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
#
# # now we just convert it to a common sample rate (44.1k - standard audio CD) to
# # make sure it works in regular audio players. Other than potentially losing audio quality (if
# # you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
# hipitch_sound = hipitch_sound.set_frame_rate(44100)
#
# #Play pitch changed sound
# play(hipitch_sound)
#
# #export / save pitch changed sound
# hipitch_sound.export("test2.wav", format="wav")
#
# ##=====================================================================
from pydub import AudioSegment
from pydub.playback import play
import pickle
# sound = AudioSegment.from_file('D:\\echoshell\\rnn\\Virtual_Assistant-master\\audio\\Open the lights\\9.wav', format="wav")
# play(sound)
# from SpeechRecognizer.editing_voice import changing_wav_files
# s=changing_wav_files()
# s.play_with_pitch()
# import pickle
# import numpy as np
# from pydub.playback import play
# from sklearn.preprocessing import LabelEncoder
# from tensorflow.python.keras import utils
import librosa
import numpy as np
# from pydub import AudioSegment
# from SpeechRecognizer.recorder import SoundRecorder
pickle_in = open("W.pickle", "rb")
x_train = pickle.load(pickle_in)
x_train = np.array(x_train)
print(x_train.shape)
# pickle_in = open("Y.pickle", "rb")
# y_train = pickle.load(pickle_in)
# y_train = np.array(y_train)
# print(y_train.shape)
# lb = LabelEncoder()
# y_train= utils.to_categorical(lb.fit_transform(y_train))
# print(y_train.shape)#(56,2)3andy 2 categories
# # s=SoundRecorder()
# # s.record_file("test.wav")
# audio, sr = librosa.load("D:\\echoshell\\rnn\\Virtual_Assistant-master\\custom_audio\\Turn the lights off\\1006.wav")
# mfcc = librosa.feature.mfcc(y=audio, sr=sr)#by default it return 20 mfccs x t
# mfcc2=np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40).T, axis=0)
# print(mfcc.shape)
# print(mfcc2.shape)
## print(get_features("test.wav",type='RNN').shape)
# test = Recognizer()
# test.start("DNN")
# sr,audio =read("test.wav")
# mfcc = librosa.feature.melspectrogram(y=audio, sr=sr)
#sr dh sampling rate of of y
#y=signal audio time series
# plt.imshow(mfcc,cmap='Greys')
# plt.show()
# mfcc2 = librosa.feature.mfcc(y=audio, sr=sr)
# print(mfcc2.shape)#(20,173)
# print(mfcc.shape)#(128,173)
# print(len(audio))#88064
# pickle_in = open("X.pickle", "rb")
# x_train = pickle.load(pickle_in)
# x_train = np.array(x_train)#110
# print(x_train.size)#191400
# print(np.shape(x_train))#(110,20,87)
# x_train = x_train.reshape(x_train.shape[0], 130, 20)
# print(np.shape(x_train))#
        #x.shape beydelek length of the zeor dimension
        #130
        #20
        #(sample rate/chunck)*seconds
# self.x_train = tf.keras.utils.normalize(self.x_train)