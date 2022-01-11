from backend.models import POETS
import transformers
import gpt_2_simple as gpt2
import tensorflow
import time
# from happytransformer import HappyGeneration
# from happytransformer import GENSettings
import text2emotion as te
import json


length = 200
line_length = 10
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
            model_type = kwargs["model_type"]
        except:
            first_line = ""

        try:
            if style == "Shakespeare":

                if model_type == "gpt2":
                    load_model("gpt2_shakespeare")
                    start = time.time()
                    with graph.as_default():
                        text = gpt2.generate(sess, run_name='gpt2_shakespeare', prefix = first_line, length = length, return_as_list=True)[0]
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    print("generating time:",time.time()-start,"s")

                if model_type == "gpt-neo":
                    try:
                        from aitextgen import aitextgen
                        ai = aitextgen(model_folder="checkpoint/neo_shakespeare/", to_gpu=False)
                        text = ai.generate_one(batch_size=5,
                            prompt=first_line,
                            max_length=200,
                            temperature=1.0,
                            top_p=0.9)
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    except Exception as e:
                        print(e)

                    # happy_gen_loaded = HappyGeneration(load_path="checkpoint/neo_shakespeare/")
                    # args = GENSettings(no_repeat_ngram_size = 2, num_beams = 5, max_length = length)
                    # result = happy_gen_loaded.generate_text(first_line, args = args)
                    # text = result.text




            elif style == "Cummings":

                if model_type == "gpt2":         
                    load_model("gpt2_cummings")
                    start = time.time()
                    with graph.as_default():
                        text = gpt2.generate(sess, run_name='gpt2_cummings', prefix = first_line, length = length, return_as_list=True)[0]
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    print("generating time:",time.time()-start,"s")

                if model_type == "gpt-neo":
                    try:
                        from aitextgen import aitextgen
                        ai = aitextgen(model_folder="checkpoint/neo_cummings/", to_gpu=True)
                        text = ai.generate(n=1,
                            batch_size=5,
                            prompt=first_line,
                            max_length=200,
                            temperature=0.7,
                            top_p=0.9)
                        # happy_gen_loaded = HappyGeneration(load_path="checkpoint/neo_cummings/")
                        # args = GENSettings(no_repeat_ngram_size=2, num_beams = 5, max_length = length)
                        # result = happy_gen_loaded.generate_text(first_line, args = args)
                        # text = result.text
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    except Exception as e:
                        print(e)



            elif style == "Whitman":

                if model_type == "gpt2":         
                    load_model("gpt2_whitman")
                    start = time.time()
                    with graph.as_default():
                        text = gpt2.generate(sess, run_name='gpt2_whitman', prefix = first_line, length = length, return_as_list=True)[0]
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    print("generating time:",time.time()-start,"s")

                if model_type == "gpt-neo":
                    try:
                        from aitextgen import aitextgen

                        ai = aitextgen(model_folder="checkpoint/neo_whitman/", to_gpu=False)
                        text = ai.generate(n=1,
                            batch_size=5,
                            prompt=first_line,
                            max_length=200,
                            temperature=0.7,
                            top_p=0.9)
                        # happy_gen_loaded = HappyGeneration(load_path="checkpoint/neo_whitman/")
                        # args = GENSettings(no_repeat_ngram_size = 2, num_beams = 5, max_length = length)
                        # result = happy_gen_loaded.generate_text(first_line, args = args)
                        # text = result.text
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    except Exception as e:
                        print(e)

                
            else: raise Exception("Style not found")

        except: # lorem ipsum request or models unvaible
            text = "Tempor eiusmod deserunt pariatur eu magna sit velit mollit cupidatat qui fugiat.\nLorem esse quis irure labore aliquip. Qui proident aliqua non voluptate deserunt id culpa velit. Pariatur duis minim esse est.\nEt commodo pariatur est exercitation duis. Id qui voluptate minim magna eiusmod.\nLaboris magna dolore sunt nisi fugiat proident irure magna ullamco et sint sit sint.\nIn cupidatat do commodo ex officia anim ad occaecat magna aliqua. Commodo labore aute ut ullamco mollit. Et pariatur aliqua velit sit nisi voluptate commodo sit officia labore eu nulla consectetur.\nLaborum dolore sint nulla voluptate in consequat.\nConsectetur anim laboris in ullamco ex sint laborum laborum non est ullamco occaecat mollit.\nEiusmod laboris est minim culpa aliquip deserunt nostrud nostrud ut. Excepteur mollit proident nisi duis pariatur. Est sint commodo velit enim dolor sit.\nSunt commodo anim dolor et. Deserunt consectetur incididunt do occaecat magna et laborum veniam exercitation minim."
            sentiment_analysis = te.get_emotion(text)
            sentiment = json.dumps(sentiment_analysis)
        
        return text, sentiment


    def generate_line(self, *args, **kwargs):
        global graph
        global line_length
        try:
            style = kwargs["style"]
            first_line = kwargs["first_line"]
            model_type = kwargs["model_type"]

        except:
            first_line = ""

        try:
            if style == "Shakespeare":

                if model_type == "gpt2":         
                    load_model("gpt2_shakespeare")
                    start = time.time()
                    with graph.as_default():
                        text = gpt2.generate(sess, run_name='gpt2_shakespeare', prefix = first_line, length = line_length, return_as_list=True)[0]
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    print("generating time:",time.time()-start,"s")

                if model_type == "gpt-neo":
                    try:

                        from aitextgen import aitextgen

                        ai = aitextgen(model_folder="checkpoint/neo_whitman/", to_gpu=False)
                        text = ai.generate(n=1,
                            batch_size=5,
                            prompt=first_line,
                            max_length=200,
                            temperature=0.7,
                            top_p=0.9)
                        # happy_gen_loaded = HappyGeneration(load_path="checkpoint/neo_shakespeare/")
                        # args = GENSettings(no_repeat_ngram_size=2, num_beams=5, max_length=line_length)
                        # result = happy_gen_loaded.generate_text(first_line, args = args)
                        # text = first_line + " " + result.text
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    
                    except Exception as e:
                        print(e)

            elif style == "Cummings":

                if model_type == "gpt2":
                    load_model("gpt2_cummings")
                    start = time.time()
                    with graph.as_default():
                        text = gpt2.generate(sess, run_name='gpt2_cummings', prefix = first_line, length = line_length, return_as_list=True)[0]
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    print("generating time:",time.time()-start,"s")

                if model_type == "gpt-neo":
                    try:
                        from aitextgen import aitextgen

                        ai = aitextgen(model_folder="checkpoint/neo_cummings/", to_gpu=False)
                        text = ai.generate(n=1,
                            batch_size=5,
                            prompt=first_line,
                            max_length=200,
                            temperature=0.7,
                            top_p=0.9)
                    # happy_gen_loaded = HappyGeneration(load_path="checkpoint/neo_cummings/")
                    # args = GENSettings(no_repeat_ngram_size=2, num_beams=5, max_length=line_length)
                    # result = happy_gen_loaded.generate_text(first_line, args = args)
                    # text = result.text
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    except Exception as e:
                        print(e)

            elif style == "Whitman":

                if model_type == "gpt2":
                    load_model("whitman_gpt2_500_steps")
                    start = time.time()
                    with graph.as_default():
                        text = gpt2.generate(sess, run_name='whitman_gpt2_500_steps', prefix = first_line, length = line_length, return_as_list=True)[0]
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    print("generating time:",time.time()-start,"s")

                if model_type == "gpt-neo":
                    try:
                        from aitextgen import aitextgen

                        ai = aitextgen(model_folder="checkpoint/neo_whitman/", to_gpu=False)
                        text = ai.generate(n=1,
                            batch_size=5,
                            prompt=first_line,
                            max_length=200,
                            temperature=0.7,
                            top_p=0.9)
                    # happy_gen_loaded = HappyGeneration(load_path="checkpoint/neo_whitman/")
                    # args = GENSettings(no_repeat_ngram_size=2, num_beams=5, max_length=line_length)
                    # result = happy_gen_loaded.generate_text(first_line, args = args)
                    # text = result.text
                        sentiment_analysis = te.get_emotion(text)
                        sentiment = json.dumps(sentiment_analysis)
                    except Exception as e:
                        print(e)
                
            else: raise Exception("Style not found")

        except Exception as e: # lorem ipsum request or models unvaible
            print(e)
            text = "Tempor eiusmod deserunt pariatur eu magna sit velit mollit cupidatat qui fugiat.\nLorem esse quis irure labore aliquip. Qui proident aliqua non voluptate deserunt id culpa velit. Pariatur duis minim esse est.\nEt commodo pariatur est exercitation duis. Id qui voluptate minim magna eiusmod.\nLaboris magna dolore sunt nisi fugiat proident irure magna ullamco et sint sit sint.\nIn cupidatat do commodo ex officia anim ad occaecat magna aliqua. Commodo labore aute ut ullamco mollit. Et pariatur aliqua velit sit nisi voluptate commodo sit officia labore eu nulla consectetur.\nLaborum dolore sint nulla voluptate in consequat.\nConsectetur anim laboris in ullamco ex sint laborum laborum non est ullamco occaecat mollit.\nEiusmod laboris est minim culpa aliquip deserunt nostrud nostrud ut. Excepteur mollit proident nisi duis pariatur. Est sint commodo velit enim dolor sit.\nSunt commodo anim dolor et. Deserunt consectetur incididunt do occaecat magna et laborum veniam exercitation minim."
            sentiment_analysis = te.get_emotion(text)
            sentiment = json.dumps(sentiment_analysis)    
        return text, sentiment


poem_generator = PoemGenerator()
