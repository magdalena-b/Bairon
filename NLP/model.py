import transformers
import gpt_2_simple as gpt2
import tensorflow
import time

length = 200

graph = tensorflow.get_default_graph()

with graph.as_default():
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='shakespeare')

class PoemGenerator:

    def generate(self, *args, **kwargs):
        global graph
        try:
            first_line = kwargs["first_line"]
        except:
            first_line = ""

        start = time.time()
        with graph.as_default():
            text = gpt2.generate(sess, run_name='shakespeare', prefix = first_line, length = length, return_as_list=True)[0]
            sentiment = "normal"
        print("generating time:",time.time()-start,"s")
        return text, sentiment

poem_generator = PoemGenerator()