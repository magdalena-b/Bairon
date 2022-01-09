<template>
    <div class="container">
        <div class="columns is-vcentered is-centered is-multiline  has-text-centered" id="wrapper">
            <div class="column is-6-desktop is-10-tablet">
                <div class="card">
                    <div class="card-content">
                        <div class="media-content">
                            <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{style}}</h3>
                            <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{first_line}}</h3>
                        </div>
                        <div v-if='generator_type == "collab" '>
                                    <div v-bind:class="{'is-hidden': counter = 0}">
                                    </div>
                                        <div v-for="line in text.split('|').slice(0, 20)" :key="line">

                                            <div v-if="line.length > 0">
                                                <div v-if="counter % 2 == 0">    
                                                    <p class="is-size-6 has-text-left">{{line}} </p>
                                                </div>
                                                <div v-else>
                                                    <p class="is-size-6 has-text-left"> <b> {{line}} </b> </p>
                                                </div>
                                            </div>
                                            <div v-else><br/></div>
                                            <div v-bind:class="{'is-hidden': counter += 1}">
                                            </div>
                                    </div>
                                </div>
                        <div v-else>
                            <div v-for="line in text.split('\n').slice(0, 20)" :key="line">
                                <div v-if="line.length > 0">
                                    <p class="is-size-6 has-text-left">{{line}}</p>
                                </div>
                                <div v-else><br/></div>
                            </div>
                        </div>
                        
                    </div>
                </div>
                <div class="mt-3" id="buttons">
                    <button class="button is-rounded is-info is-small mb-1" @click="download_PDF">Download PDF</button>
                    <a href="https://twitter.com/intent/tweet" class="twitter-share-button" data-size="large" data-text="#poem #poetrygenerator" :data-url="fullUrl" data-dnt="true" data-show-count="false">Tweet</a>
                </div>
            </div>
            <div class="column is-2 is-desktop">
                <!-- placeholder -->
            </div>
            <div class="column is-4-desktop is-6-tablet">
                <div class="message has-text-centered is-primary" id="rating">
                    <p class="message-header is-size-6">How much do you like this poem?</p>
                    <p class="is-size-6"></p>
                    <div class="stars icon-text py-2">
                        <span class="star icon is-size-4 is-medium" v-for="n in [1,2,3,4,5,6,7,8,9,10]" :key="n" @click="rate(n)">
                            <i class="fas fa-star"></i>
                        </span>
                    </div>

                    <p class="is-size-7">Average rating: {{Math.round(score*10)/10}}</p>

                    <p class="message-header is-size-6">How good is the grammar?</p>
                    <div class="stars icon-text py-2">
                        <span class="star icon is-size-4 is-medium" v-for="n in [1,2,3,4,5,6,7,8,9,10]" :key="n" @click="rate_grammar(n)">
                            <i class="fas fa-star"></i>
                        </span>
                    </div>

                    <p class="is-size-7">Average rating: {{Math.round(grammar_score*10)/10}}</p>
                    
                    <p class="message-header is-size-6">How much is it similar to the poet's style?</p>
                    <div class="stars icon-text py-2">
                        <span class="star icon is-size-4 is-medium" v-for="n in [1,2,3,4,5,6,7,8,9,10]" :key="n" @click="rate_style(n)">
                            <i class="fas fa-star"></i>
                        </span>
                    </div>

                    <p class="is-size-7">Average rating: {{Math.round(style_score*10)/10}}</p>
                    <p class="message-header is-size-6">views: {{views}}</p>
                </div>

                <div v-if='style_transfer == 1 '>
                    <p class="message-header is-size-6 is-primary"> Style Transfer </p>
                    <h1> <b> Translations </b> </h1>
                    <div v-for="translated_line in translated_lines" :key="translated_line">
                        {{translated_line}}
                    </div>
                    <h1> <b> BLEU score </b> </h1>
                    <div> {{bleu_score}} </div>
                    <div class="stars icon-text py-2">
                        <span class="star icon is-size-3 is-medium" v-for="n in [1,2,3,4,5,6,7,8,9,10]" :key="n" @click="rate_style_transfer(n)">
                            <i class="fas fa-star"></i>
                        </span>
                    </div>

                    <p class="is-size-6">Average rating: {{Math.round(style_transfer_score*10)/10}}</p>
                </div>
                <div align="center">
                    <h3 class=" is-size-5 has-text-centered has-text-weight-bold" >Emotion analysis of your poem!</h3>
                    <table class="table is-fullwidth is-striped  is-narrow">
                        <thead>
                            <th style="text-align: center"><p class="is-size-6">Feeling</p></th>
                            <th style="text-align: center"><p class="is-size-6">Value (in %)</p></th>
                        </thead>
                        <tbody>
                            <tr v-for="(item, key, index) in json_sentiment" :key="index">
                                <td><p class="is-size-6 has-text-centered">{{key}}</p></td>
                                <td><p class="is-size-6 has-text-centered">{{item}}</p></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div align="center" class="mt-3 has-text-centered">
                    <h3 class="button is-rounded is-light is-inactive is-size-6 has-text-centered has-text-weight-bold dropdown-trigger" data-tooltip="Also known as emotion AI, emotion analysis is a use of natural language processing, text analysis, 
