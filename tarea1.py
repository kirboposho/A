import time
while True:    
    meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso", "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado",}

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print("Significado:")
        time.sleep(1)
        print(meme_dict[word])
    else:
        print("No se encontró esa palabra ")
    time.sleep(1)
    print("-------------------------------------------------")
