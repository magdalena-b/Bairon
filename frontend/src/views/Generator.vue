<template>
    <main>
        <div class="poem">
            <h2>Select your favourite poet</h2>
            <button v-for="p in avaible_poets" :key="p" @click="selectPoet(p)" v-bind:class="{highlight: p==poet}">
                {{ p }}
            </button>
            <h2 >Type your first line</h2>
            <input type="text" v-model="first_line"/>
            <button @click="fetch_poem">generate</button>
            <div id="poem" v-if="poem != ''">
                <p v-for="line in poem.split('\n')" :key="line">{{ line }}</p>
                <button @click="save_poem">save</button>
            </div>
        </div>
        <Gallery v-model:current_author="poet"/>
    </main>
</template>

<script>
import Gallery from '@/components/Gallery.vue'
const {API_URL} = require('../settings.json')

export default {
    name: 'Generator',
    components: { Gallery },
    data() {
        return {
            first_line: "",
            poet: "Shakespeare",
            poem: "",
            avaible_poets: ["Shakespeare", "Ginsberg", "Lorem Ipsum"],
            input_id: null,
        }
    },
    methods: {
        selectPoet(poet){
            this.poet = poet
        },
        fetch_poem(){
            this.poem = ""
            fetch(`${API_URL}/api/generate/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "style": this.poet,
                    "first_line": this.first_line,
                })
            })
                .then(res => res.json())
                .then(data => ({text: this.poem, input: this.input_id} = data))
                .catch(err => console.log(err.message))
        },
        save_poem() {
            fetch(`${API_URL}/api/save/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "input": this.input_id,
                    "text": this.poem
                })
            })
                .catch(err => console.log(err.message))
        }
    }
}
</script>

<style scoped>
    main {
        /* TODO fix that shit */
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: baseline;
    }

    .poem {
        width: 40vw;
        height: 100%;
        margin: auto;
        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-content: center;
    }

    .highlight {
        background-color: lightseagreen;
    }
</style>