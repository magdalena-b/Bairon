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
            <div class="column is-7-desktop">
                <h1 class="is-size-1-tablet is-size-2-mobile has-text-weight-bold mb-6">
                    Become world class artist and create your own masterpiece!
                </h1>
                <router-link to="/generate">
                    <button class="button is-primary is-large is-rounded">
                        Check it out!
                    </button>
                </router-link>
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