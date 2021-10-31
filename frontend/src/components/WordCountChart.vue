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
            words: ['bla', 'obla'],
            counts: [2, 1],
        }
    },
    methods: {
        get_rating(callback = () => "words"){
            fetch(`${API_URL}/api/rating/`)
                .then(res => res.json())
                .then(data => {
                    ({
                        "TT-human": this.TT_human,
                        "TT-machine": this.TT_machine,
                        "rate-average": this.score,
                        "TT-TH": this.TT_TH,
                        "TT-FH": this.TT_FH,
                        "TT-TM": this.TT_TM,
                        "TT-FM": this.TT_FM,
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