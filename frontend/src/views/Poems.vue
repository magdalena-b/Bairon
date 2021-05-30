<template>
    <main>
        <h2>Filters</h2>
        <button v-for="p in avaible_styles" :key="p" @click="selectPoet(p)" v-bind:class="{highlight: p==style}"> {{ p }} </button>
        <button @click="fetch_poems">filter</button>
        <ul>
            <router-link v-for="{id, input, text, style} in poems" :key="id" :to="'/poem/'+id">
                <li>
                    <h3>{{style}}</h3>
                    <strong><p>{{input}}</p></strong>
                    <p v-for="line in text.split('\n')" :key="line">{{ line }}</p>
                </li>
            </router-link>
        </ul>
    </main>
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: 'Poems',
    components: { },
    data() {
        return {
            poems: [],
            avaible_styles: ["Shakespeare", "Ginsberg", "cummings", "Lorem Ipsum"],
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
</style>