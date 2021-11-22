<template> 
    <div id="wrapper">
        <h1>Sentiment analysis of your generated poem!</h1>
        <canvas id="sentimentChart1"></canvas>  
    </div>    
</template>

<script>
const {API_URL} = require('../settings.json')
export default {
    name: "SentimentChart",
    data() {
        return {
            keys: [],
            values: [],
        }
    },
    methods: {
        get_sentiment(callback = () => "lol"){
            fetch(`${API_URL}/api/poems/1/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        "sentiment": this.sentiment,
                        "id": this.id,
                    } = data)
                    callback()
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
    
    mounted() {
        this.get_sentiment(this.get_sentiment_chart)
    }
}
</script>

<style>

</style>