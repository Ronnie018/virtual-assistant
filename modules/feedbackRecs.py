from gtts import gTTS
import playsound

def feedbackCreator(text, path, lang, nickname, ext="mp3"):
  filepath = f"{path}/{nickname}.{ext}"
  tts = gTTS(text=text, lang=lang)
  tts.save(filepath)
  playsound.playsound(filepath)
  
feedbackCreator(
  "não entendi",
  "feedbacks",
  "pt-BR",
  "nao_entendi"
  )