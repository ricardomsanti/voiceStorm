import pyttsx3
import speech_recognition as sr


class RecAndRead:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = self.engine.getProperty("rate")
        self.voices = [x for x in self.engine.getProperty("voices")]
        self.defaultIndex = 1



    def ratePick(self, adjust = + 10):
        self.engine.setProperty("rate", self.rate + adjust)

    def voicePick(self, voiceNum=0):
        v = self.voices[voiceNum]
        self.engine.setProperty("voice", v.id)

    def micPick(self):
        micList = [x for x in sr.Microphone.list_microphone_names()]
        for x in enumerate(micList):
            print(x)

        self.defaultIndex = int(input("Chosen mic number: "))


    def saySomething(self, line):
        self.ratePick()
        self.voicePick()
        self.engine.say(line)
        self.engine.runAndWait()

    def listenTo(self):
        microphone = sr.Microphone(device_index=self.defaultIndex)
        recognizer = sr.Recognizer()

        response = {"success": True,
                    "error": None,
                    "transcription": None}

        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source=source, timeout=4)

        try:
            response["transcription"] = recognizer.recognize_google(audio_data=audio, language="pt-BR")
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        return response["transcription"]

    def askAndListen(self, ask_line):
        ask = self.saySomething(ask_line)
        listen = self.listenTo()
        return listen