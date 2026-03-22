# NLP Stop Words Removal 🛑

This repository demonstrates how to filter out "stop words" from text using Natural Language Processing (NLP) techniques in Python. Stop words are commonly used words (like "the", "a", "is", "bu", "ve") that generally do not contribute much to the meaning of a sentence and are often removed to optimize text analysis models.

## 🚀 Features
- **English Stop Words Removal:** Utilizing NLTK's built-in English corpus to filter out noisy words.
- **Turkish Stop Words Removal:** Utilizing NLTK's built-in Turkish corpus to clean Turkish text.
- **Custom Stop Words Removal:** Creating a manual, library-free list of stop words to filter out domain-specific or custom keywords without relying on external datasets.

## 🛠️ Libraries Used
- `nltk` (Natural Language Toolkit)
  - `stopwords` corpus

## 💻 How to Run
1. Ensure NLTK is installed (`pip install nltk`).
2. Run the Python script. The script will automatically download the required NLTK stopwords dataset on its first execution.
3. Observe the terminal output to see the difference between the original text and the filtered word lists.
