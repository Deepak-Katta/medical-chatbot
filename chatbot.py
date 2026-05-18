import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def get_response(user_input):

    user_input = user_input.lower()

    tokens = word_tokenize(user_input)

    if "fever" in tokens:
        return "You may have viral fever. Drink water and take rest."

    elif "headache" in tokens:
        return "Headache may occur due to stress or dehydration."

    elif "cold" in tokens or "cough" in tokens:
        return "You may have common cold symptoms."

    elif "diabetes" in tokens:
        return "Maintain healthy sugar levels and exercise regularly."

    elif "chest" in tokens and "pain" in tokens:
        return "Please contact emergency medical services immediately."

    else:
        return "Sorry, I couldn't understand your symptoms."
