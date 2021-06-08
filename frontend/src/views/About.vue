<template>
    <div class="container mt-4">
        <h2 class="title">About this project</h2>
        <p class="is-size-5-desktop is-size-6-tablet">
            An application for generating poetry using finetuned pretrained language models. For now we use GPT-2 model, but we plan to add other language models
            and use Style Transfer methods.
            You can generate text from an input line (or only a word, but the results are better if you write a full sentence).
            Choose the poet whose style you want to emulate. If you like the generated text, save it. Check out other generated poems and rate them.
            You can also take a Poetry Turing Test - it will help us evaluate our generator. 
        </p>
        <h3 class="is-size-4 mt-4">
            Technologies:
        </h3>
        <div class="columns has-text-centered is-multiline">
            <div class="column is-4-desktop is-8-tablet">
                <p class="is-size-6">backend</p>
                <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" alt="">
            </div>
            <div class="column is-4-desktop is-8-tablet">
                <p class="is-size-6">frontend</p>
                <div class="columns is-vcentered is-centered">
                    <div class="column is-half">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" alt="">
                    </div>
                    <div class="column is-one-third">
                        <img src="https://seeklogo.com/images/B/bulma-logo-45B5145BF4-seeklogo.com.png" alt="">
                    </div>
                </div>
                
            </div>
            <div class="column is-4-desktop is-8-tablet">
                <p class="is-size-6">NLP</p>
                <img src="https://venturebeat.com/wp-content/uploads/2019/04/d2fcb133-1ed1-4a92-bd7f-8be7cfc96cec.png?w=1200&strip=all" alt="">
            </div>
        </div>
        <h3 class="is-size-4 mt-4">
            Tests results:
        </h3>
        <div class="columns is-centered mt-4">
            <div class="column is-6-desktop is-8-tablet has-text-centered">
                <div class="message is-dark">
                    <div class="message-header">
                        <p>Average rating</p>
                    </div>
                    <div class="header-body py-4 px-4">
                        <p>{{score}}</p>
                    </div>
                    <div class="message-header">
                        <p>Turing Test votes</p>
                    </div>
                    <div class="header-body">
                        <TTChart />
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
const {API_URL} = require('../settings.json')
import TTChart from '@/components/TTChart.vue'


export default ({
    name: "About",
    components: {
        TTChart,
    },
    data() {
        return {
            score: 0,
            TT_machine: 0,
            TT_human: 0,
            TT_TH: 0,
            TT_FH: 0,
            TT_TM: 0,
            TT_TM: 0,
        }
    },
    methods: {
        get_rating(callback = () => "dupa"){
            fetch(`${API_URL}/api/rating/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        "TT-human": this.TT_human,
                        "TT-machine": this.TT_machine,
                        "rate-average": this.score,
                        "TT-TH": this.TT_TH,
                        "TT-FH": this.TT_FH,
                        "TT-TM": this.TT_TM,
                        "TT-FM": this.TT_FM,
                    } = data)
                    callback()
                })
                .catch(err => console.log(err.message))
        },
    },
    mounted() {
        this.get_rating(this.get_chart)
    }
})
</script>

<style scoped>
    img {
        max-width: 300px;
        max-height: 200px;
    }
</style>
