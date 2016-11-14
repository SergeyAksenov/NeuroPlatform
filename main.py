__author__ = 'Sergey'

from tokenize import *

bt = base_tokenizer_factory().get_tokenizer()

print bt.tokenize("Hello, my name is??... Sergey!!",input_delimiters=['\?','\.','\n',';','!'])