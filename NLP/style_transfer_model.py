from simpletransformers.t5 import T5Model
from pprint import pprint
import os



class StyleTransferGenerator():

    def __init__():

        self.args = {
            "overwrite_output_dir": True,
            "max_seq_length": 256,
            "max_length": 50,
            "top_k": 50,
            "top_p": 0.95,
            "num_return_sequences": 5,
        }
        
        # self.model_path = "./shakespeare_T5"
        # self.model = T5Model("t5", self.model_path, args = self.args)

    
    def generate(self, *args, **kwargs):
        # prefix = "paraphrase"
        # line = kwargs["line"]
        # predictions = trained_model.predict([f'{prefix}: {line}'])
        # predicitions = predictions[0]
        # return predicitions[0]
        return "Translated to shakespearian"


