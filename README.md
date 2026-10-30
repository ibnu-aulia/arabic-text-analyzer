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

## Tech
Python, pandas, scikit-learn, NLTK, matplotlib, seaborn

## License
MIT
