<template>
    <div class="carousel">
        <div class="item" v-if="'Shakespeare'===current_poet">
            <img alt="shakespeare" src="../assets/Shakespeare.jpg">
        </div>
        <div class="item" v-if="'Ginsberg'===current_poet">
            <img alt="ginsberg" src="../assets/Ginsberg.jpg">
        </div>
    </div>
</template>

<script>
export default {
    name: 'Gallery',
    components: {
    },
    props: ["current_author"],
    data() {
        return {
            current_poet: "Ginsberg"
        }
    },

}
</script>

<style scoped>

	img {
		width: 80%;
	}

    .carousel {
        width: 40vw;
        height: 80vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>