computational linguistics, and biometrics to systematically identify, extract, quantify, 
and study affective states and subjective information. In our analysis we divide it into five feelings: 
happiness, anger, surprise, sadness and fear.">What is emotion analysis?</h3>
                    <!-- <p class="is-size-6 has-text-justified dropdown-menu"> Also known as emotion AI, emotion analysis is a use of natural language processing, text analysis, 
                        computational linguistics, and biometrics to systematically identify, extract, quantify, 
                        and study affective states and subjective information. In our analysis we divide it into five feelings: 
                        happiness, anger, surprise, sadness and fear. </p> -->
                </div>
                
            </div>

        </div>
    </div>
</template>

<script>
import jsPDF from 'jspdf' 
const {API_URL} = require('../settings.json')
export default {
    name: 'Poem',
    components: {
     //   SentimentChart
      },
    props: ["id"],
    data() {
        return {
            style: "",
            author: "",
            first_line: "",
            text: "",
            sentiment: "",
            views: 0,
            score: 0,
            grammar_score: 0,
            style_score: 0,
            style_transfer_score: 0,
            TT_machine: 0,
            TT_human: 0,
            generator_type: "",
            style_transfer: 0,
            translations: "",
            bleu_score: 0,
            translated_lines: "",
            json_sentiment: {},
            TT_machine: 0,
            TT_human: 0,
            keys: [],
            values: [],
            fullUrl: "" + location.origin + this.$route.fullPath,
        }
    },
    mounted() {
        let twitterScript = document.createElement('script')
        twitterScript.setAttribute('async', '')
        twitterScript.setAttribute('src', 'http://platform.twitter.com/widgets.js')
        twitterScript.setAttribute('charset', 'utf-8')
        document.head.appendChild(twitterScript)

        fetch(`${API_URL}/api/poems/${this.id}/`)
            .then(res => res.json())
            .then(data => {
                ({author: this.author, first_line: this.first_line, style: this.style, text: this.text, sentiment: this.sentiment, views: this.views, keys: this.keys, values: this.values, generator_type: this.generator_type, style_transfer: this.style_transfer, translations: this.translations, bleu_score: this.bleu_score, translated_lines: this.translated_lines} = data)
                ({author: this.author, first_line: this.first_line, style: this.style, text: this.text, sentiment: this.sentiment, views: this.views, keys: this.keys, values: this.values} = data)
            })
            .then()
            .catch(err => console.log(err.message))
        this.get_rating()
        this.fetch_text()
        this.get_json_sentiment()

    },
    methods: {
        get_rating(){
            fetch(`${API_URL}/api/rating/${this.id}/`)
                .then(res => res.json())
                .then(data => {
                    ({"TT-human": this.TT_human, "TT-machine": this.TT_machine, "rate-average": this.score, "grammar-rate-average": this.grammar_score, "style-rate-average": this.style_score, "style-transfer-rate-average": this.style_transfer_score} = data)
                })
                .catch(err => console.log(err.message))
        },
        get_json_sentiment(){
            fetch(`${API_URL}/api/sentiment/${this.id}/`)
                .then(res => res.json())
                .then(data => {
                    ({"json_sentiment": this.json_sentiment} = data)
                })
                .catch(err => console.log(err.message))
        },
        rate(n) {
            fetch(`${API_URL}/api/add/rate/${this.id}/`,{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "poem": this.id,
                    "rate": n,
                    "category": "overall",
                })
            })
                .then(res => {this.get_rating()})
                .catch(err => console.log(err.message))
            this.get_rating()
        },
        rate_grammar(n) {
            fetch(`${API_URL}/api/add/rate/${this.id}/`,{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "poem": this.id,
                    "rate": n,
                    "category": "grammar",
                })
            })
                .then(res => {this.get_rating()})
                .catch(err => console.log(err.message))
            this.get_rating()
        },
        rate_style(n) {
            fetch(`${API_URL}/api/add/rate/${this.id}/`,{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "poem": this.id,
                    "rate": n,
                    "category": "style",
                })
            })
                .then(res => {this.get_rating()})
                .catch(err => console.log(err.message))
            this.get_rating()
        },
        rate_style_transfer(n) {
            fetch(`${API_URL}/api/add/rate/${this.id}/`,{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "poem": this.id,
                    "rate": n,
                    "category": "style_transfer",
                })
            })
                .then(res => {this.get_rating()})
                .catch(err => console.log(err.message))
            this.get_rating()
        },
        
        fetch_text(){
            this.keys = null
            this.values = null
            fetch(`${API_URL}/api/poems/${this.id}`)
                .then(res => res.json())
                .then(data => {
                    ({keys: this.keys, values: this.values})
                })
                .catch(err => console.log(err.message))
        },
        
        download_PDF(){
            var today_date = new Date()
            var date = today_date.getFullYear()+'-'+(today_date.getMonth()+1) + '-' + (today_date.getDate()) + ' ' + (today_date.getHours()) + '.' +(today_date.getMinutes()<10?'0':'') + (today_date.getMinutes());
            let pdfName = "Generated " + this.style + " poem, input word -  " + this.first_line + ", Generated date - " + date;
            var doc = new jsPDF('p', 'mm', 'A4');
            doc.setFillColor(192, 235, 244);
            doc.rect(0, 0, 10000, 10000, "F");
            doc.setFillColor(255, 255, 255);
            doc.rect(20, 20, 170, 260, "F");
            doc.setFont(undefined, 'bold')
            doc.setFontSize(30)
            doc.text("BAIron", 85, 12).setFont(undefined, 'normal')
            doc.setFontSize(24)
            doc.text(this.style +" - " + this.first_line, 122-((this.style.length+this.first_line.length)*4), 35)
            doc.setFontSize(10)
            doc.text(this.text,  60, 60)
            doc.text(date, 5,5)
            doc.save(pdfName + '.pdf');
        },
        
    }
}
</script>

<style scoped>
    .star{
        color: gold !important;
    }
    .star:hover{
        transform: scale(1.5,1.5);
        cursor: pointer;
    }
    #wrapper {
        min-height: 90vh;
    }
    /* table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }
    td, th {
        border: 1px solid #acd4ce;
        text-align: left;
        padding: 8px;
    } */
    
    
    /* tr:nth-child(even) {
    background-color: #7cb3f7;
    color: white
    }
    tr:nth-child(odd) {
    background-color: #edf5ff;
    } */

    .dropdown {
        width: 100%;
    }

    #buttons {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
