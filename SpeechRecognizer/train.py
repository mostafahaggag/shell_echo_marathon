from SpeechRecognizer.sound_extractor import SoundExtraction
from SpeechRecognizer.neural_network import RNN,DNN,plot
from SpeechRecognizer.recognizer import Recognizer
from SpeechRecognizer.editing_voice import changing_wav_files
# y=changing_wav_files()
# # #you can change min and max and step change in the pitch and the magnitude from the function it self, no need to open the class
# # #use the parameters of the object like
# # #y.play_with_pitch(min_pitch=0.3,max_pitch=1,step_pitch=0.2)
# y.change_in_magnitude(min_mag=-18,max_mag=18,step_mag=2)
# # #the min and max and step are used to tell the function how much to change in the signal
# # #the default parameters are set inside of the class so if you want you may not enter anything
S = SoundExtraction()
# S.create_training_data(type='RNN',pitch=False, magnitude =True)
# #it is a must to set parameter pitch=true, magnitude =true to use the data which has a different magnitude or frequency
# T = RNN()
# history = T.train()
# plot(history)
# the_dnn_model="Model.h5"
the_rnn_model="D:\\echoshell\\rnn\\Virtual_Assistant-master\\SpeechRecognizer\\2019_02_13-1031_RNN\\ModelRNN.h5"
test = Recognizer(model=the_rnn_model)
# test.start("RNN")
test.testaccuracy(type="RNN")