<template>
  <div class="container mt-5 text-center">
    <DetailedRatingsChart />
  </div>
</template>


<script>
import DetailedRatingsChart from '@/components/DetailedRatingsChart.vue'
const {API_URL} = require('../settings.json')

    export default {
        name: 'RatingStatistics',
        components: { 
            DetailedRatingsChart
        },
        data() {
            return {

            }
        },
        methods: {
        },
        mounted() {
        }
}
</script>