<template>
    <div id="wrapper">
        <div class="container has-text-centered">
            <h1 class="is-size-2">Ratings Statistics</h1>
            <div>
                <div class="container">
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-5 is-12-mobile">
                            <h1 class="is-size-3">GPT2</h1>
                        </div>  
                        <div class="column is-5 is-12-mobile">
                            <h1 class="is-size-3">GPT-Neo</h1>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <h1 class="is-size-4"> e.e.cummings </h1>
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-5 is-12-mobile">
                                <canvas id="cummings_GPT2_RatingsChart"></canvas> 
                        </div>  
                        <div class="column is-5 is-12-mobile">
                                <canvas id="cummings_GPT_Neo_RatingsChart"></canvas> 
                        </div>
                    </div>
                </div>
                <div class="container">
                    <h1 class="is-size-4"> William Shakespare </h1>
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-5 is-12-mobile">
                            <canvas id="shakespeare_GPT2_RatingsChart"></canvas>
                        </div>
                        <div class="column is-5 is-12-mobile">
                            <canvas id="shakespeare_GPT_Neo_RatingsChart"></canvas>
                        </div>

                    </div>
                </div>
                <div class="container">
                    <h1 class="is-size-4"> Walt Whitman </h1>
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-5 is-12-mobile">
                            <canvas id="whitman_GPT2_RatingsChart"></canvas>
                        </div>
                        <div class="column is-5 is-12-mobile">
                            <canvas id="whitman_GPT_Neo_RatingsChart"></canvas>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>        
</template>

<script>
const {API_URL} = require('../settings.json')

