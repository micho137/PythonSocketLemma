import spacy

def preprocess_text(text):
    # Aqui cargamos el modelo spañol de Spacy
    # nlp = spacy.load('es_core_news_sm') # Modelo Eficiente
    nlp = spacy.load('es_dep_news_trf') # Modelo Preciso

    # Se definen los STOP WORDS excluyendo los prononmbres y terminos a utilizar 
    stop_words = set(['además','las', 'los' 'ante', 'cabe','en', 'e', 'a', 'el', 'hacia', 'lo'
                      ,'según','tras','le','la','al','es','.', ',', 'de'])

    # POS tags permitidos (Pronombres, Verbos, Adjetivos)
    allowed_tags = ['PRON', 'VERB', 'ADJ']

    # Procesar el texto con Spacy
    doc = nlp(text)

    processed_text = []

    # Iterar los tokens en el texto procesado
    for token in doc:
        # Verificar si el token no es una STOP WORD (excluyendo los pronombres) y si el POS tag se encuentra en los tags permitidos
        if token.text.lower() not in stop_words or token.pos_ in allowed_tags:
            # Lemmatize the token
            if token.ent_type_ == 'PER':
                # Spell out the name character by character and add it to the processed text
                spelled_name = list(token.text)
                processed_text.extend(spelled_name)
            else:
                # Lemmatize the token and add it to the processed text
                lemma = token.lemma_
                processed_text.append(lemma)

    return processed_text