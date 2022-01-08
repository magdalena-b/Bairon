<template>
    <div class="container mt-5 text-center">
        <AvgSentimentCharts />
    </div> 
</template>

<script>
import AvgSentimentCharts from '@/components/AvgSentimentCharts.vue'
const {API_URL} = require('../settings.json')
    export default {
        name: 'SentimentAnalysis',
        components: {
            AvgSentimentCharts
        },
        data() {
            return {
                keys: null,
                values: null
            }
        },
        methods:{
            fetch_text(){
                this.keys = null
                this.values = null
                fetch(`${API_URL}/api/sentiment-analysis`)
                    .then(res => res.json())
                    .then(data => {
                        ({keys: this.keys, values: this.values} = data)
                    })
                    .catch(err => console.log(err.message))
            },
        },
        mounted() {
            this.fetch_text()
        }
    }
</script>
