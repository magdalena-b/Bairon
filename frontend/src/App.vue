<template>
  <Header />
  <router-view/>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
  name: 'Home',
  components: {
    Header,
  },
}
</script>


<style scoped>

</style>
