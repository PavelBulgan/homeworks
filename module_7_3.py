class WordsFinder:
    def __init__(self, *file_name: str):
        self.file_names = list(file_name)


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name,'r', encoding='utf-8') as file:
                text = file.read().lower()
                for sumbol in ',.=!?;:-':
                    text = text.replace(sumbol, '')
                #print(text)
                text = text.replace('\n', ' ')
                #print(text)
                text = text.split(' ')
                #print(text)
                #text.index('english')
                #text.count('english')
            all_words[file_name] = text
        return all_words

    def find(self, word):
        self.word = word.lower()
        all_words = self.get_all_words()
        result = {}
        score = 0
        for name, key in all_words.items():
            for word in key:
                score += 1
                if word == self.word:
                    result[name] = score
                    break
        return result


    def count(self, word):
        self.word = word.lower()
        all_words = self.get_all_words()
        score = 0
        result = {}
        for name, key in all_words.items():
            for word in key:
                if word == self.word:
                    score += 1
            result[name] = score
        return result

    def count2(self, word):
        self.word = word.lower()
        all_words = self.get_all_words()




finder2 = WordsFinder('test_7_3.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('мор')) # 3 слово по счёту
print(finder2.count('engLish')) # 4 слова teXT в тексте всего