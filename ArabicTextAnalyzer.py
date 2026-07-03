with open("arabic_text.txt", "r", encoding="utf-8") as f:
    contents = f.read()


class ArabicTextAnalyzer:
    def __init__(self, arabic_text):
        self.arabic_text = arabic_text

    def count_words(self):
        return len(self.arabic_text.split())

    def count_letters(self):
        return len(self.arabic_text.replace(" ", "").replace(",", "").replace(".", ""))


text_analyzer = ArabicTextAnalyzer(contents)

with open("analysis_result.txt", "w", encoding="utf-8") as f:
    f.write(f"word count: {text_analyzer.count_words()}\n")
    f.write(f"letter count: {text_analyzer.count_letters()}\n")
