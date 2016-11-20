import textmining
import numpy as np



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


class base_frequency_matrix_creator_factory:

    def __init__(self, n_gram = 1, language='English'):
        self.n_gram = n_gram
        self.language = 'English'

    def get_frequency_matrix_creator(self):
        return


########################################################################################################################


class base_frequency_matrix_creator:

    
