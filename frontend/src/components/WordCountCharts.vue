<template>
    <div id="wrapper">
            <div class="container">
                <h1 class="is-size-4"> e. e. cummings </h1>
                <div class="columns is-centered is-vcentered">
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Original poems </h2>
                        <div>
                            <canvas id="cummingsWordCountChart"></canvas>
                        </div>  
                    </div>
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Generated poems - GPT2 </h2>
                        <div>
                            <canvas id="generatedcummingsGPT2WordCountChart"></canvas>
                        </div>  
                    </div>
                </div>
                <!-- <div class="columns is-centered is-vcentered">
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Generated poems - GPT-Neo </h2>
                        <div>
                            <canvas id="generatedcummingsGPTNeoWordCountChart"></canvas>
                        </div>  
                    </div>
                </div> -->
            </div>
            <div class="container">
                <h1 class="is-size-4"> William Shakespeare </h1>
                <div class="columns is-centered is-vcentered">
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Original poems </h2>
                        <div>
                            <canvas id="shakespeareWordCountChart"></canvas>
                        </div>  
                    </div>
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Generated poems - GPT2 </h2>
                        <div>
                            <canvas id="generatedshakespeareGPT2WordCountChart"></canvas>
                        </div>  
                    </div>
                </div>
                <!-- <div class="columns is-centered is-vcentered">
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Generated poems - GPT-Neo </h2>
                        <div>
                            <canvas id="generatedshakespeareGPTNeoWordCountChart"></canvas>
                        </div>  
                    </div>
                </div> -->
            </div>
            <div class="container">
                <h1 class="is-size-4"> Walt Whitman </h1>
                <div class="columns is-centered is-vcentered">
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Original poems </h2>
                        <div>
                            <canvas id="whitmanWordCountChart"></canvas>
                        </div>  
                    </div>
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Generated poems - GPT2 </h2>
                        <div>
                            <canvas id="generatedwhitmanGPT2WordCountChart"></canvas>
                        </div>  
                    </div>
                </div>
                <!-- <div class="columns is-centered is-vcentered">
                    <div class="column is-6 is-12-mobile">
                        <h2 class="is-size-5"> Generated poems - GPT-Neo </h2>
                        <div>
                            <canvas id="generatedwhitmanGPTNeoWordCountChart"></canvas>
                        </div>  
                    </div>
                </div> -->
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
                        "generated_cummings_gpt2_words": this.generated_cummings_gpt2_words,
                        "generated_cummings_gpt2_counts": this.generated_cummings_gpt2_counts,
                        "generated_cummings_gpt_neo_words": this.generated_cummings_gpt_neo_words,
                        "generated_cummings_gpt_neo_counts": this.generated_cummings_gpt_neo_counts,

                        "shakespeare_words": this.shakespeare_words,
                        "shakespeare_counts": this.shakespeare_counts,
                        "generated_shakespeare_gpt2_words": this.generated_shakespeare_gpt2_words,
                        "generated_shakespeare_gpt2_counts": this.generated_shakespeare_gpt2_counts,
                        "generated_shakespeare_gpt_neo_words": this.generated_shakespeare_gpt_neo_words,
                        "generated_shakespeare_gpt_neo_counts": this.generated_shakespeare_gpt_neo_counts,

                        "whitman_words": this.whitman_words,
                        "whitman_counts": this.whitman_counts,
                        "generated_whitman_gpt2_words": this.generated_whitman_gpt2_words,
                        "generated_whitman_gpt2_counts": this.generated_whitman_gpt2_counts,
                        "generated_whitman_gpt_neo_words": this.generated_whitman_gpt_neo_words,
                        "generated_whitman_gpt_neo_counts": this.generated_whitman_gpt_neo_counts,

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

            let cummingsGWordCountChart = new Chart(
                document.getElementById('cummingsWordCountChart'),
                config
            )
        },
        get_generated_cummings_gpt2_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_cummings_gpt2_words,
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
                        data: this.generated_cummings_gpt2_counts,
                    }]
                },
                options: {}
            }

            let generatedcummingsGPT2WordCountChart = new Chart(
                document.getElementById('generatedcummingsGPT2WordCountChart'),
                config
            )
        },
        get_generated_cummings_gpt_neo_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_cummings_gpt_neo_words,
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
                        data: this.generated_cummings_gpt_neo_counts,
                    }]
                },
                options: {}
            }

            let generatedcummingsGPTNeoWordCountChart = new Chart(
                document.getElementById('generatedcummingsGPTNeoWordCountChart'),
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
        get_generated_shakespeare_gpt2_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_shakespeare_gpt2_words,
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
                        data: this.generated_shakespeare_gpt2_counts,
                    }]
                },
                options: {}
            }

            let generatedshakespeareGPT2WordCountChart = new Chart(
                document.getElementById('generatedshakespeareGPT2WordCountChart'),
                config
            )
        },
        get_generated_shakespeare_gpt_neo_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_shakespeare_gpt_neo_words,
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
                        data: this.generated_shakespeare_gpt_neo_counts,
                    }]
                },
                options: {}
            }

            let generatedshakespeareGPTNeoWordCountChart = new Chart(
                document.getElementById('generatedshakespeareGPTNeoWordCountChart'),
                config
            )
        },
        get_whitman_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.whitman_words,
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
                        data: this.whitman_counts,
                    }]
                },
                options: {}
            }
            let whitmanWordCountChart = new Chart(
                document.getElementById('whitmanWordCountChart'),
                config
            )
        },
        get_generated_whitman_gpt2_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_whitman_gpt2_words,
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
                        data: this.generated_whitman_gpt2_counts,
                    }]
                },
                options: {}
            }
            let generatedwhitmanGPT2WordCountChart = new Chart(
                document.getElementById('generatedwhitmanGPT2WordCountChart'),
                config
            )
        },
        get_generated_whitman_gpt_neo_chart(){
            let config = {
                type: 'bar',
                data: {
                    labels: this.generated_whitman_gpt_neo_words,
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
                        data: this.generated_whitman_gpt_neo_counts,
                    }]
                },
                options: {}
            }
            let generatedwhitmanGPTNeoWordCountChart = new Chart(
                document.getElementById('generatedwhitmanGPTNeoWordCountChart'),
                config
            )
        }

    },
    
    mounted() {
        this.get_statistics(this.get_cummings_chart),
        this.get_statistics(this.get_generated_cummings_gpt2_chart),
        this.get_statistics(this.get_generated_cummings_gpt_neo_chart),
        this.get_statistics(this.get_shakespeare_chart),
        this.get_statistics(this.get_generated_shakespeare_gpt2_chart),
        this.get_statistics(this.get_generated_shakespeare_gpt_neo_chart),
        this.get_statistics(this.get_whitman_chart),
        this.get_statistics(this.get_generated_whitman_gpt2_chart),
        this.get_statistics(this.get_generated_whitman_gpt_neo_chart)

    }
}
</script>

<style>

</style>