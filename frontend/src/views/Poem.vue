<template>
    <h3> Author: {{author}}</h3>
    <div id="poem">
        <strong><p>{{first_line}}</p></strong>
        <p v-for="line in text.split('\n')" :key="line">{{ line }}</p>
    </div>
    <p>views: {{views}}</p>
    <div id="rating">
        <p>Average rating: {{score}}</p>
        <p>How much do you like this poem?</p>
        <div id="stars">
            <span id="star" v-for="n in [1,2,3,4,5,6,7,8,9,10]" :key="n" @click="rate(n)"></span>
        </div>
    </div>
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: 'Poem',
    components: {
    },
    props: ["id"],
    data() {
        return {
            style: "",
            author: "",
            first_line: "",
            text: "",
            views: 0,
            score: 0,
            TT_machine: 0,
            TT_human: 0,
        }
    },
    mounted() {
        fetch(`${API_URL}/api/poems/${this.id}/`)
            .then(res => res.json())
            .then(data => {
                ({author: this.author, first_line: this.first_line, style: this.style, text: this.text, views: this.views} = data)
            })
            .catch(err => console.log(err.message))
        this.get_rating()
    },
    methods: {
        get_rating(){
            fetch(`${API_URL}/api/rating/${this.id}/`)
                .then(res => res.json())
                .then(data => {
                    ({"TT-human": this.TT_human, "TT-machine": this.TT_machine, "rate-average": this.score} = data)
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
                })
            })
                .then(res => {this.get_rating()})
                .catch(err => console.log(err.message))
            this.get_rating()
        }
    }
}
</script>

<style>
    #poem {
        background-color: #eee;
        padding: 50px;
    }
    #star {
        width: 20px;
        height: 20px;
        border-radius: 10px;
        background-color: gold;
        margin: 5px
    }
    #star:hover {
        background-color: rgb(214, 182, 0);
    }
    #stars {
        display: flex;
        justify-content: center;
    }
</style>