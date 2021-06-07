<template>
    <div id="wrapper">
        <div class="container has-text-centered px-4 py-6" v-bind:class="{'has-background-light': is_correct=='none', 'has-background-danger-light': is_correct=='no', 'has-background-success-light': is_correct=='yes'}">
            <h2 class="is-size-3-desktop is-size-4 is-italic">
                "{{text}}"
            </h2>
            <p class="is-size-4-desktop is-size-5 mt-6 mb-4">Who do you think wrote this poem?</p>
            <div class="buttons is-centered">
                <button class="button is-rounded is-medium is-primary" @click="save_vote('Human')">Human</button>
                <p class="is-size-4-desktop is-size-5 mx-2">or</p>
                <button class="button is-rounded is-medium is-info" @click="save_vote('Machine')">Machine</button>
            </div>
        </div>
    </div>
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: 'TuringTest',
    components: { },
    data() {
        return {
            poem_id: -1,
            text: "",
            is_correct: 'none',
        }
    },
    methods: {
        fetch_text(){
            this.text = ""

            fetch(`${API_URL}/api/get/tt-fragment/`)
                .then(res => res.json())
                .then(data => {
                    ({text: this.text, poem_id: this.poem_id} = data)
                })
                .catch(err => console.log(err.message))
        },
        save_vote(vote) {
            fetch(`${API_URL}/api/add/turing-test-vote/${this.poem_id}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "poem_id": this.poem_id,
                    "fragment": this.text,
                    "vote": vote
                })
            })
                .then(res => res.json())
                .then(data => {
                    ({is_correct: this.is_correct} = data)
                    this.is_correct = is_correct ? "yes" : "no"
                    setTimeout(() => {
                        this.is_correct = "none"
                        this.fetch_text()
                    }, 1000)
                })
                .catch(err => console.log(err.message))
        }
    },
    mounted() {
        this.fetch_text()
    }
}
</script>

<style scoped>
    #wrapper {
        min-height: 90vh;
        display: flex;
        align-items: center;
    }
    .container {
        border-radius: 50px;
    }
</style>