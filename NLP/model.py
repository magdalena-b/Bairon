from backend.models import POETS
import transformers
import gpt_2_simple as gpt2
import tensorflow
import time

length = 200
graph = tensorflow.get_default_graph()
sess = gpt2.start_tf_sess()

def load_model(run_name):
    global sess
    global graph
    gpt2.reset_session(sess)
    sess = gpt2.start_tf_sess()
    graph = tensorflow.get_default_graph()
    with graph.as_default():
        gpt2.load_gpt2(sess, run_name=run_name)



class PoemGenerator:

    def generate(self, *args, **kwargs):
        global graph
        try:
            style = kwargs["style"]
            first_line = kwargs["first_line"]
        except:
            first_line = ""


        if style == "Shakespeare":
            
            load_model("shakespeare")
            start = time.time()
            with graph.as_default():
                text = gpt2.generate(sess, run_name='shakespeare', prefix = first_line, length = length, return_as_list=True)[0]
                sentiment = "normal"
            print("generating time:",time.time()-start,"s")
        
        if style == "Ginsberg":
            
            load_model("ginsberg")
            start = time.time()
            with graph.as_default():
                text = gpt2.generate(sess, run_name='ginsberg', prefix = first_line, length = length, return_as_list=True)[0]
                sentiment = "normal"
            print("generating time:",time.time()-start,"s")
        

        if style == "cummings":
            
            load_model("cummings")
            start = time.time()
            with graph.as_default():
                text = gpt2.generate(sess, run_name='cummings', prefix = first_line, length = length, return_as_list=True)[0]
                sentiment = "normal"
            print("generating time:",time.time()-start,"s")

        
        
        return text, sentiment

poem_generator = PoemGenerator()