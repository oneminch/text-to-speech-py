import nltk
from newspaper import Article
from gtts import gTTS


class TextToSpeech:
    def __init__(self, url):
        self.lang = "en"
        self.article = Article(url)
        self.article.download()
        self.article.parse()
        nltk.download('punkt')
        self.article.nlp()
        self.article_text = self.article.text
        
        print("Initialized...")

    def generate_audio(self):
        try:
            audio = gTTS(text=self.article_text, lang=self.lang, slow=False)
            audio.save("article_audio.mp3")
            print("Audio saved...")
        except Exception:
            print("There was an issue generating audio.")
    

if __name__ == '__main__':
    tts = TextToSpeech(
       url='https://oneminch.dev/articles/dns'
    )
        
    tts.generate_audio()