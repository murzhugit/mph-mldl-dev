#from os import system
#system('say stupid apple')

from AppKit import NSSpeechSynthesizer
speechSynthesizer = NSSpeechSynthesizer.alloc().initWithVoice_("com.apple.speech.synthesis.voice.Bruce")
speechSynthesizer.startSpeaking('Hi! Nice to meet you!')
