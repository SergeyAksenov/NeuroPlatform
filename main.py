__author__ = 'Sergey'

from tokenize import *
from frequency import *

bt = base_tokenizer_factory().get_tokenizer()

words = bt.tokenize("Hello, my name is??... Sergey!!",input_delimiters=['\?','\.','\n',';','!',','])

wcp = base_frequency_processor_factory().get_frequency_processor()
words = words.replace('  ',' ')

some = wcp.process(words)

tmp  = some.split('\t')
print (words)
for t in tmp:
    print t
#print words

