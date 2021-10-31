<template>
    <div>
        <canvas id="wordCountChart"></canvas>
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
        get_rating(callback = () => "lol"){
            fetch(`${API_URL}/api/statistics/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        "words": this.words,
                        "counts": this.counts,
                    } = data)
                    callback()
                })
                .catch(err => console.log(err.message))
        },
        get_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.words,
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
                        data: this.counts,
                    }]
                },
                options: {}
            }

            let wordCountChart = new Chart(
                document.getElementById('wordCountChart'),
                config
            )
        }
    },
    mounted() {
        this.get_rating(this.get_chart)
    }
}
</script>

<style>

</style>