<template>
    <div id="wrapper">
        <div class="container has-text-centered">
            <h1 class="is-size-2">Poetry Turing Test Statistics</h1>
            <div>
                <div class="container">
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-6 is-12-mobile">
                            <h1 class="is-size-3">GPT2</h1>
                        </div>  
                        <!-- <div class="column is-5 is-12-mobile">
                            <h1 class="is-size-3">GPT-Neo</h1>
                        </div> -->
                    </div>
                </div>
                <div class="container">
                    <h1 class="is-size-4"> e.e.cummings </h1>
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-6 is-12-mobile">
                                <canvas id="cummings_GPT2_TTChart"></canvas> 
                        </div>  
                        <!-- <div class="column is-5 is-12-mobile">
                                <canvas id="cummings_GPT_Neo_TTChart"></canvas> 
                        </div> -->
                    </div>
                </div>
                <div class="container">
                    <h1 class="is-size-4"> William Shakespare </h1>
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-6 is-12-mobile">
                            <canvas id="shakespeare_GPT2_TTChart"></canvas>
                        </div>
                        <!-- <div class="column is-5 is-12-mobile">
                            <canvas id="shakespeare_GPT_Neo_TTChart"></canvas>
                        </div> -->
                    </div>
                </div>
                <div class="container">
                    <h1 class="is-size-4"> Walt Whitman </h1>
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-5 is-12-mobile">
                            <canvas id="whitman_GPT2_TTChart"></canvas>
                        </div>
                        <!-- <div class="column is-5 is-12-mobile">
                            <canvas id="whitman_GPT_Neo_TTChart"></canvas>
                        </div> -->
                    </div>
                </div>
            </div>
        </div>
    </div>        
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: "DetailedTTChart",
    data() {
        return {
            TT_TM_gpt2_whitman: 0,
            TT_TM_gpt_neo_whitman: 0, 
            TT_FH_gpt2_whitman: 0,
            TT_FH_gpt_neo_whitman: 0,


            TT_TM_gpt2_cummings: 0,
            TT_TM_gpt_neo_cummings: 0,
            TT_FH_gpt2_cummings: 0,
            TT_FH_gpt_neo_cummings: 0,


            TT_TM_gpt2_shakespeare: 0,
            TT_TM_gpt_neo_shakespeare: 0,
            TT_FH_gpt2_shakespeare: 0,
            TT_FH_gpt_neo_shakespeare: 0,

            TT_TH: 0,
            TT_FM: 0,

        }
    },
    methods: {
        get_statistics(callback = () => "lol"){
            fetch(`${API_URL}/api/poetry-turing-test-statistics/`)
                .then(res => res.json())
                .then(data => {
                    ({

                        "TT-TM-gpt2-whitman": this.TT_TM_gpt2_whitman,
                        "TT-TM-gpt-neo-whitman": this.TT_TM_gpt_neo_whitman,
                        "TT-FH-gpt2-whitman": this.TT_FH_gpt2_whitman,
                        "TT-FH-gpt-neo-whitman": this.TT_FH_gpt_neo_whitman,
                        "TT-TH-whitman": this.TT_TH_whitman,
                        "TT-FM-whitman": this.TT_FM_whitman,


                        "TT-TM-gpt2-cummings": this.TT_TM_gpt2_cummings,
                        "TT-TM-gpt-neo-cummings": this.TT_TM_gpt_neo_cummings,
                        "TT-FH-gpt2-cummings": this.TT_FH_gpt2_cummings,
                        "TT-FH-gpt-neo-cummings": this.TT_FH_gpt_neo_cummings,
                        "TT-TH-cummings": this.TT_TH_cummings,
                        "TT-FM-cummings": this.TT_FM_cummings,


                        "TT-TM-gpt2-shakespeare": this.TT_TM_gpt2_shakespeare,
                        "TT-TM-gpt-neo-shakespeare": this.TT_TM_gpt_neo_shakespeare,
                        "TT-FH-gpt2-shakespeare": this.TT_FH_gpt2_shakespeare,
                        "TT-FH-gpt-neo-shakespeare": this.TT_FH_gpt_neo_shakespeare,
                        "TT-TH-shakespeare": this.TT_TH_shakespeare,
                        "TT-FM-shakespeare": this.TT_FM_shakespeare,
                        

                        "TT-TH": this.TT_TH,
                        "TT-FM": this.TT_FM


                    } = data)
                    callback()
                })
                .catch(err => console.log(err.message))
        },


        get_cummings_gpt2_chart(){
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
                        data: [this.TT_TH_cummings, this.TT_TM_gpt2_cummings],
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
                        data: [this.TT_FH_gpt2_cummings, this.TT_FM_cummings],
                    }]
                },
                options: {}
            }

            let cummings_GPT2_TTChart = new Chart(
                document.getElementById('cummings_GPT2_TTChart'),
                config
            )
        },

        get_shakespeare_gpt2_chart(){
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
                        data: [this.TT_TH_shakespeare, this.TT_TM_gpt2_shakespeare],
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
                        data: [this.TT_FH_gpt2_shakespeare, this.TT_FM_shakespeare],
                    }]
                },
                options: {}
            }

            let shakespeare_GPT2_TTChart = new Chart(
                document.getElementById('shakespeare_GPT2_TTChart'),
                config
            )
        },

        get_whitman_gpt2_chart(){
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
                        data: [this.TT_TH_whitman, this.TT_TM_gpt2_whitman],
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
                        data: [this.TT_FH_gpt2_whitman, this.TT_FM_whitman],
                    }]
                },
                options: {}
            }

            let whitman_GPT2_TTChart = new Chart(
                document.getElementById('whitman_GPT2_TTChart'),
                config
            )
        },



        get_cummings_gpt_neo_chart(){
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
                        data: [this.TT_TH_cummings, this.TT_TM_gpt_neo_cummings],
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
                        data: [this.TT_FH_gpt_neo_cummings, this.TT_FM_cummings],
                    }]
                },
                options: {}
            }

            let cummings_GPT_Neo_TTChart = new Chart(
                document.getElementById('cummings_GPT_Neo_TTChart'),
                config
            )
        },

        get_shakespeare_gpt_neo_chart(){
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
                        data: [this.TT_TH_shakespeare, this.TT_TM_gpt_neo_shakespeare],
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
                        data: [this.TT_FH_gpt2_shakespeare, this.TT_FM_shakespeare],
                    }]
                },
                options: {}
            }

            let shakespeare_GPT_Neo_TTChart = new Chart(
                document.getElementById('shakespeare_GPT_Neo_TTChart'),
                config
            )
        },

        get_whitman_gpt_neo_chart(){
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
                        data: [this.TT_TH_whitman, this.TT_TM_gpt_neo_whitman],
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
                        data: [this.TT_FH_gpt_neo_whitman, this.TT_FM_whitman],
                    }]
                },
                options: {}
            }

            let whitman_GPT_Neo_TTChart = new Chart(
                document.getElementById('whitman_GPT_Neo_TTChart'),
                config
            )
        }
        

    },
    
    mounted() {

        this.get_statistics(this.get_cummings_gpt2_chart),
        this.get_statistics(this.get_shakespeare_gpt2_chart),
        this.get_statistics(this.get_whitman_gpt2_chart),

        this.get_statistics(this.get_cummings_gpt_neo_chart),
        this.get_statistics(this.get_shakespeare_gpt_neo_chart),
        this.get_statistics(this.get_whitman_gpt_neo_chart)

    }
}
</script>

<style>

</style>