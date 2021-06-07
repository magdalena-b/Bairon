<template>
    <div class="container">
        <div class="columns is-vcentered is-centered is-multiline  has-text-centered">
            <div class="column is-6-desktop is-10-tablet">
                <div class="card">
                    <div class="card-content">
                        <div class="media-content">
                            <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{style}}</h3>
                            <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{first_line}}</h3>
                        </div>
                        <div v-for="line in text.split('\n')" :key="line">
                            <div v-if="line.length > 0">
                                <p class="is-size-6 has-text-left">{{line}}</p>
                            </div>
                            <div v-else><br/></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-2 is-desktop">
                <!-- placeholder -->
            </div>
            <div class="column is-4-desktop is-6-tablet">
                <div class="message has-text-centered is-primary" id="rating">
                    <p class="message-header is-size-6">How much do you like this poem?</p>
                    <div class="stars icon-text py-2">
                        <span class="star icon is-size-3 is-medium" v-for="n in [1,2,3,4,5,6,7,8,9,10]" :key="n" @click="rate(n)">
                            <i class="fas fa-star"></i>
                        </span>
                    </div>
                    <p class="is-size-6">Average rating: {{Math.round(score*10)/10}}</p>
                    <p class="message-header is-size-6">views: {{views}}</p>
                </div>
            </div>
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

<style scoped>
    .star{
        color: gold !important;
    }
    .star:hover{
        transform: scale(1.5,1.5);
        cursor: pointer;
    }
    .columns {
        min-height: 90vh;
    }
</style>