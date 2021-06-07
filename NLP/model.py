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
    start = time.time()
    gpt2.reset_session(sess)
    sess = gpt2.start_tf_sess()
    graph = tensorflow.get_default_graph()
    with graph.as_default():
        gpt2.load_gpt2(sess, run_name=run_name)
    print("loading time:",time.time()-start,"s")



class PoemGenerator:

    def generate(self, *args, **kwargs):
        global graph
        global length
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
        

        if style == "Cummings":
            
            load_model("cummings")
            start = time.time()
            with graph.as_default():
                text = gpt2.generate(sess, run_name='cummings', prefix = first_line, length = length, return_as_list=True)[0]
                sentiment = "normal"
            print("generating time:",time.time()-start,"s")

        if style == "Lorem Ipsum":
            text = "Tempor eiusmod deserunt pariatur eu magna sit velit mollit cupidatat qui fugiat.\nLorem esse quis irure labore aliquip. Qui proident aliqua non voluptate deserunt id culpa velit. Pariatur duis minim esse est.\nEt commodo pariatur est exercitation duis. Id qui voluptate minim magna eiusmod.\nLaboris magna dolore sunt nisi fugiat proident irure magna ullamco et sint sit sint.\nIn cupidatat do commodo ex officia anim ad occaecat magna aliqua. Commodo labore aute ut ullamco mollit. Et pariatur aliqua velit sit nisi voluptate commodo sit officia labore eu nulla consectetur.\nLaborum dolore sint nulla voluptate in consequat.\nConsectetur anim laboris in ullamco ex sint laborum laborum non est ullamco occaecat mollit.\nEiusmod laboris est minim culpa aliquip deserunt nostrud nostrud ut. Excepteur mollit proident nisi duis pariatur. Est sint commodo velit enim dolor sit.\nSunt commodo anim dolor et. Deserunt consectetur incididunt do occaecat magna et laborum veniam exercitation minim."
            sentiment = "normal"
        
        
        return text, sentiment

poem_generator = PoemGenerator()