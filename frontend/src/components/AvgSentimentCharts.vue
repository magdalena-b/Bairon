<template>
    <div id="wrapper">
        <div class="container has-text-centered">
            <h1 class="is-size-3">
                Discover the average emotion analysis of original and created by You poems!
            </h1>
            <h1 class="is-size-4"> e.e.cummings </h1>
            <div class="columns is-vcentered is-centered is-multiline  has-text-centered">    
                <div class="column is-6-desktop is-10-tablet">
                    <h2 class="is-size-5"> Original poems </h2>
                    <div>
                        <canvas id="cummingsAvgSentimentChart"></canvas>
                    </div>
                </div>  
                <div class="column is-6-desktop is-10-tablet">
                    <h2 class="is-size-5"> Generated poems </h2>
                    <div>
                        <canvas id="generatedCummingsAvgSentimentChart"></canvas>
                    </div>
                </div>
            </div>  
            <h1 class="is-size-4"> William Shakespare </h1>
            <div class="columns is-vcentered is-centered is-multiline  has-text-centered">    
                <div class="column is-6-desktop is-10-tablet">
                    <h2 class="is-size-5"> Original poems </h2>
                    <div>
                        <canvas id="shakespeareAvgSentimentChart"></canvas>
                    </div> 
                </div>
                <div class="column is-6-desktop is-10-tablet">
                    <h2 class="is-size-5"> Generated poems </h2>
                    <div>
                        <canvas id="generatedShakespeareAvgSentimentChart"></canvas>
                    </div>
                </div>
            </div>
            <h1 class="is-size-4"> Walt Whitman </h1>
            <div class="columns is-vcentered is-centered is-multiline  has-text-centered">    
                <div class="column is-6-desktop is-10-tablet">   
                    <h2 class="is-size-5"> Original poems </h2> 
                    <div>
                        <canvas id="whitmanAvgSentimentChart"></canvas>
                    </div>
                </div>  
                <div class="column is-6-desktop is-10-tablet">    
                    <h2 class="is-size-5"> Generated poems </h2>
                    <div>
                        <canvas id="generatedWhitmanAvgSentimentChart"></canvas>
                    </div>  
                </div>
            </div>
        </div>
    </div>        
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: "AvgSentimentCharts",
    data() {
        return {
            keys: [],
            values: [],
        }
    },
    methods: {
        get_avg_sentiment(callback = () => "sth"){
            fetch(`${API_URL}/api/sentiment-analysis/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        "generated_cummings_analysis": this.generated_cummings_analysis,
                        "generated_shakespeare_analysis": this.generated_shakespeare_analysis,
                        "generated_whitman_analysis": this.generated_whitman_analysis,
                        "cummings_analysis": this.cummings_analysis,
                        "shakespeare_analysis": this.shakespeare_analysis,
                        "whitman_analysis": this.whitman_analysis,

                    } = data)
                    callback()
                })
                .catch(err => console.log(err.message))
        },
        get_cummings_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(this.cummings_analysis),
                    datasets: [{
                        label: 'values',
                        backgroundColor: [
                            'rgba(19, 80, 93, 0.4)',
                            'rgba(19, 80, 93, 0.4)',
                        ],
                        borderColor: [
                            'rgb(19, 80, 93)',
                            'rgb(19, 80, 93)',
                        ],
                        borderWidth: 1,
                        data: Object.values(this.cummings_analysis),
                    }]
                },
                options: {}
            }

            let cummingsWordCountChart = new Chart(
                document.getElementById('cummingsAvgSentimentChart'),
                config
            )
        },
        get_generated_cummings_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(this.generated_cummings_analysis),
                    datasets: [{
                        label:'values',
                        backgroundColor: [
                            'rgba(19, 80, 93, 0.8)',
                            'rgba(19, 80, 93, 0.8)',
                        ],
                        borderColor: [
                            'rgb(19, 80, 93)',
                            'rgb(19, 80, 93)',
                        ],
                        borderWidth: 1,
                        data: Object.values(this.generated_cummings_analysis),
                    }]
                },
                options: {}
            }

            let generatedCummingsAvgSentimentChart = new Chart(
                document.getElementById('generatedCummingsAvgSentimentChart'),
                config
            )
        },
        get_shakespeare_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(this.shakespeare_analysis),
                    datasets: [{
                        label:'values',
                        backgroundColor: [
                            'rgba(224, 206, 117, 0.4)',
                            'rgba(224, 206, 117, 0.4)',
                        ],
                        borderColor: [
                            'rgb(224, 206, 117)',
                            'rgb(224, 206, 117)',
                        ],
                        borderWidth: 1,
                        data: Object.values(this.shakespeare_analysis),
                    }]
                },
                options: {}
            }

            let shakespeareAvgSentimentChart = new Chart(
                document.getElementById('shakespeareAvgSentimentChart'),
                config
            )
        },
        get_generated_shakespeare_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(this.generated_shakespeare_analysis),
                    datasets: [{
                        label:'values',
                        backgroundColor: [
                            'rgba(224, 206, 117, 0.8)',
                            'rgba(224, 206, 117, 0.8)',
                        ],
                        borderColor: [
                            'rgb(224, 192, 117)',
                            'rgb(224, 192, 117)',
                        ],
                        borderWidth: 1,
                        data: Object.values(this.generated_shakespeare_analysis),
                    }]
                },
                options: {}
            }

            let generatedShakespeareAvgSentimentChart = new Chart(
                document.getElementById('generatedShakespeareAvgSentimentChart'),
                config
            )
        },
        get_whitman_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(this.whitman_analysis),
                    datasets: [{
                        label:'values',
                        backgroundColor: [
                            'rgba(181, 156, 192, 0.4)',
                            'rgba(181, 156, 192, 0.4)',
                        ],
                        borderColor: [
                            'rgb(181, 156, 192)',
                            'rgb(181, 156, 192)',
                        ],
                        borderWidth: 1,
                        data: Object.values(this.whitman_analysis),
                    }]
                },
                options: {}
            }
            let whitmanAvgSentimentChart = new Chart(
                document.getElementById('whitmanAvgSentimentChart'),
                config
            )
        },
        get_generated_whitman_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: Object.keys(this.generated_whitman_analysis),
                    datasets: [{
                        label:'values',
                        backgroundColor: [
                            'rgba(181, 156, 192, 0.8)',
                            'rgba(181, 156, 192, 0.8)',
                        ],
                        borderColor: [
                            'rgb(181, 156, 192)',
                            'rgb(181, 156, 192)',
                        ],
                        borderWidth: 1,
                        data: Object.values(this.generated_whitman_analysis),
                    }]
                },
                options: {}
            }
            let generatedWhitmanAvgSentimentChart = new Chart(
                document.getElementById('generatedWhitmanAvgSentimentChart'),
                config
            )
        }
    },

    mounted() {
        this.get_avg_sentiment(this.get_cummings_chart),
        this.get_avg_sentiment(this.get_shakespeare_chart),
        this.get_avg_sentiment(this.get_whitman_chart),
        this.get_avg_sentiment(this.get_generated_cummings_chart),
        this.get_avg_sentiment(this.get_generated_shakespeare_chart),
        this.get_avg_sentiment(this.get_generated_whitman_chart)

    }
}
</script>

<style>

</style>
