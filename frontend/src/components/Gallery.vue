<template>
    <div class="container">
        <h4 class="is-size-3 has-text-centered">
            meet our artists
        </h4>
        <div id="carousel-demo" class="carousel">
            <div class="item-1 py-5 px-5 has-text-centered">
                <img alt="shakespeare" src="../assets/Shakespeare.jpg">
                <h2 class="is-size-4"> William Shakespeare </h2>
                <div class="tabs is-centered is-boxed">
                    <ul>
                        <li class="about_button" data-target="about" v-bind:class="{'is-active': info_type == 'about'}"><a class="has-text-dark">about</a></li>
                        <li class="example_button" data-target="example" v-bind:class="{'is-active': info_type == 'example'}"><a class="has-text-dark">example</a></li>
                    </ul>
                </div> 
                <div class="px-2" id="tab-content">
                    <div id="about" v-bind:class="{'is-hidden': info_type != 'about'}">
                        <h3>English poet and dramatist from 16th/17th century, by some considered the greatest English writer of all time.</h3>
                    </div>
                    <div id="example" v-bind:class="{'is-hidden': info_type != 'example'}">
                        <p class="is-size-6 has-text-left" v-for="line in shakespeare_example.split('\n')" :key="line">{{ line }}</p>
                    </div>
                </div>
            </div>
            <div class="item-2 py-5 px-5 has-text-centered">
                <img alt="shakespeare" src="../assets/cummings.jpg">
                <h2 class="is-size-4"> e.e. cummings </h2>
                <div class="tabs is-centered is-boxed">
                    <ul>
                        <li class="about_button" data-target="about" v-bind:class="{'is-active': info_type == 'about'}"><a class="has-text-dark">about</a></li>
                        <li class="example_button" data-target="example" v-bind:class="{'is-active': info_type == 'example'}"><a class="has-text-dark">example</a></li>
                    </ul>
                </div> 
                <div class="px-2" id="tab-content">
                    <div id="about" v-bind:class="{'is-hidden': info_type != 'about'}">
                        <h3>American poet from 20th century, wrote modernist free-form poetry, known for his experiments with style and syntax.</h3>
                    </div>
                    <div id="example" v-bind:class="{'is-hidden': info_type != 'example'}">
                        <p class="is-size-6 has-text-left" v-for="line in cummings_example.split('\n')" :key="line">{{ line }}</p>
                    </div>
                </div>
            </div>
            <div class="item-3 py-5 px-5 has-text-centered">
                <img alt="shakespeare" src="../assets/whitman.jpg">
                <h2 class="is-size-4"> Walt Whitman </h2>
                <div class="tabs is-centered is-boxed">
                    <ul>
                        <li class="about_button" data-target="about" v-bind:class="{'is-active': info_type == 'about'}"><a class="has-text-dark">about</a></li>
                        <li class="example_button" data-target="example" v-bind:class="{'is-active': info_type == 'example'}"><a class="has-text-dark">example</a></li>
                    </ul>
                </div> 
                <div class="px-2" id="tab-content">
                    <div id="about" v-bind:class="{'is-hidden': info_type != 'about'}">
                        <h3>American poet from 19th century, often called the father of free verse.</h3>
                    </div>
                    <div id="example" v-bind:class="{'is-hidden': info_type != 'example'}">
                        <p class="is-size-6 has-text-left" v-for="line in whitman_example.split('\n')" :key="line">{{ line }}</p>
                    </div>
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
            info_type: "about",
            current_poet: "Cummings",
            shakespeare_example: "When forty winters shall besiege thy brow,\nAnd dig deep trenches in thy beauty's field,\nThy youth's proud livery so gazed on now,\nWill be a totter'd weed of small worth held:\nThen being asked, where all thy beauty lies,\nWhere all the treasure of thy lusty days;\nTo say, within thine own deep sunken eyes,\nWere an all-eating shame, and thriftless praise.\nHow much more praise deserv'd thy beauty's use,\nIf thou couldst answer 'This fair child of mine\nShall sum my count, and make my old excuse,'\nProving his beauty by succession thine!\nThis were to be new made when thou art old,\nAnd see thy blood warm when thou feel'st it cold.",
            cummings_example: "a wind has blown the rain away and blown\nthe sky away and all the leaves away,\nand the trees stand.  I think i too have known\nautumn too long\n               (and what have you to say,\nwind wind wind—did you love somebody\nand have you the petal of somewhere in your heart\npinched from dumb summer?\n                            O crazy daddy\nof death dance cruelly for us and start\nthe last leaf whirling in the final brain\nof air!)Let us as we have seen see\ndoom’s integration………a wind has blown the rain\n\naway and the leaves and the sky and the\ntrees stand:\n            the trees stand.  The trees,\nsuddenly wait against the moon’s face.",
            whitman_example: "Passing stranger! you do not know how longingly I look upon you,\nYou must be he I was seeking, or she I was seeking, (it comes to me as of a dream,)\nI have somewhere surely lived a life of joy with you,\nAll is recall’d as we flit by each other, fluid, affectionate, chaste, matured,\nYou grew up with me, were a boy with me or a girl with me,\nI ate with you and slept with you, your body has become not yours only nor left my body mine only,\nYou give me the pleasure of your eyes, face, flesh, as we pass, you take of my beard, breast, hands, in return,\nI am not to speak to you, I am to think of you when I sit alone or wake at night alone,\nI am to wait, I do not doubt I am to meet you again,\nI am to see to it that I do not lose you.\n",
        }
    },
    mounted() {
        bulmaCarousel.attach('#carousel-demo', {
            slidesToScroll: 1,
            slidesToShow: 1,
            infinite: true,
            autoplay: this.autoplay,
            autoplaySpeed: 3000,
	    })

        const abs = document.querySelectorAll('.about_button')
        const ebs = document.querySelectorAll('.example_button')
        
        abs.forEach(ab => ab.addEventListener("click", () => {this.info_type = "about"}))
        ebs.forEach(eb => eb.addEventListener("click", () => {this.info_type = "example"}))


    }

}
</script>

<style scoped>
    .carousel {
        overflow: hidden;
    }

    img {
        height: 25vmin;
        max-width: 100%;
        overflow: hidden;
    }
</style>