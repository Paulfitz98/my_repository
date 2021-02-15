import pyttsx3
import PyPDF2
book = open('pythonbook1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)


converter = pyttsx3.init()
converter.setProperty('rate', 120)
converter.setProperty('volume', 0.7)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
converter.setProperty('voice', voice_id)
converter.say("Well Yaw Whats the craic son?")
converter.say("story lad")

converter.runAndWait()
voices = converter.getProperty('voices')

for voice in voices:
    # to get the info. about various voices in our PC
    print("Voice:")
    print("ID: %s" % voice.id)
    print("Name: %s" % voice.name)
    print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    print("Languages Known: %s" % voice.languages)



# speaker = pyttsx3.init()
# for num in range(7, pages):
# page = pdfReader.getPage(1)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()



