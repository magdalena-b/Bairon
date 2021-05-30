<template>
    <!-- <main>
        <div id="hero">
            <h1>Become world class artist and create your own masterpiece!</h1>
            <router-link to="/generate"><button>Check it out!</button></router-link>
            <h2>... or just check others popular poems<router-link to="/poems">here</router-link></h2>
        </div>
        <Gallery />
    </main> -->
    <div class="container">
        <div class="columns is-vcentered has-text-centered">
            <div class="column is-7-desktop is-12-tablet">
                <div class="hero is-fullheight-with-navbar">
                    <div class="hero-body">
                        <div>
                            <h1 class="is-size-1-tablet is-size-2-mobile has-text-weight-bold">
                                Become world class artist and create your own masterpiece!
                            </h1>
                            <router-link to="/generate">
                                <button class="button is-primary is-large is-rounded my-5">
                                    Check it out!
                                </button>
                            </router-link>
                            <h2 class="is-size-4-tablet is-size-5-mobile">
                                ... or just check others popular poems <router-link to="/poems" class="has-text-primary has-text-weight-bold">here</router-link>
                            </h2>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-5-desktop is-hidden-touch">
                <Gallery />
            </div>
        </div>
    </div>
</template>

<script>
import Gallery from '@/components/Gallery.vue'

export default {
  name: 'Home',
  components: {
    Gallery
  },
}
</script>

<style scoped>
.columns {
    min-height: 100vh;
}
</style>