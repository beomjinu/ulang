import ulang

text_input = Element("text_input")
result = Element("result")

def encryption(*args):
    sentence = text_input.value
    result.element.innerText = ulang.encryption(sentence) 

def decryption(*args):
    sentence = text_input.value
    result.element.innerText = ulang.decryption(sentence)


