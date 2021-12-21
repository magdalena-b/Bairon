<template>

    <div class="container">
        <div class="columns is-multiline is-centered is-vcentered">

            <div class = "column is-6-desktop is-12-mobile has-text-centered">

                <div class="poem container is-fluid mt-6">
                    <h2 class="is-size-3-tablet is-size-4-mobile">Select your favourite poet</h2>
                    <div class="buttons is-centered">
                        <button class="button is-rounded" v-for="p in avaible_poets" :key="p" @click="selectPoet(p)" v-bind:class="{'is-primary': p==poet}">
                            {{ p }}
                        </button>
                    </div>

                    <h2 class="is-size-3-tablet is-size-4-mobile">Choose a generating mode</h2>
                    <div class="buttons is-centered">
                        <button class="button is-rounded has-tooltip-arrow" @click="selectGenerator('full')" v-bind:class="{'is-primary': generator_type == 'full'}" data-tooltip="generate whole poem">
                            Full
                        </button>

                        <button class="button is-rounded has-tooltip-arrow" @click="selectGenerator('collab')" v-bind:class="{'is-primary': generator_type == 'collab'}" data-tooltip="generate poem line by line alternately with the generator">
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
                                <button id="generate_style_transfer_button" class="button is-rounded is-info has-tooltip-arrow" @click="fetch_style_transfer_line(first_line)" data-tooltip="translate your line to shaespearian style. then you can use it as input to new poem">translate to shakespearian</button>
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
                                    <button class="button is-info is-rounded" @click="save_collab_poem">save</button>
                                </div>
                                </div>

                                </div>
                            </div>
                        </div>
                    </template>
                    <template v-if="generator_type == 'full'">
                        <div v-if=" translated_lines != null & poet == 'Shakespeare'">
                            <div class="button is_rounded is_info" @click="fetch_poem(translated_line, true)" v-for="translated_line in translated_lines" :key="translated_line">{{ translated_line }} </div>
                        </div>

                        <div v-if=" bleu_score != null & poet == 'Shakespeare'">
                            <h3> BLEU score: {{bleu_score}} </h3>
                        </div>

                        <div id="poem_container" class="mt-5" v-bind:style="{'max-height':(( poem != '' || show_notification) ? '100vh' : '0px')}">
                            <div v-if="poem != ''" id="poem" class="card">
                                <div class="card-content">
                                    <div class="media-content">
                                        <h3 class="is-size-5 is-capitalized has-text-weight-bold">{{first_line}}</h3>
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
            <div class="column is-1-dektop">
                <!-- placeholder -->
            </div>
            
            <div class="column is-5-desktop is-12-mobile">
                <div id="wrapper">
                    <Gallery />
                </div>
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
            formatted_collab_lines: null,
            show_notification: false,
            bleu_score: null,
            used_style_transfer: 0,
            saved_poem_id: null,
            translations: null
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
        fetch_poem(line, first_line_from_style_transfer){

            if (first_line_from_style_transfer){
                this.used_style_transfer = 1
            }

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

        // fetch_poem(line){
        //     this.poem = ""
        //     const generate_button = document.querySelector('#generate_button')

        //     generate_button.classList.add('is-loading')

        //     fetch(`${API_URL}/api/generate/`, {
        //         method: 'POST',
        //         mode: 'cors',
        //         cache: 'no-cache',
        //         headers: {
        //             'Content-Type': 'application/json',
        //         },
        //         body: JSON.stringify({
        //             "style": this.poet,
        //             "first_line": line,
        //         })
        //     })
        //         .then(res => {
        //             if(res.ok){
        //                 return res.json()
        //             }
        //             else{
        //                 this.toggle_notification(true)
        //                 generate_button.classList.remove("is-loading")  
        //                 throw new Error("Requests limit exceeded")
        //             }
        //         })
        //         .then(data => {
        //             ({text: this.poem, input: this.input_id} = data)
        //             generate_button.classList.remove("is-loading")
        //         })
        //         .catch(err => console.log(err.message))
        // },
        fetch_poem_line(line){

            const generate_button = document.querySelector('#generate_button')
            generate_button.classList.add('is-loading')
            this.input = null


            if (this.next_machine_line === null){
                this.input = line
                // this.formatted_collab_lines = "|" + line + "|"
                this.formatted_collab_lines = line + "|"
            }
            else {
                this.input = this.next_machine_line + line
                // this.formatted_collab_lines += "|" + line + "|"
                this.formatted_collab_lines += line + "|"
            }

            if (this.collab_lines == null) {
                this.collab_lines = line
            } else {
                this.collab_lines +=  " " + line
            }

            fetch(`${API_URL}/api/generate-line/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "style": this.poet,
                    "first_line": this.collab_lines,
                })
            })
                .then(res => res.json())
                .then(data => {
                    ({text: this.next_machine_line, input: this.input_id} = data)
                    generate_button.classList.remove("is-loading")
                    if (this.collab_lines != null) {
                        this.formatted_collab_lines += this.next_machine_line.substring(this.collab_lines.length + line.length, this.next_machine_line.length) + "|"
                        this.collab_lines = this.next_machine_line
                    }
                    else {
                        this.formatted_collab_lines += this.next_machine_line.substring(line.length, this.next_machine_line.length) + "|"
                        this.collab_lines = this.next_machine_line
                        // this.formatted_collab_lines = this.collab_lines + "|"
                    }
                })
                .catch(err => console.log(err.message))
        },

        clear_collab_lines_cache(){
            this.collab_lines = null
            this.formatted_collab_lines = null
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
                    ({translated_lines: this.translated_lines, bleu_score: this.bleu_score} = data)
                })
                .catch(err => console.log(err.message))
        },

        save_poem() {

            if (this.translated_lines != null) {
                this.translations = this.translated_lines.join("|")
                this.translated_lines = this.translated_lines.join("|")
            }
            else {
                this.translations = ""
            }

            this.translated_lines = null

            if (this.generator_type == 'collab') {
                this.generator_type = "collab"
            }
            else {
                this.generator_type = "full"
            }

            if (this.bleu_score != null) {
                this.bleu_score = this.bleu_score.toString()
            }
            

            fetch(`${API_URL}/api/save/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "input": this.input_id,
                    "text": this.poem,
                    "style_transfer": this.used_style_transfer.toString(),
                    "translations": this.translations,
                    "bleu_score": this.bleu_score,
                    "generator_type": this.generator_type
                })
            })
                .then(() => {
                    this.poem = "",
                    this.used_style_transfer = 0            
                })
                .catch(err => console.log(err.message))
        },
        save_collab_poem() {
            fetch(`${API_URL}/api/save/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "input": this.input_id,
                    "text": this.formatted_collab_lines,
                    "generator_type": this.generator_type,
                    "style_transfer": 0,
                    "translations": "",
                    "bleu_score": 0,
                    "generator_type": this.generator_type
                })
            })
                .then(() => {
                    this.poem = "",
                    this.used_style_transfer = 0
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
    
    #wrapper {
        display: block;
    }

    #wrapper > * {
        max-width: 50vw;
    }
</style>