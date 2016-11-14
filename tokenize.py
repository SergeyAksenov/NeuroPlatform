__author__ = 'Sergey'

import re

########################################################################################################################


class base_tokenizer:


    def __init__(self, language='English',stop_words=None):
        self.language=language
        if not stop_words == None:
            self.stop_words = stop_words
        else:
            self.stop_words = set()

    def tokenize(self, input, input_delimiters=None, output_delimiter=' '):
        terms = []
        if input_delimiters == None:
            terms = re.findall(r"[\w']+", input)
        else:
            terms = re.split("|".join(input_delimiters), input)
        terms_without_stopwords = [t for t in terms if t not in self.stop_words and len(t) > 0]
        return output_delimiter.join(terms_without_stopwords)


########################################################################################################################


class base_tokenizer_factory:


    def __init__(self, language="English"):
        self.language = language


    def get_language(self):
        return self.language


    def get_tokenizer(self):
        return base_tokenizer(self.language)


########################################################################################################################



