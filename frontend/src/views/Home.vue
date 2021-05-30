<template>
    <main>
        <div id="hero">
            <h1>Become world class artist and create your own masterpiece!</h1>
            <router-link to="/generate"><button>Check it out!</button></router-link>
            <h2>... or just check others popular poems<router-link to="/poems">here</router-link></h2>
        </div>
        <Gallery />
    </main>
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
</style>