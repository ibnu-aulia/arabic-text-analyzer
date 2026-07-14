with open("arabic_text.txt", "r", encoding="utf-8") as f:
    contents = f.read()


class ArabicTextAnalyzer:
    def __init__(self, arabic_text):
        self.arabic_text = (
            arabic_text.replace("#", "")
            .replace(",", "")
            .replace(".", "")
            .replace("*", "")
            .replace("()", "")
            .replace("?", "")
            .replace("~", "")
            .replace("<", "")
            .replace(">", "")
            .replace("&", "")
            .replace("^", "")
            .replace("+", "")
            .replace("@", "")
            .replace("!", "")
            .replace("$", "")
            .replace("%", "")
            .replace("×", "")
            .replace("،", "")
            .replace(":", "")
            .replace(";", "")
            .replace("'", "")
        )

    def count_words(self):
        return len(self.arabic_text.split())

    def count_letters(self):
        return len(self.arabic_text.replace(" ", ""))

    def count_letters_unique(self):
        return len(set(self.arabic_text.replace(" ", "")))

    def word_frequency(self):
        count = {}
        for k in self.arabic_text.split():
            count[k] = count.get(k, 0) + 1
        return max(count, key=count.get)

    def longest_word(self):
        return max(self.arabic_text.split(), key=len)


text_analyzer = ArabicTextAnalyzer(contents)

with open("analysis_result.txt", "w", encoding="utf-8") as f:
    f.write(f"word count: {text_analyzer.count_words()}\n")
    f.write(f"letter count: {text_analyzer.count_letters()}\n")
    f.write(f"letter unique count: {text_analyzer.count_letters_unique()}\n")
    f.write(f"word frequency count: {text_analyzer.word_frequency()}\n")
    f.write(f"longest_word: {text_analyzer.longest_word()}\n")
