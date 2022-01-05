<template> 
    <div id="wrapper">
        <h1>Sentiment analysis of your generated poem!</h1>
        <canvas id="sentimentChart1"></canvas>  
    </div>    
</template>

<script>
const {API_URL} = require('../settings.json')
export default {
    name: 'SentimentChart',
    components: { },
    props: ["id"],
    data() {
        return {
            keys: [],
            values: [],
            sentiment: "",
        }
    },
    mounted() {
        fetch(`${API_URL}/api/poems/4/`)
            .then(res => res.json())
            .then(data => {
                ({sentiment: this.sentiment, keys: this.keys, values: this.values})
            })
            .catch(err => console.log(err.message))
        this.get_sentiment(this.get_sentiment_chart)
    },
    methods: {
        get_sentiment(){
            fetch(`${API_URL}/api/poems/4/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        sentiment: this.sentiment, keys: this.keys, values: this.values
                    })
                    
                })
                .catch(err => console.log(err.message))
        },
        get_sentiment_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(JSON.parse(this.sentiment)),
                    datasets: [{
                        label: 'values',
                        backgroundColor: [
                            'rgba(181, 156, 192, 0.8)',
                            'rgba(181, 156, 192, 0.8)',
                        ],
                         borderColor: [
                            'rgb(181, 156, 192)',
                            'rgb(181, 156, 192)',
                        ],
                        borderWidth: 1,
                        data: Object.values(JSON.parse(this.sentiment)), 
                    }]
                },
                options: {}
            }
            let sentimentChart1 = new Chart(
                document.getElementById('sentimentChart1'),
                config
            )
        }
    },
    
}
</script>

<style>
</style>
