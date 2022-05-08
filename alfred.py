from functions import flip, openFileExplorer, openvscode, remember, remembered, screenShot, takeCommandMic, tellJoke, text2Speech, time, date, email, whatsapp, openWhatsapp, wikipediaSearch, googleSearch, speak, wishme, youtubeSearch
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
    wishme()
    wakeword = 'alfred'
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        if wakeword in query:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'email' in query:
                email()
            elif 'message' in query:
                whatsapp()
            elif 'whatsapp' in query:
                openWhatsapp()
            elif 'wikipedia' in query:
                wikipediaSearch()
            elif 'google' in query:
                googleSearch()
            elif 'youtube' in query:
                youtubeSearch()
            elif 'read' in query:
                text2Speech()
            elif 'open code' in query:
                openvscode()
            elif 'open' in query:
                openFileExplorer(query)
            elif 'joke' in query:
                tellJoke()
            elif 'screenshot' in query:
                screenShot()
            elif 'remember this' in query:
                remember()
            elif 'do you remember anything' in query:
                remembered()
            elif 'flip a coin' in query:
                flip()
            elif 'offline' in query or 'sleep' in query:
                speak('ok sir i will take my leave')
                quit()
