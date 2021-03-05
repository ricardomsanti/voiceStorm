import pyttsx3

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.rate = self.engine.getProperty("rate")
        self.voices = [x for x in self.engine.getProperty("voices")]

    def ratePick(self, adjust = -10):
        self.engine.setProperty("rate", self.rate + adjust)

    def voicePick(self, voiceNum=0):
        v = self.voices[voiceNum]
        self.engine.setProperty("voice", v.id)

    def saySomething(self, line):
        self.ratePick()
        self.voicePick()
        self.engine.say(line)
        self.engine.runAndWait()
