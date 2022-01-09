<template>
  <div class="container mt-5 text-center">
    <DetailedTTChart />
  </div>
</template>


<script>
import DetailedTTChart from '@/components/DetailedTTChart.vue'
const {API_URL} = require('../settings.json')

    export default {
        name: 'PoetryTuringTestStatistics',
        components: { 
            DetailedTTChart
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

                fetch(`${API_URL}/api/poetry-turing-test-statistics/`)
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