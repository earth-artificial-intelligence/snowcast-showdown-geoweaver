getdays = lambda keys: list(sorted([tday for tday in keys if tday[:4].isnumeric() and len(tday) == 10]))

from features_constFeatures import getconstfeatures
from features_modisFeatures import getmodisfeatures
from features_datadict import getdatadict
from features_embeddings import getembindex
from features_inputs import getinputs
