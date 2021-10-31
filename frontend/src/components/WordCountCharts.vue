<template>
    <div id="wrapper">
        <div class="container">
            <div>
                <canvas id="cummingsWordCountChart"></canvas>
            </div>  
            <div>
                <canvas id="shakespeareWordCountChart"></canvas>
            </div>  
                <div>
                <canvas id="ginsbergWordCountChart"></canvas>
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
                        "shakespeare_words": this.shakespeare_words,
                        "shakespeare_counts": this.shakespeare_counts,
                        "ginsberg_words": this.ginsberg_words,
                        "ginsberg_counts": this.ginsberg_counts,
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
                            'rgba(75, 192, 192, 0.4)',
                            'rgba(75, 192, 192, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
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
        get_shakespeare_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.shakespeare_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.4)',
                            'rgba(75, 192, 192, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
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
        get_ginsberg_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.ginsberg_words,
                    datasets: [{
                        label: 'counts',
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.4)',
                            'rgba(75, 192, 192, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
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
        }

    },
    mounted() {
        this.get_statistics(this.get_cummings_chart),
        this.get_statistics(this.get_shakespeare_chart),
        this.get_statistics(this.get_ginsberg_chart)
    }
}
</script>

<style>

</style>