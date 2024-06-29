from textblob import TextBlob

def analizar_sentimiento(texto):
    blob = TextBlob(texto)
    sentimiento = blob.sentiment.polarity
    if sentimiento > 0:
        return "Positivo"
    elif sentimiento < 0:
        return "Negativo"
    else:
        return "Neutral"

def main():
    texto = input("Ingresa un texto para analizar su sentimiento: ")
    resultado = analizar_sentimiento(texto)
    print(f"El sentimiento del texto es: {resultado}")

if __name__ == "__main__":
    main()
