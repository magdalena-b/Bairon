<template>
    <div class="container">
        <div class="columns is-vcentered has-text-centered is-centered is-multiline">
            <div class="column is-7-desktop is-12-tablet">
                <div class="hero is-medium">
                    <div class="hero-body">
                        <div>
                            <template v-if="count>0">
                                <h4 class="is-size-5-tablet is-size-6-mobile">So far we have helped out <span class="has-text-primary has-text-weight-bold">{{count}}</span> people!</h4>
                            </template>

                            <h1 class="is-size-1-tablet is-size-2-mobile has-text-weight-bold">
                                Become world class artist and create your own masterpiece!
                            </h1>
                            <router-link to="/generate">
                                <button class="button is-primary is-large is-rounded my-5">
                                    Check it out!
                                </button>
                            </router-link>
                            <h2 class="is-size-4-tablet is-size-5-mobile">
                                ... or just check others popular <router-link to="/poems" class="has-text-primary has-text-weight-bold">poems</router-link>
                            </h2>
                            <h2 class="is-size-4-tablet is-size-5-mobile">
                                Remember to give us feedback via <router-link to="/turing-test" class="has-text-primary has-text-weight-bold"> Turing Test</router-link>
                            </h2>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-5 is-4-tablet is-6-mobile">
                <!-- <Gallery :autoplay="false"/> -->
                <!-- <Gallery /> -->
                <HeroImage />
            </div>
        </div>
    </div>
</template>

<script>
import Gallery from '@/components/Gallery.vue'
import HeroImage from '@/components/HeroImage.vue'

const {API_URL} = require('../settings.json')

export default {
    name: 'Home',
    components: {
        Gallery,
        HeroImage
    },
    data() {
            return {
                count: 0,
            }
    },
    methods: {
        fetch_count(line){
                this.count = 0
                
                fetch(`${API_URL}/api/generations-count/`, {
                    method: 'GET',
                })
                    .then(res => res.json())
                    .then(data => {
                        ({count: this.count} = data)
                    })
                    .catch(err => {
                        console.log(err.message)
                    })
            },
    },
    mounted() {
        this.fetch_count()
    }
}
</script>

<style scoped>
.columns {
    min-height: 90vh;
}
</style>