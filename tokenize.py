__author__ = 'Sergey'

import re

########################################################################################################################


class base_tokenizer:


    def __init__(self, stop_words=None):
        self.language=''
        if not stop_words == None:
            self.stop_words = stop_words


    def tokenize(self, input, input_delimiters=None, output_delimiter=' '):
        terms = []
        if input_delimiters == None:
            terms = re.findall(r"[\w']+", input)
        else:
            #splits = " |".join(input_delimiters)
           # print(splits)
            terms = re.split("|".join(input_delimiters), input)
            #terms = re.split('; |, |\*|\n|\.|\?|!|\t', input)
        return output_delimiter.join(terms)


########################################################################################################################


class base_tokenizer_factory:


    def __init__(self, language="English"):
        self.language = language


    def get_language(self):
        return self.language


    def get_tokenizer(self):
        return base_tokenizer(self.language)


########################################################################################################################



