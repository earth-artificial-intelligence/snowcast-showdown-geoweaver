import torch
calcdevice = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

import models_addons as addons
# import models.catboost as catboost
import models_functions as functions
from models_models import Model,Model3
from models_oanet4s import DLOA,Model0
from models_apply import apply,valid_bs,applymodels
from models_inference import inference, test, getests
from models_loadmodels import loadmodels
