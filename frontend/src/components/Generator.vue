<template>
    <main>
        <div class="poem">
            <button
                v-for="p in avaible_poets"
                :key="p"
                @click="selectPoet(p)"
                v-bind:class="{highlight: p==poet}"
            >
                {{ p }}
            </button>
            <label >Type your first line</label>
            <input type="text" v-model="first_line"/>
            <button @click="fetch_poem">generate!</button>
            <p>{{ first_line }}</p>
            <p>{{ poem }}</p>
        </div>
        <div class="carousel">
            <div class="item" v-if="'Shakespeare'===poet">
                <img alt="shakespeare" src="../assets/Shakespeare.jpg">
            </div>
            <div class="item" v-if="'Ginsberg'===poet">
                <img alt="ginsberg" src="../assets/Ginsberg.jpg">
            </div>
        </div>
    </main>
</template>

<script>

export default {
    name: 'Generator',
    components: { },
    data() {
        return {
            first_line: "",
            poet: "",
            poem: ""
        }
    },
    computed: {
        avaible_poets() {
            // TODO fetch it from server
            this.poet = "Shakespeare"
            return ["Shakespeare", "Ginsberg"]
        }
    },
    methods: {
        selectPoet(poet){
            this.poet = poet
        },
        fetch_poem(){
            //TODO fetching generated data from server
            this.poem = "Ipsum consequat nostrud in Lorem officia. Est reprehenderit duis sunt tempor veniam ipsum adipisicing sit eiusmod sit esse. Aute duis laboris voluptate ea culpa nisi fugiat. Laboris quis cupidatat excepteur Lorem."
        }

    }

}
</script>

<style scoped>
    main {
        /* TODO fix that shit */
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: baseline;
    }

	img {
		width: 80%;
	}

    .poem {
        width: 40vw;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-content: center;
        justify-content: center;
    }

    .carousel {
        width: 40vw;
        height: 80vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .highlight {
        background-color: lightseagreen;
    }
</style>