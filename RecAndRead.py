import pyttsx3
import speech_recognition as sr
import os

class RecAndRead:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = self.engine.getProperty("rate")
        self.voices = [x for x in self.engine.getProperty("voices")]



    def ratePick(self, adjust = -10):
        self.engine.setProperty("rate", self.rate + adjust)

    def voicePick(self, voiceNum=0):
        v = self.voices[voiceNum]
        self.engine.setProperty("voice", v.id)


    def micPick(self):

        micList = [x for x in sr.Microphone.list_microphone_names()]
        for x in enumerate(micList):
            print(x)

        select = input("Chosen mic number: ")
        return int(select)

    def saySomething(self, line):
        self.ratePick()
        self.voicePick()
        self.engine.say(line)
        self.engine.runAndWait()
        self.engine.save_to_file()
    def listenTo(self):
        microphone = sr.Microphone(device_index=self.micPick())
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
            audio = recognizer.listen(source)

        try:
            response["transcription"] = recognizer.recognize_google(audio_data=audio, language="pt-BR")
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        return response


if __name__ == "__main__":



