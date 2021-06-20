import stt
import librosa
import numpy as np

class sttHelper():
    
    def __init__(self):
        self.en_model =  stt.Model("/root/deepspeech/userbot/userbot/models/en_model.pbmm")
        self.en_model.enableExternalScorer("/root/deepspeech/userbot/userbot/models/en_scorer.scorer")
        self.dv_model =  stt.Model("/root/deepspeech/userbot/userbot/models/dv_model.pbmm")


    def do_stt(self,filename,model_lang="en"):
        data, sample_rate = librosa.load(filename)
        int16 = (data * 32767).astype(np.int16)

        if model_lang == "en":
            text = self.en_model.stt(int16)
            return text

        if model_lang =="dv":
            text = self.dv_model.stt(int16)
            return text





    

