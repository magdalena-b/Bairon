<template>
    <main>
        <div class="poem">
            <h2>Select your favourite poet</h2>
            <button v-for="p in avaible_poets" :key="p" @click="selectPoet(p)" v-bind:class="{highlight: p==poet}">
                {{ p }}
            </button>
            <h2 >Type your first line</h2>
            <input type="text" v-model="first_line"/>
            <button @click="fetch_poem">generate</button>
            <div id="poem" v-if="poem != ''">
                <p v-for="line in poem.split('\n')" :key="line">{{ line }}</p>
                <button @click="save_poem">save</button>
            </div>
        </div>
        <!-- <Gallery v-model:current_poet="poet"/> -->
            
        <div class="margin-right-20"  v-if="poet=='Shakespeare'">
            <img src="../assets/Shakespeare.jpg" >  
            <h2> William Shakespeare </h2>
            <h3> English poet and dramatist from 16th/17th century, by some considered the greatest English writer of all time. </h3>
            <p>
                When forty winters shall besiege thy brow,
                <br>And dig deep trenches in thy beauty's field,
                <br>Thy youth's proud livery so gazed on now,
                <br>Will be a totter'd weed of small worth held:
                <br>Then being asked, where all thy beauty lies,
                <br>Where all the treasure of thy lusty days;
                <br>To say, within thine own deep sunken eyes,
                <br>Were an all-eating shame, and thriftless praise.
                <br>How much more praise deserv'd thy beauty's use,
                <br>If thou couldst answer 'This fair child of mine
                <br>Shall sum my count, and make my old excuse,'
                <br>Proving his beauty by succession thine!
                <br>This were to be new made when thou art old,
                <br>And see thy blood warm when thou feel'st it cold.
            </p>    
        </div>

        <div class="margin-right-20"  v-if="poet=='Ginsberg'">
            <img src="../assets/Ginsberg.jpg" >  
            <h2> Allen Ginsberg </h2>
            <h3> American poet from 20th century, one of the beatniks - a literary countercultural movement. </h3>
            <p>
                <br>Strange now to think of you, gone without corsets & eyes, while I walk on the sunny pavement of Greenwich Village.
                <br>downtown Manhattan, clear winter noon, and I’ve been up all night, talking, talking, reading the Kaddish aloud, listening to Ray Charles blues shout blind on the phonograph
                <br>the rhythm the rhythm—and your memory in my head three years after—And read Adonais’ last triumphant stanzas aloud—wept, realizing how we suffer—
                <br>And how Death is that remedy all singers dream of, sing, remember, prophesy as in the Hebrew Anthem, or the Buddhist Book of Answers—and my own imagination of a withered leaf—at dawn—
                <br>Dreaming back thru life, Your time—and mine accelerating toward Apocalypse,
                <br>the final moment—the flower burning in the Day—and what comes after,   
                <br>looking back on the mind itself that saw an American city
                <br>a flash away, and the great dream of Me or China, or you and a phantom Russia, or a crumpled bed that never existed—
                <br>like a poem in the dark—escaped back to Oblivion—
                <br>No more to say, and nothing to weep for but the Beings in the Dream, trapped in its disappearance,
            </p>    
        </div>

        <div class="margin-right-20"  v-if="poet=='Cummings'">
            <img src="../assets/cummings.jpg" >  
            <h2> e.e. cummings </h2>
            <h3> American poet from 20th century, wrote modernist free-form poetry, known for his experiments with style and syntax. </h3>
            <p>
                a wind has blown the rain away and blown
                <br>the sky away and all the leaves away,
                <br>and the trees stand.  I think i too have known
                <br>autumn too long

                <br>               (and what have you to say,
                <br>wind wind wind—did you love somebody
                <br>and have you the petal of somewhere in your heart
                <br>pinched from dumb summer?
                <br>                            O crazy daddy
                <br>of death dance cruelly for us and start

                <br>the last leaf whirling in the final brain
                <br>of air!)Let us as we have seen see
                <br>doom’s integration………a wind has blown the rain
                <br>
                <br>away and the leaves and the sky and the
                <br>trees stand:
                <br>            the trees stand.  The trees,
                <br>suddenly wait against the moon’s face.
            </p>

        </div>


        
    </main>
</template>

<script>
import Gallery from '@/components/Gallery.vue'
const {API_URL} = require('../settings.json')

export default {
    name: 'Generator',
    components: { Gallery },
    data() {
        return {
            first_line: "",
            poet: "Shakespeare",
            poem: "",
            avaible_poets: ["Shakespeare", "Ginsberg", "Cummings", "Lorem Ipsum"],
            input_id: null,
        }
    },
    methods: {
        selectPoet(poet){
            this.poet = poet
        },
        fetch_poem(){
            this.poem = ""
            fetch(`${API_URL}/api/generate/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "style": this.poet,
                    "first_line": this.first_line,
                })
            })
                .then(res => res.json())
                .then(data => ({text: this.poem, input: this.input_id} = data))
                .catch(err => console.log(err.message))
        },
        save_poem() {
            fetch(`${API_URL}/api/save/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "input": this.input_id,
                    "text": this.poem
                })
            })
                .catch(err => console.log(err.message))
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

    .poem {
        width: 40vw;
        height: 100%;
        margin: auto;
        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-content: center;
    }

    .highlight {
        background-color: lightseagreen;
    }
</style>