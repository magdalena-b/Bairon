<template>
    <div class="container">
        <div class="columns is-vcentered has-text-centered is-centered is-multiline">
            <div class="column is-7-desktop is-12-tablet">
                <div class="hero is-large">
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

export default {
  name: 'Home',
  components: {
    Gallery,
    HeroImage
  },
}
</script>

<style scoped>
.columns {
    /* min-height: 100vh; */
}
</style>