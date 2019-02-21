import os
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import string
cwd = os.path.abspath(os.path.join("", os.pardir))
Dir = cwd+"/custom_audio"
Official_directory=cwd+"/audio"
catdir = cwd+"/Categories.txt"
Magnitude=cwd+"/custom_magnitude"
f = open(catdir, "r")
CATEGORIES = f.read().replace('\n', ',').split(',')
f.close()
#print(Dir)
class changing_wav_files:
    def __init__(self,categories= CATEGORIES, directory = Dir, files_directory=Official_directory,mag=Magnitude):
        self.categories = categories
        self.new_dir = directory
        self.old_directory=files_directory
        self.magnitude_directory=mag
        #print("The new directory")
        #print(self.new_dir )
        #print("The old directory")
        #print(self.old_directory)
        l = []
        y = []
        for file in os.listdir(self.new_dir):
            l.append(str(file))
        for cat in self.categories:
            if cat not in l:
                print("the word '", cat, "' does't have a folder but it will be added  :)")
                os.makedirs(self.new_dir + "/" + cat)
        for file in os.listdir(self.magnitude_directory):
            y.append(str(file))
        for cat in self.categories:
            if cat not in y:
                print("the word '", cat, "' does't have a folder but it will be added  :)")
                os.makedirs(self.magnitude_directory + "/" + cat)
    def play_with_pitch(self,min_pitch=0.3,max_pitch=1,step_pitch=0.2):
        for category in self.categories:
            path = os.path.join(self.old_directory, category)#i get directory el beywadeny li kol el files
            #print("The path is ")
            #print(path)
            # badeey li kol category a kind of an index mo3yan fa maslan close the light 3anadah category 4
            for file in sorted(os.listdir(path)):
                file = self.old_directory + "/" + category + "/" + file
                file=file.replace("/","//")
                #print("the file is")
                # print(file)
                #kda ana ma3aya files el betstart mn 1 li 27
                #i want to start editting in them
                try:
                    for pitching in np.arange(min_pitch, max_pitch, step_pitch):
                          sound = AudioSegment.from_file(file, format="wav")
                          octaves = pitching
                          new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
                          hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
                          hipitch_sound = hipitch_sound.set_frame_rate(44100)
                          test=self.get_last_number(category)+1
                          data=self.new_dir+"/"+category+"/"+str(test)+".wav"
                          # #print(data)
                          hipitch_sound.export(data, format="wav")
                except Exception as e:
                    print(e)
                    pass

    def get_last_number(self, cat):
            path = os.path.join(self.new_dir, cat)
            m = 1000
            for file in sorted(os.listdir(path)):
                tmp = int(str(file.replace('.wav', '')))
                if m < tmp:
                    m = tmp
            return m
    def get_last_number_mag(self, cat):
            path = os.path.join(self.magnitude_directory, cat)
            m = 1000
            for file in sorted(os.listdir(path)):
                tmp = int(str(file.replace('.wav', '')))
                if m < tmp:
                    m = tmp
            return m
    def change_in_magnitude(self,min_mag=-16,max_mag=16,step_mag=4):
        for category in self.categories:
            path = os.path.join(self.old_directory, category)#i get directory el beywadeny li kol el files
            #print("The path is ")
            #print(path)
            # badeey li kol category a kind of an index mo3yan fa maslan close the light 3anadah category 4
            for file in sorted(os.listdir(path)):
                file = self.old_directory + "/" + category + "/" + file
                file=file.replace("/","//")
                #print("the file is")
                #print(file)
                #kda ana ma3aya files el betstart mn 1 li 27
                #i want to start editting in them
                try:
                    for mag in np.arange(min_mag, max_mag, step_mag):
                        if mag is not 0:
                            song = AudioSegment.from_file(file, format="wav")
                            song = song + mag
                            song=song.set_frame_rate(44100)
                            test = self.get_last_number_mag(category) + 1
                            data = self.magnitude_directory + "/" + category + "/" + str(test) + ".wav"
                            song.export(data,format="wav")
                except Exception as e:
                    print(e)
                    pass
