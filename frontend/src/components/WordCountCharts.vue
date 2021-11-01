<template>
    <div id="wrapper">
        <div class="container">
            <h1 class="is-size-4"> e.e.cummings </h1>
            <h2 class="is-size-5"> Original poems </h2>
            <div>
                <canvas id="cummingsWordCountChart"></canvas>
            </div>  
            <h2 class="is-size-5"> Generated poems </h2>
            <div>
                <canvas id="generatedCummingsWordCountChart"></canvas>
            </div>  
            <h1 class="is-size-4"> William Shakespare </h1>
            <h2 class="is-size-5"> Original poems </h2>
            <div>
                <canvas id="shakespeareWordCountChart"></canvas>
            </div> 
            <h2 class="is-size-5"> Generated poems </h2>
            <div>
                <canvas id="generatedShakespeareWordCountChart"></canvas>
            </div>
            <h1 class="is-size-4"> Allen Ginsberg </h1>
            <h2 class="is-size-5"> Original poems </h2> 
            <div>
                <canvas id="ginsbergWordCountChart"></canvas>
            </div>  
            <h2 class="is-size-5"> Generated poems </h2>
            <div>
                <canvas id="generatedGinsbergWordCountChart"></canvas>
            </div>  
        </div>
    </div>        
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: "WordCountChart",
    data() {
        return {
            words: [],
            counts: [],
        }
    },
    methods: {
        get_statistics(callback = () => "lol"){
            fetch(`${API_URL}/api/statistics/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        "cummings_words": this.cummings_words,
                        "cummings_counts": this.cummings_counts,
                        "generated_cummings_words": this.generated_cummings_words,
                        "generated_cummings_counts": this.generated_cummings_counts,
                        "shakespeare_words": this.shakespeare_words,
                        "shakespeare_counts": this.shakespeare_counts,
                        "generated_shakespeare_words": this.generated_shakespeare_words,
                        "generated_shakespeare_counts": this.generated_shakespeare_counts,
                        "ginsberg_words": this.ginsberg_words,
                        "ginsberg_counts": this.ginsberg_counts,
                        "generated_ginsberg_words": this.generated_ginsberg_words,
                        "generated_ginsberg_counts": this.generated_ginsberg_counts,
                    } = data)
                    callback()
                })
                .catch(err => console.log(err.message))
        },
        get_cummings_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.cummings_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(19, 80, 93, 0.4)',
                            'rgba(19, 80, 93, 0.4)',
                        ],
                        borderColor: [
                            'rgb(19, 80, 93)',
                            'rgb(19, 80, 93)',
                        ],
                        borderWidth: 1,
                        data: this.cummings_counts,
                    }]
                },
                options: {}
            }

            let cummingsWordCountChart = new Chart(
                document.getElementById('cummingsWordCountChart'),
                config
            )
        },
        get_generated_cummings_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_cummings_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(19, 80, 93, 0.8)',
                            'rgba(19, 80, 93, 0.8)',
                        ],
                        borderColor: [
                            'rgb(19, 80, 93)',
                            'rgb(19, 80, 93)',
                        ],
                        borderWidth: 1,
                        data: this.generated_cummings_counts,
                    }]
                },
                options: {}
            }

            let generatedCummingsWordCountChart = new Chart(
                document.getElementById('generatedCummingsWordCountChart'),
                config
            )
        },
        get_shakespeare_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.shakespeare_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(224, 206, 117, 0.4)',
                            'rgba(224, 206, 117, 0.4)',
                        ],
                        borderColor: [
                            'rgb(224, 206, 117)',
                            'rgb(224, 206, 117)',
                        ],
                        borderWidth: 1,
                        data: this.shakespeare_counts,
                    }]
                },
                options: {}
            }

            let shakespeareWordCountChart = new Chart(
                document.getElementById('shakespeareWordCountChart'),
                config
            )
        },
        get_generated_shakespeare_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_shakespeare_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(224, 206, 117, 0.8)',
                            'rgba(224, 206, 117, 0.8)',
                        ],
                        borderColor: [
                            'rgb(224, 192, 117)',
                            'rgb(224, 192, 117)',
                        ],
                        borderWidth: 1,
                        data: this.generated_shakespeare_counts,
                    }]
                },
                options: {}
            }

            let generatedShakespeareWordCountChart = new Chart(
                document.getElementById('generatedShakespeareWordCountChart'),
                config
            )
        },
        get_ginsberg_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.ginsberg_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(181, 156, 192, 0.4)',
                            'rgba(181, 156, 192, 0.4)',
                        ],
                        borderColor: [
                            'rgb(181, 156, 192)',
                            'rgb(181, 156, 192)',
                        ],
                        borderWidth: 1,
                        data: this.ginsberg_counts,
                    }]
                },
                options: {}
            }
            let ginsbergWordCountChart = new Chart(
                document.getElementById('ginsbergWordCountChart'),
                config
            )
        },
        get_generated_ginsberg_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_ginsberg_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(181, 156, 192, 0.8)',
                            'rgba(181, 156, 192, 0.8)',
                        ],
                        borderColor: [
                            'rgb(181, 156, 192)',
                            'rgb(181, 156, 192)',
                        ],
                        borderWidth: 1,
                        data: this.generated_ginsberg_counts,
                    }]
                },
                options: {}
            }
            let generatedGinsbergWordCountChart = new Chart(
                document.getElementById('generatedGinsbergWordCountChart'),
                config
            )
        }

    },
    
    mounted() {
        this.get_statistics(this.get_cummings_chart),
        this.get_statistics(this.get_generated_cummings_chart),
        this.get_statistics(this.get_shakespeare_chart),
        this.get_statistics(this.get_generated_shakespeare_chart),
        this.get_statistics(this.get_ginsberg_chart),
        this.get_statistics(this.get_generated_ginsberg_chart)

    }
}
</script>

<style>

</style>