class TextAnalyzer(object):

    def __init__(self, text):
        self.text = text
        self.freq_all = {}

    def toLower(self):
        formattedText = self.text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')
        return formattedText.lower()

    def findFreq(self):
        low_str = self.toLower()
        words_list = low_str.split(" ")
        words_set = set(words_list)
        freqDict = {}
        for word in words_set:
            freqDict[word] = words_list.count(word)
            print(word)
        self.freq_all = freqDict
        return freqDict

    def freqWord(self,word):
        return self.freq_all.get(word)

ta = TextAnalyzer("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
print(ta.findFreq())
print(ta.freqWord("lorem"))
print(ta.freqWord("awinas"))
