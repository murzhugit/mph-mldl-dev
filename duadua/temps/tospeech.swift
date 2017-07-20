/ Text-to-Speech on OSX
// run: swift speech.swift "東京特許許可局"
// build: xcrun -sdk macosx swiftc speech.swift && ./speech "東京特許許可局"
//
// for OSX, use NSSpeechSYnthesizer in AppKit,
// (for iOS, use AVSpeechSynthesizer in AVFoundation)
import Foundation
import AppKit

// show the installed voice list with major attributes
for v in NSSpeechSynthesizer.availableVoices() {
    print("\"\(v)\"")
    let attrs = NSSpeechSynthesizer.attributesForVoice(v)
    // swift < 2.1(from Xcode7.1): cannot interpolate string literals inside
    if case let val? = attrs["VoiceName"]     {print(" Name:   \(val)")}
    if case let val? = attrs["VoiceLanguage"] {print(" Lang:   \(val)")}
    if case let val? = attrs["VoideGender"]   {print(" Gender: \(val)")}
    if case let val? = attrs["VoiceAge"]      {print(" Age:    \(val)")}
    //for (k, v) in attrs {print("  \(k)")}
}


// Code of text-to-speech
let loop = NSRunLoop.currentRunLoop()
let synth = NSSpeechSynthesizer()
func speech(text: String) {
    synth.startSpeakingString(text)
    let mode = loop.currentMode ?? NSDefaultRunLoopMode
    while loop.runMode(mode, beforeDate: NSDate(timeIntervalSinceNow: 0.1))
          && synth.speaking {}
}


// example: in default English
speech("Hello World!")

// example in Japanese
//synth.setVoice("com.apple.speech.synthesis.voice.kyoko.premium")
for v in NSSpeechSynthesizer.availableVoices() {
    let attrs = NSSpeechSynthesizer.attributesForVoice(v)
    if attrs["VoiceLanguage"] as? String == "ja-JP" {
        synth.setVoice(v)
        break
    }
}
speech("こんにちは世界!")

// speech commandline arguments
for m in Process.arguments[1 ..< Process.arguments.count] {
    speech(m)
}
