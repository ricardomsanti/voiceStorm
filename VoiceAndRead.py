import pyttsx3
import speech_recognition as sr

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = self.engine.getProperty("rate")
        self.voices = [x for x in self.engine.getProperty("voices")]
        self.recon = sr.Recognizer()
        self.Mic = sr.Microphone(device_index=0)
        self.micList = self.Mic.list_microphone_names()
        self.response = { "success": True,
                            "error": None,
                            "transcription": None}

    def ratePick(self, adjust = -10):
        self.engine.setProperty("rate", self.rate + adjust)

    def voicePick(self, voiceNum=0):
        v = self.voices[voiceNum]
        self.engine.setProperty("voice", v.id)

    def micPick(self):
        for x in enumerate(self.micList):
            print(x)
        select = input("Chosen mic number: ")
        self.Mic(device_index=int(select))

    def listenTo(self):
        self.micPick()
        with self.Mic as source:
            self.recon.adjust_for_ambient_noise(source)
            audio = self.recon.listen(source, timeout=3)
        try:
            self.response["transcription"] = self.recon.recognize_google(audio, language="pt-BR")
        except sr.RequestError:
            self.response["success"] = False
            self.response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            self.response["error"] = "Unable to recognize speech"
        return self.response

    def saySomething(self, line):
        self.ratePick()
        self.voicePick()
        self.engine.say(line)
        self.engine.runAndWait()





vs = Voice()
vs.listenTo()