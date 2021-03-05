import pyttsx3
import speech_recognition as sr

class RecAndRead:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = self.engine.getProperty("rate")
        self.voices = [x for x in self.engine.getProperty("voices")]
        self.recon = sr.Recognizer()
        self.mic = sr.Microphone(device_index=7)
        self.response = { "success": True,
                            "error": None,
                            "transcription": None}

    def ratePick(self, adjust = -10):
        self.engine.setProperty("rate", self.rate + adjust)

    def voicePick(self, voiceNum=0):
        v = self.voices[voiceNum]
        self.engine.setProperty("voice", v.id)

    def micPick(self):
        micList = [x for x in sr.Microphone.list_microphone_names]
        for x in enumerate(micList):
            print(x)
        select = input("Chosen mic number: ")
        self.mic(device_index=int(select))

    def listenTo(self):
        with self.mic as source:
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





vs = RecAndRead().listenTo()
