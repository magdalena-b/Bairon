<template>
    <div>
        <canvas id="myChart"></canvas>
    </div>  
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: "TTChart",
    data() {
        return {
            score: 0,
            TT_machine: 0,
            TT_human: 0,
            TT_TH: 0,
            TT_FH: 0,
            TT_TM: 0,
            TT_TM: 0,
        }
    },
    methods: {
        get_rating(callback = () => "dupa"){
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
                    labels: ["human", "machine"],
                    datasets: [{
                        label: 'true',
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.4)',
                            'rgba(75, 192, 192, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.TT_TH, this.TT_TM],
                    },
                    {
                        label: 'false',
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.4)',
                            'rgba(255, 99, 132, 0.4)',
                        ],
                        borderColor: [
                            'rgb(255, 99, 132)',
                            'rgb(255, 99, 132)',
                        ],
                        borderWidth: 1,
                        data: [this.TT_FH, this.TT_FH],
                    }]
                },
                options: {}
            }

            let myChart = new Chart(
                document.getElementById('myChart'),
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