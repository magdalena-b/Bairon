<template>
    <div class="about">
        <h1>About this project</h1>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quos ab esse accusamus quae possimus culpa nesciunt voluptatum recusandae odit tempore molestiae voluptatem sit assumenda dolor quas nihil, neque cumque illo!</p>

        <h2>rating</h2>
        <p>Average rating: {{score}}</p>
        <p>Turing Test votes (M/H): {{TT_machine}} vs. {{TT_human}}</p>
        <h2>backend</h2>
        <section id="backend">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" alt="">
        </section>
        <h2>frontend</h2>
        <section id="frontend">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" alt="">
            <img src="https://seeklogo.com/images/B/bulma-logo-45B5145BF4-seeklogo.com.png" alt="">
        </section>
        <h2>NLP</h2>
        <section id="NLP">
            <img src="https://venturebeat.com/wp-content/uploads/2019/04/d2fcb133-1ed1-4a92-bd7f-8be7cfc96cec.png?w=1200&strip=all" alt="">
        </section>
    </div>
</template>

<script>
const {API_URL} = require('../settings.json')

export default ({
    name: "About",
    data() {
        return {
            score: 0,
            TT_machine: 0,
            TT_human: 0,
        }
    },
    methods: {
        get_rating(){
            fetch(`${API_URL}/api/rating/`)
                .then(res => res.json())
                .then(data => {
                    ({"TT-human": this.TT_human, "TT-machine": this.TT_machine, "rate-average": this.score} = data)
                })
                .catch(err => console.log(err.message))
        },
    },
    mounted() {
        this.get_rating()
    }
})
</script>

<style scoped>
    section{
        height: 10vh;
        display: flex;
        justify-content: center;
    }
    img {
        max-height: 100%;
    }
</style>
