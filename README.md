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

Code: [ArabicTextAnalyzer.py](https://github.com/ibnu-aulia/arabic-text-analyzer/blob/main/ArabicTextAnalyzer.py)

### Why I Built This
Practicing OOP concepts in Python while building tools relevant to my future path in Arabic NLP.

## 2. EDA Notebook: Arabic Reviews

[arabic_reviews_eda.ipynb](https://github.com/ibnu-aulia/arabic-text-analyzer/blob/main/arabic_reviews_eda.ipynb) is an exploratory data analysis of an Arabic reviews dataset (~100k reviews).

- Top 10 most frequent words, before and after removing Arabic stopwords
- Bar chart with properly rendered Arabic labels (`arabic_reshaper`, `python-bidi`)
- Text features (word count, letter count, average word length) with a correlation heatmap

### Key findings
- `word_count` and `letter_count` are almost perfectly correlated (~0.998), because more words means more letters.

## 3. First Neural Network: Arabic Sentiment

[arabic_sentiment_first_neural_net.ipynb](https://github.com/ibnu-aulia/arabic-text-analyzer/blob/main/arabic_sentiment_first_neural_net.ipynb) is my first neural network in PyTorch, trained to classify short Arabic reviews as good (1) or bad (0).

- Code counts good and bad words in each sentence, turning it into two numbers
- A 2-layer network (2 inputs, 3 neurons, ReLU, 1 neuron, sigmoid) is trained on them
- Trained for 500 epochs on a Colab T4 GPU

### Result
Loss dropped to about 0.05 and accuracy reached 1.0 on 8 sentences.

### Key findings
- Words are matched exactly, so a word with the definite article (السيء instead of سيء) or a spelling variant (hamza/alif forms, ي vs ى) is not counted, and the sentence can look neutral.
- Accuracy was measured on the training sentences only, so it does not show how the model handles new sentences.

### Next
Normalize Arabic text before counting, and test on unseen sentences (done in section 4).

## 4. Arabic Restaurant Review Sentiment

`arabic_review_sentiment.ipynb` classifies Arabic restaurant reviews as positive or negative
using TF-IDF features and scikit-learn. Data: [ArRestReviews](https://huggingface.co/datasets/hadyelsahar/ar_res_reviews) (8,364 reviews).

- Explored the data: labels are imbalanced (71% positive), and negative reviews are longer.
- Wrote an Arabic normalization function (alef variants, ي/ى, removing non-Arabic characters)
  and removed 47 empty and 80 duplicate reviews.
- Split the data 80/20 (stratified) and compared five models.

### Result

| Model | Accuracy | Recall (negative) | F1 (negative) |
|---|---|---|---|
| Always predict "positive" | 0.71 | 0.00 | - |
| Logistic Regression | 0.84 | 0.52 | 0.65 |
| Logistic Regression, balanced | 0.84 | 0.76 | 0.74 |
| Random Forest, balanced | 0.83 | 0.53 | 0.65 |
| Best: LR, balanced, 20k uni+bigrams | 0.86 | 0.77 | 0.76 |

### Key findings
- Accuracy hides the problem: the plain model missed almost half of the negative reviews.
  Balanced class weights fixed most of that.
- A more complex model (Random Forest) did not help.
- Reading the mistakes by hand showed that negation (e.g. ما انصح, "I don't recommend")
  is the main failure, because TF-IDF counts words, not their order.

### Limitations
Five models were compared on the same test set, so the best score is slightly optimistic.
Arabizi (Arabic in Latin letters) is dropped by the cleaning step.

### Next
Cross-validation, better handling of negation and dialect, and fine-tuning a pretrained
Arabic model (AraBERT).

[Open the notebook](https://github.com/ibnu-aulia/arabic-text-analyzer/blob/main/arabic_review_sentiment.ipynb)

## 5. Arabic Tokenization Experiments

[arabic_tokenization_experiments.ipynb](https://github.com/ibnu-aulia/arabic-text-analyzer/blob/main/arabic_tokenization_experiments.ipynb) compares several ways to split Arabic text into tokens, and shows where each one breaks.

- Plain `split()` vs a regex that keeps only Arabic letters
- The same meaning needs 4 tokens in Arabic and 10 in English
- A mini stemmer, and TF-IDF written from scratch (matches scikit-learn exactly)
- Tokenizers: AraBERT v2 on raw text, AraBERT v02, Farasa, and Stanza
- My own splitter for the prefix و, using word counts from the reviews

### Key findings
- The model, the tokenizer, and the preprocessing must match. AraBERT v2 on raw text gave broken subwords without any error message.
- No tool separated the و perfectly. The word `والد` ("father") was wrongly split by the mini stemmer and by Stanza.
- My own splitter worked on 5 test words only, and its threshold is my own choice. It is an experiment, not a finished tool.
  
## Tech
Python, pandas, scikit-learn, NLTK, PyTorch, matplotlib, seaborn, Hugging Face datasets and transformers, Stanza

## License
MIT
