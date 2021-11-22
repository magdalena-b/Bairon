from backend.models import POETS
import transformers
import text2emotion as te
import gpt_2_simple as gpt2
import tensorflow
import time
import json

length = 200
line_length = 10
graph = tensorflow.get_default_graph()
sess = gpt2.start_tf_sess()
collab_lines_cache = ""

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

        try:
            if style == "Shakespeare":
                
                load_model("shakespeare2")
                start = time.time()
                with graph.as_default():
                    text = gpt2.generate(sess, run_name='shakespeare2', prefix = first_line, length = length, return_as_list=True)[0]
                    sentiment_analysis = te.get_emotion(text)
                    sentiment = json.dumps(sentiment_analysis)
                print("generating time:",time.time()-start,"s")
            
            elif style == "Ginsberg":
                
                load_model("ginsberg2")
                start = time.time()
                with graph.as_default():
                    text = gpt2.generate(sess, run_name='ginsberg2', prefix = first_line, length = length, return_as_list=True)[0]
                    sentiment_analysis = te.get_emotion(text)
                    sentiment = json.dumps(sentiment_analysis)
                print("generating time:",time.time()-start,"s")

            elif style == "Cummings":
                
                load_model("cummings2")
                start = time.time()
                with graph.as_default():
                    text = gpt2.generate(sess, run_name='cummings2', prefix = first_line, length = length, return_as_list=True)[0]
                    sentiment_analysis = te.get_emotion(text)
                    sentiment = json.dumps(sentiment_analysis)
                print("generating time:",time.time()-start,"s")
                
            else: raise Exception("Style not found")

        except: # lorem ipsum request or models unvaible
            #text = "Tempor eiusmod deserunt pariatur eu magna sit velit mollit cupidatat qui fugiat.\nLorem esse quis irure labore aliquip. Qui proident aliqua non voluptate deserunt id culpa velit. Pariatur duis minim esse est.\nEt commodo pariatur est exercitation duis. Id qui voluptate minim magna eiusmod.\nLaboris magna dolore sunt nisi fugiat proident irure magna ullamco et sint sit sint.\nIn cupidatat do commodo ex officia anim ad occaecat magna aliqua. Commodo labore aute ut ullamco mollit. Et pariatur aliqua velit sit nisi voluptate commodo sit officia labore eu nulla consectetur.\nLaborum dolore sint nulla voluptate in consequat.\nConsectetur anim laboris in ullamco ex sint laborum laborum non est ullamco occaecat mollit.\nEiusmod laboris est minim culpa aliquip deserunt nostrud nostrud ut. Excepteur mollit proident nisi duis pariatur. Est sint commodo velit enim dolor sit.\nSunt commodo anim dolor et. Deserunt consectetur incididunt do occaecat magna et laborum veniam exercitation minim."
            text = """ROSES, their sharp spines being gone,
Not royal in their smells alone,
   But in their hue;
Maiden pinks, of odour faint,
Daisies smell-less, yet most quaint,
   And sweet thyme true;

Primrose, firstborn child of Ver;
Merry springtime's harbinger,
   With her bells dim;
Oxlips in their cradles growing,
Marigolds on death-beds blowing,
   Larks'-heels trim;

All dear Nature's children sweet
Lie 'fore bride and bridegroom's feet,
   Blessing their sense!
Not an angel of the air,
Bird melodious or bird fair,
   Be absent hence!

The crow, the slanderous cuckoo, nor
The boding raven, nor chough hoar,
   Nor chattering pye,
May on our bride-house perch or sing,
Or with them any discord bring,
   But from it fly!"""            
            sentiment_analysis = te.get_emotion(text)
            sentiment = json.dumps(sentiment_analysis)
            
        return text, sentiment


    def generate_line(self, *args, **kwargs):
        global graph
        global line_length
        global collab_lines_cache
        try:
            style = kwargs["style"]
            first_line = kwargs["first_line"]
            collab_lines_cache += " " + first_line
            print("\n\n" + collab_lines_cache)
        except:
            first_line = ""

        try:
            if style == "Shakespeare":
                
                load_model("shakespeare2")
                start = time.time()
                with graph.as_default():
                    text = gpt2.generate(sess, run_name='shakespeare2', prefix = collab_lines_cache, length = line_length, return_as_list=True)[0]
                    sentiment_analysis = te.get_emotion(text)
                    sentiment = json.dumps(sentiment_analysis)
                print("generating time:",time.time()-start,"s")
            
            elif style == "Ginsberg":
                
                load_model("ginsberg2")
                start = time.time()
                with graph.as_default():
                    text = gpt2.generate(sess, run_name='ginsberg2', prefix = collab_lines_cache, length = line_length, return_as_list=True)[0]
                    sentiment_analysis = te.get_emotion(text)
                    sentiment = json.dumps(sentiment_analysis)
                print("generating time:",time.time()-start,"s")

            elif style == "Cummings":
                
                load_model("cummings2")
                start = time.time()
                with graph.as_default():
                    text = gpt2.generate(sess, run_name='cummings2', prefix = collab_lines_cache, length = line_length, return_as_list=True)[0]
                    sentiment_analysis = te.get_emotion(text)
                    sentiment = json.dumps(sentiment_analysis)
                print("generating time:",time.time()-start,"s")
                
            else: raise Exception("Style not found")

        except Exception as e: # lorem ipsum request or models unvaible
            print(e)
            text = """ROSES, their sharp spines being gone,
Not royal in their smells alone,
   But in their hue;
Maiden pinks, of odour faint,
Daisies smell-less, yet most quaint,
   And sweet thyme true;

Primrose, firstborn child of Ver;
Merry springtime's harbinger,
   With her bells dim;
Oxlips in their cradles growing,
Marigolds on death-beds blowing,
   Larks'-heels trim;

All dear Nature's children sweet
Lie 'fore bride and bridegroom's feet,
   Blessing their sense!
Not an angel of the air,
Bird melodious or bird fair,
   Be absent hence!

The crow, the slanderous cuckoo, nor
The boding raven, nor chough hoar,
   Nor chattering pye,
May on our bride-house perch or sing,
Or with them any discord bring,
   But from it fly!"""      

        sentiment_analysis = te.get_emotion(text)
        sentiment = json.dumps(sentiment_analysis)
        collab_lines_cache = text  
              
        return text, sentiment


    def clear_collab_lines_cache(self):
        global collab_lines_cache
        collab_lines_cache = ""
        print("CACHE CLEARD")

poem_generator = PoemGenerator()