export default {
    name: "DetailedRatingsChart",
    data() {
        return {
            overall_cummings_gpt2: 0,
            grammar_cummings_gpt2: 0,
            style_cummings_gpt2: 0,
            
            overall_cummings_gpt_neo: 0,
            grammar_cummings_gpt_neo: 0,
            style_cummings_gpt_neo: 0,


            overall_shakespeare_gpt2: 0,
            grammar_shakespeare_gpt2: 0,
            style_shakespeare_gpt2: 0,
            
            overall_shakespeare_gpt_neo: 0,
            grammar_shakespeare_gpt_neo: 0,
            style_shakespeare_gpt_neo: 0,


            overall_whitman_gpt2: 0,
            grammar_whitman_gpt2: 0,
            style_whitman_gpt2: 0,
            
            overall_whitman_gpt_neo: 0,
            grammar_whitman_gpt_neo: 0,
            style_whitman_gpt_neo: 0,

        }
    },
    methods: {
        get_statistics(callback = () => "lol"){
            fetch(`${API_URL}/api/ratings-statistics/`)
                .then(res => res.json())
                .then(data => {
                    ({

                        "overall-cummings-gpt2": this.overall_cummings_gpt2,
                        "grammar-cummings-gpt2": this.grammar_cummings_gpt2,
                        "style-cummings-gpt2": this.style_cummings_gpt2,

                        "overall-cummings-gpt-neo": this.overall_cummings_gpt_neo,
                        "grammar-cummings-gpt-neo": this.grammar_cummings_gpt_neo,
                        "style-cummings-gpt-neo": this.style_cummings_gpt_neo,


                        "overall-shakespeare-gpt2": this.overall_shakespeare_gpt2,
                        "grammar-shakespeare-gpt2": this.grammar_shakespeare_gpt2,
                        "style-shakespeare-gpt2": this.style_shakespeare_gpt2,

                        "overall-shakespeare-gpt-neo": this.overall_shakespeare_gpt_neo,
                        "grammar-shakespeare-gpt-neo": this.grammar_shakespeare_gpt_neo,
                        "style-shakespeare-gpt-neo": this.style_shakespeare_gpt_neo,


                        "overall-whitman-gpt2": this.overall_whitman_gpt2,
                        "grammar-whitman-gpt2": this.grammar_whitman_gpt2,
                        "style-whitman-gpt2": this.style_whitman_gpt2,

                        "overall-whitman-gpt-neo": this.overall_whitman_gpt_neo,
                        "grammar-whitman-gpt-neo": this.grammar_whitman_gpt_neo,
                        "style-whitman-gpt-neo": this.style_whitman_gpt_neo


                    } = data)
                    callback()
                })
                .catch(err => console.log(err.message))
        },


        get_cummings_gpt2_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: ["overall", "grammar", "style"],
                    datasets: [{
                        label: 'average rating',
                        backgroundColor: [
                            'rgba(13, 189, 143, 0.4)',
                            'rgba(13, 189, 143, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.overall_cummings_gpt2, this.grammar_cummings_gpt2, this.style_cummings_gpt2],
                    }]
                },
                options: {}
            }

            let cummings_GPT2_RatingsChart = new Chart(
                document.getElementById('cummings_GPT2_RatingsChart'),
                config
            )
        },

        get_shakespeare_gpt2_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: ["overall", "grammar", "style"],
                    datasets: [{
                        label: 'average rating',
                        backgroundColor: [
                            'rgba(13, 189, 143, 0.4)',
                            'rgba(13, 189, 143, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.overall_shakespeare_gpt2, this.grammar_shakespeare_gpt2, this.style_shakespeare_gpt2],
                    }]
                },
                options: {}
            }

            let shakespeare_GPT2_RatingsChart = new Chart(
                document.getElementById('shakespeare_GPT2_RatingsChart'),
                config
            )
        },

        get_whitman_gpt2_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: ["overall", "grammar", "style"],
                    datasets: [{
                        label: 'average rating',
                        backgroundColor: [
                            'rgba(13, 189, 143, 0.4)',
                            'rgba(13, 189, 143, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.overall_whitman_gpt2, this.grammar_whitman_gpt2, this.style_whitman_gpt2],
                    }]
                },
                options: {}
            }

            let whitman_GPT2_RatingsChart = new Chart(
                document.getElementById('whitman_GPT2_RatingsChart'),
                config
            )
        },



        get_cummings_gpt_neo_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: ["overall", "grammar", "style"],
                    datasets: [{
                        label: 'average rating',
                        backgroundColor: [
                            'rgba(13, 189, 143, 0.4)',
                            'rgba(13, 189, 143, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.overall_cummings_gpt_neo, this.grammar_cummings_gpt_neo, this.style_cummings_gpt_neo],
                    }]
                },
                options: {}
            }

            let cummings_GPT_Neo_RatingsChart = new Chart(
                document.getElementById('cummings_GPT_Neo_RatingsChart'),
                config
            )
        },

        get_shakespeare_gpt_neo_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: ["overall", "grammar", "style"],
                    datasets: [{
                        label: 'average rating',
                        backgroundColor: [
                            'rgba(13, 189, 143, 0.4)',
                            'rgba(13, 189, 143, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.overall_shakespeare_gpt_neo, this.grammar_shakespeare_gpt_neo, this.style_shakespeare_gpt_neo],
                    }]
                },
                options: {}
            }

            let shakespeare_GPT_Neo_RatingsChart = new Chart(
                document.getElementById('shakespeare_GPT_Neo_RatingsChart'),
                config
            )
        },

        get_whitman_gpt_neo_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: ["overall", "grammar", "style"],
                    datasets: [{
                        label: 'average rating',
                        backgroundColor: [
                            'rgba(13, 189, 143, 0.4)',
                            'rgba(13, 189, 143, 0.4)',
                        ],
                        borderColor: [
                            'rgb(75, 192, 192)',
                            'rgb(75, 192, 192)',
                        ],
                        borderWidth: 1,
                        data: [this.overall_whitman_gpt_neo, this.grammar_whitman_gpt_neo, this.style_whitman_gpt_neo],
                    }]
                },
                options: {}
            }

            let whitman_GPT_Neo_RatingsChart = new Chart(
                document.getElementById('whitman_GPT_Neo_RatingsChart'),
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