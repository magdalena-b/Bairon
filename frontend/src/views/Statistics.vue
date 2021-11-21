<template>
  <div class="container mt-5 text-center">
    <WordCountCharts />
  </div>
</template>


<script>
import WordCountCharts from '@/components/WordCountCharts.vue'
const {API_URL} = require('../settings.json')

    export default {
        name: 'Statistics',
        components: { 
            WordCountCharts
        },
        data() {
            return {
                words: null,
                counts: null
            }
        },
        methods: {
            fetch_text(){
                this.words = null
                this.counts = null

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