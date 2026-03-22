import nltk
from nltk.corpus import stopwords

# Download the dataset containing common stop words in various languages
nltk.download("stopwords") 

# %% 1. English Stop Words Analysis (NLTK)
stop_words_eng = set(stopwords.words("english"))

# Sample English text
text_eng = "There are some examples of handling stop words from some texts"
text_list_eng = text_eng.split()

# If the word is not in the English stop words list, add it to the filtered list
filtered_words_eng = [word for word in text_list_eng if word.lower() not in stop_words_eng]
print(f"1. Filtered English Words: {filtered_words_eng}")


# %% 2. Turkish Stop Words Analysis (NLTK)
stop_words_tr = set(stopwords.words("turkish"))

# Sample Turkish text 
text_tr = "merhaba arkadaslar çok güzel bir ders işliyoruz. bu ders faydalı mı"
text_list_tr = text_tr.split()

# Filtering out the Turkish stop words
filtered_words_tr = [word for word in text_list_tr if word.lower() not in stop_words_tr]
print(f"\n2. Filtered Turkish Words: {filtered_words_tr}")


# %% 3. Custom (Library-Free) Stop Words Removal
# Defining our own custom Turkish stop words list
custom_stop_words = ["için", "bu", "ile", "mu", "mi", "özel"]

# Sample text
custom_text = "Bu bir denemedir. Amacımız bu metinde bulunan özel karakterleri elemek mi acaba?"

# Filtering out the custom stop words
filtered_words_custom = [word for word in custom_text.split() if word.lower() not in custom_stop_words]

# Extracting which stop words were actually caught in the text
caught_stop_words = set([word.lower() for word in custom_text.split() if word.lower() in custom_stop_words])

print(f"\n3. Custom Filtered Words: {filtered_words_custom}")
print(f"   Caught Stop Words: {caught_stop_words}")