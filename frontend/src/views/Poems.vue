<template>
    <div class="container has-text-centered mt-4">
        <h1 class="is-size-2">
            discover the most popular poems
        </h1>
        <!-- <h2 class="is-size-5">Filters</h2> -->
        <div class="buttons is-centered mt-3">
            <button class="button is-rounded" v-for="p in avaible_styles" :key="p" @click="selectPoet(p)" v-bind:class="{'is-primary': p==style}"> {{ p }} </button>
            <button class="button is-rounded is-info" @click="fetch_poems">filter</button>
        </div>
        <div class="columns scrollable mt-4">
            <div class="column is-4-desktop is-6-tablet" v-for="{id, input, text, style, generator_type} in poems" :key="id">
                <router-link  :to="'/poem/'+id">
                    <div id="poem_container" class="mt-5">
                        <div id="poem" class="card">
                            <div class="card-content">
                                <div class="media-content">
                                    <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{style}}</h3>
                                    <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{input}}</h3>
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

                                <p class="is-size-6 has-text-centered" v-if="text.split('\n').length > 20"> ... </p>
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: 'Poems',
    components: { },
    data() {
        return {
            poems: [],
            avaible_styles: ["Shakespeare", "Ginsberg", "Cummings", "Lorem Ipsum"],
            style: "",
            // TODO filtering by sentiments
            avaible_sentiments: ["normal"],
            sentiment: "",
        }
    },
    methods: {
        fetch_poems(){
            let endpoint = `${API_URL}/api/poems/`
            if(this.style){
                endpoint += "style=" + this.style + "/"
            }
            fetch(endpoint)
                .then(res => res.json())
                .then(data => ({all: this.poems}=data))
                .catch(err => console.log(err.message))
        },
        selectPoet(poet){
            if(this.style == poet){
                this.style = ""
            }
            else{
                this.style = poet
            }
        }
    },
    mounted() {
        this.fetch_poems()
    }
}
</script>

<style scoped>
    .scrollable, .scrollable > * {
        overflow-y: auto;
        transform: rotateX(180deg);
    }
</style>