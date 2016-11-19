import textmining



def create_frequency_matrix(documents, cutoff=2, path_to_save=None):
    tdm = textmining.TermDocumentMatrix()
    for doc in documents:
        tdm.add_doc(doc)
    if not path_to_save == None:
        tdm.write_csv(path_to_save,cutoff=cutoff)
    return tdm.rows(cutoff=cutoff)

