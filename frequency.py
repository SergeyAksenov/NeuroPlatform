import textmining
import numpy as np
from nltk import ngrams


########################################################################################################################


def create_frequency_matrix(documents, cutoff=2, path_to_save=None):
    # x = np.array([1, 1, 1, 2, 2, 2, 5, 25, 1, 1])
    # y = np.bincount(x)
    # ii = np.nonzero(y)[0]
    # return zip(ii, y[ii])
    tdm = textmining.TermDocumentMatrix()
    for doc in documents:
        tdm.add_doc(doc)
    if not path_to_save == None:
        tdm.write_csv(path_to_save,cutoff=cutoff)
    return tdm.rows(cutoff=cutoff)


########################################################################################################################


class base_frequency_processor_factory:

    def __init__(self, language='English'):
        self.language = 'English'

    def get_frequency_matrix_creator(self, context_size=3):
        return base_frequency_processor(self.language, context_size=context_size)


########################################################################################################################


class base_frequency_processor:

    def __init__(self, context_size=3, language='English'):
        self.context_size = context_size

    def process(self, document, input_delimiter=' ', \
                output_inner_delimiter=' ', output_outer_delimiter='\t'):
        words = document.split(input_delimiter)
        d  = {}
        for i in range(self.context_size, len(words)):
            context_words = words[i - self.context_size:i]
            for w in context_words:
                for u in context_words:
                    # if not w in d:
                    #     d[w] = {u : 1}
                    # else:
                    #     if u not in d[w]:
                    #         d[w][u] = 1
                    #     else:
                    #         d[w][u] = d[w][u] + 1
                    if not w+'__'+u in d:
                        d[w+'__'+u] = 0
                    else:
                        d[w+'__'+u] = d[w+'__'+u] + 1
        ret = []
        for k in d.keys():
            ret.append(k + output_inner_delimiter + str(d[k]))
        return output_outer_delimiter.join(ret)


########################################################################################################################

