<template>    
    <h2> {{this.words}} - {{this.counts}} </h2>
</template>

<script>
const {API_URL} = require('../settings.json')

    export default {
        name: 'Statistics',
        data() {
            return {
                words: [],
                counts: []
            }
        },
        methods: {
            fetch_text(){
                this.words = []
                this.counts = []

                fetch(`${API_URL}/api/statistics/`)
                    .then(res => res.json())
                    .then(data => {
                        ({words: this.words, counts: this.counts} = data)
                    })
                    .catch(err => console.log(err.message))
            },
        },
        mounted() {
            this.fetch_text()
        }
}
</script>