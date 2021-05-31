<template>
    <!-- <div class="carousel">
        <div class="item" v-if="'Shakespeare'===current_poet">
            <img alt="shakespeare" src="../assets/Shakespeare.jpg">
        </div>
        <div class="item" v-if="'Ginsberg'===current_poet">
            <img alt="ginsberg" src="../assets/Ginsberg.jpg">
        </div>
    </div> -->
    <div class="container">
        <div id="carousel-demo" class="carousel">
            <div class="item-1">
                <div class="item">
                    <img alt="shakespeare" src="../assets/Shakespeare.jpg">
                </div>
            </div>
            <div class="item-2">
                <div class="item">
                    <img alt="shakespeare" src="../assets/ginsberg.jpg">
                </div>
            </div>
            <div class="item-3">
                <div class="item">
                    <img alt="shakespeare" src="../assets/cummings.jpg">
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Gallery',
    components: {
    },
    props: {
        parent: {

        },
        autoplay: {
            default: true,
        }
    },
    data() {
        return {
            current_poet: "Ginsberg"
        }
    },
    mounted() {
        bulmaCarousel.attach('#carousel-demo', {
            slidesToScroll: 1,
            slidesToShow: 1,
            infinite: true,
            autoplay: this.autoplay,
            autoplaySpeed: 2000,
	    });
    }

}
</script>

<style scoped>
    .carousel {
        overflow: hidden;
    }

    img {
        width: 100%;
        overflow: hidden;
    }

    .item {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
</style>