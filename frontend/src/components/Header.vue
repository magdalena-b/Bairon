<template>
    <div>
        
        <!-- placeholder -->
        <nav class="navbar" style="position: relative; z-index: -1;">
            <div class="navbar-brand">
                <div class="navbar-item">
                    <figure class="image is-64x64 mx-4">
                        <img src="../assets/logo.png" style="max-height: 128px; max-width: 128px;">
                    </figure>
                    <h1 class="title mx-4">
                        BAIron
                    </h1>
                </div>
            </div>
        </nav>
        <!-- end of placeh0lder -->

        <nav class="navbar is-light is-fixed-top px-5">
            <div class="navbar-brand">
                <router-link to="/" class="navbar-item">
                    <figure class="image is-64x64 mx-4">
                        <img src="../assets/logo.png" style="max-height: 128px; max-width: 128px;">
                    </figure>
                    <h1 class="title mx-4">
                        Bairon
                    </h1>
                </router-link>
                <a class="navbar-burger" id="burger">
                    <span></span>
                    <span></span>
                    <span></span>
                </a>
            </div>
            <div class="navbar-menu" id="nav-links">
                <div class="navbar-end">
                    <router-link class="navbar-item" to="/">Home</router-link>
                    <router-link class="navbar-item" to="/about">About</router-link>
                    <router-link class="navbar-item" to="/generate">Generator</router-link>
                    <router-link class="navbar-item" to="/poems">Poems</router-link>
                    <!-- <router-link class="navbar-item" to="/sentimentanalysis">Sentiment Analysis</router-link> -->
                    <router-link class="navbar-item" to="/turing-test">Vote!</router-link>
                    <!-- <router-link class="navbar-item" to="/statistics">Statistics</router-link> -->
                    <a class="navbar is-light" role="navigation" aria-label="dropdown navigation">
                        <div class="navbar-item has-dropdown is-hoverable">
                            <div class="navbar-link">
                                Statistics
                            </div>
                            <div class="navbar-dropdown is-right">
                                <router-link class="navbar-item" to="/statistics">Word Count</router-link>
                                <router-link class="navbar-item" to="/sentimentanalysis">Emotion Analysis</router-link>
                                <router-link class="navbar-item" to="/poetry-turing-test-statistics">Poetry Turing Test Statistics</router-link>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    mounted() {
        const burgerIcon = document.querySelector('#burger')
        const navbarMenu = document.querySelector('#nav-links')

        document.addEventListener('click', function(e){   
        if (navbarMenu.contains(e.target)){
            navbarMenu.classList.add('is-active')
        }
        else if(burgerIcon.contains(e.target)){
            navbarMenu.classList.toggle('is-active')
        }
        else{
            navbarMenu.classList.remove('is-active')
        }
        })
    }

}
</script>

<style scoped>
    img {
        border-radius: 25%;
    }

    #burger {
        margin-top: auto;
        margin-bottom: auto;
    }
</style>
