# Arabic Text Analyzer

Python tools for analyzing Arabic text.

## 1. ArabicTextAnalyzer

Simple Python tool to analyze Arabic text from a text file.

### Features
- Count total words in Arabic text
- Count total characters (excluding spaces and punctuation)
- Count total unique letters in Arabic text
- Find the most used word in Arabic text
- Find the longest word in Arabic text

### How to Use
1. Put your Arabic text in `arabic_text.txt`
2. Run the script
3. Results are saved to `analysis_result.txt`

### Why I Built This
Practicing OOP concepts in Python while building tools relevant to my future path in Arabic NLP.

## 2. EDA Notebook: Arabic Reviews

`arabic-reviews-eda.ipynb` is an exploratory data analysis of an Arabic reviews dataset (~100k reviews).

- Top 10 most frequent words, before and after removing Arabic stopwords
- Bar chart with properly rendered Arabic labels (`arabic_reshaper`, `python-bidi`)
- Text features (word count, letter count, average word length) with a correlation heatmap

### Key findings
- `word_count` and `letter_count` are almost perfectly correlated (~0.998), because more words means more letters.

## 3. First Neural Network: Arabic Sentiment

`arabic-sentiment-first-neural-net.ipynb` is my first neural network in PyTorch, trained to classify short Arabic reviews as good (1) or bad (0).

- Code counts good and bad words in each sentence, turning it into two numbers
- A 2-layer network (2 inputs, 3 neurons, ReLU, 1 neuron, sigmoid) is trained on them
- Trained for 500 epochs on a Colab T4 GPU

### Result
Loss dropped to about 0.006 and accuracy reached 1.0 on 8 sentences.

### Key findings
- Words are matched exactly, so a word with the definite article (السيء instead of سيء) or a spelling variant (hamza/alif forms, ي vs ى) is not counted, and the sentence can look neutral.
- Accuracy was measured on the training sentences only, so it does not show how the model handles new sentences.

### Next
Normalize Arabic text before counting, and test on unseen sentences.

## Tech
Python, pandas, scikit-learn, NLTK, PyTorch, matplotlib, seaborn

## License
MIT
