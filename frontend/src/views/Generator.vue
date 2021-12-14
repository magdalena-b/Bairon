<template>

    <div class="container">
        <div class="columns is-multiline is-mobile is-vcentered">

            <div class = "column is-6 is-half has-text-centered">

                <div class="poem">
                    <h2 class="is-size-3-tablet is-size-4-mobile">Select your favourite poet</h2>
                    <div class="buttons is-centered">
                        <button class="button is-rounded" v-for="p in avaible_poets" :key="p" @click="selectPoet(p)" v-bind:class="{'is-primary': p==poet}">
                            {{ p }}
                        </button>
                    </div>

                    <h2 class="is-size-3-tablet is-size-4-mobile">Choose a generating mode</h2>
                    <div class="buttons is-centered">
                        <button class="button is-rounded" @click="selectGenerator('full')" v-bind:class="{'is-primary': generator_type == 'full'}" data-tooltip="Tooltip Text">
                            Full
                        </button>

                        <button class="button is-rounded" @click="selectGenerator('collab')" v-bind:class="{'is-primary': generator_type == 'collab'}" data-tooltip="Tooltip Text">
                            Collab
                        </button>
                    </div>

                    <h2 class="is-size-3-tablet is-size-4-mobile mt-5">Type your first line</h2>
                    <div class="field is-grouped">
                        <div class="control is-expanded">
                            <input class="input is-rounded" type="text" v-model="first_line" placeholder="eg. life as it is" :maxlength="100" required/>
                        </div>
                        <template v-if="generator_type == 'collab'">
                            <div class="control">
                                <button id="generate_button" class="button is-rounded is-info" @click="fetch_poem_line(first_line)">generate</button>
                            </div>
                        </template>
                        <template v-if="generator_type == 'full'">
                            <div class="control">
                                <button id="generate_button" class="button is-rounded is-info" @click="fetch_poem(first_line)">generate</button>
                            </div>
                            <div class="control" v-if=" poet ==  'Shakespeare' ">
                                <button id="generate_style_transfer_button" class="button is-rounded is-info" @click="fetch_style_transfer_line(first_line)">translate to shakespearian</button>
                            </div>
                        </template>
                    </div>

                    <template v-if="generator_type == 'collab'">
                        <div id="poem_container" class="mt-5" v-bind:style="{'max-height':(( collab_lines != null) ? '100vh' : '0px')}">
                            <div id="poem" class="card" v-if="collab_lines != null" >
                                <div class="card-content">
                                    <div class="media-content">
                                        <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{first_line}}</h3>
                                    </div>
                                    <div v-if="collab_lines != null">
                                        <p class="is-size-6 has-text-left" v-for="line in collab_lines.split('\n')" :key="line">{{ line }}</p>
                                    </div>
                                <div class="control">

                                <div class="control is-expanded">
                                    <input class="input is-rounded" type="text" v-model="next_human_line" placeholder="eg. life as it is" :maxlength="100" required/>
                                </div>
                                <div class="control buttons mt-3 is-centered">
                                    <button v-if=" collab_lines != null" id="generate_button" class="button is-rounded is-info"  @click="fetch_poem_line(next_human_line)">continue generating</button>
                                    <button class="button is-info is-rounded" @click="clear_collab_lines_cache">clear</button>
                                </div>
                                </div>

                                </div>
                            </div>
                        </div>
                    </template>
                    <template v-if="generator_type == 'full'">
                        <div v-if=" translated_lines != null & poet == 'Shakespeare'">
                            <div class="button is_rounded is_info" @click="fetch_poem(translated_line)" v-for="translated_line in translated_lines" :key="translated_line">{{ translated_line }} </div>
                        </div>

                        <div id="poem_container" class="mt-5" v-bind:style="{'max-height':(( poem != '' || show_notification) ? '100vh' : '0px')}">
                            <div v-if="poem != ''" id="poem" class="card">
                                <div class="card-content">
                                    <div class="media-content">
                                        <!-- <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{first_line}}</h3> -->
                                    </div>
                                    <p class="is-size-6 has-text-left" v-for="line in poem.split('\n')" :key="line">{{ line }}</p>
                                    <button class="button is-info is-rounded mt-3" @click="save_poem">save</button>
                                </div>
                            </div>
                            <template v-if="show_notification==true">
                                <div class="notification is-warning is-light" @click="toggle_notification(false)">
                                    You can only generate 3 poems per hour. Try again later :)
                                </div>
                            </template>
                        </div>
                    </template>
                </div>

            </div>
            <div class="column is-1">
                <!-- placeholder -->
            </div>
            
            <div class="column is-5 is-half">
                <Gallery />
            </div>
        </div>
    </div>

    
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
            avaible_poets: ["Shakespeare", "Ginsberg", "Cummings", "Lorem Ipsum"],
            input_id: null,
            translated_lines: null,
            generator_type: "full",
            collab_lines: null,
            next_human_line: null,
            next_machine_line: null,
            show_notification: false,
        }
    },
    methods: {
        selectPoet(poet){
            this.poet = poet
        },
        toggle_notification(bool){
            console.log(bool)
            this.show_notification = bool
        },
        fetch_poem(line){
            this.poem = ""
            const generate_button = document.querySelector('#generate_button')

            generate_button.classList.add('is-loading')

            fetch(`${API_URL}/api/generate/`, {
                method: 'POST',
                mode: 'cors',
                cache: 'no-cache',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "style": this.poet,
                    "first_line": line,
                })
            })
                .then(res => {
                    if(res.ok){
                        return res.json()
                    }
                    else{
                        this.toggle_notification(true)
                        generate_button.classList.remove("is-loading")  
                        throw new Error("Requests limit exceeded")
                    }
                })
                .then(data => {
                    ({text: this.poem, input: this.input_id} = data)
                    generate_button.classList.remove("is-loading")
                })
                .catch(err => console.log(err.message))
        },
        fetch_poem_line(line){

            const generate_button = document.querySelector('#generate_button')
            generate_button.classList.add('is-loading')

            fetch(`${API_URL}/api/generate-line/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "style": this.poet,
                    "first_line": line,
                })
            })
                .then(res => res.json())
                .then(data => {
                    ({text: this.next_machine_line, input: this.input_id} = data)
                    generate_button.classList.remove("is-loading")
                    if (this.collab_lines != null) {
                        this.collab_lines = this.collab_lines + this.next_machine_line
                    }
                    else {
                        this.collab_lines = this.next_machine_line
                    }
                })
                .catch(err => console.log(err.message))
        },

        clear_collab_lines_cache(){
            fetch(`${API_URL}/api/generate-line/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .catch(err => console.log(err.message))
        },

        fetch_style_transfer_line(first_line){
            fetch(`${API_URL}/api/generate-style-transfer/`, {
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
                .then(data => {
                    ({translated_lines: this.translated_lines} = data)
                })
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
                .then(() => {
                    this.poem = ""
                })
                .catch(err => console.log(err.message))
        },
        selectGenerator(g) {
            this.generator_type = g
        }
    },
}
</script>

<style scoped>
    .columns {
        min-height: 90vh;
    }

    #poem_container {
        overflow: hidden;
        transition: max-height 1s ease-out;
    }
</style>