<template>
    <nav class="navbar is-light is-fixed-top">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <figure class="image is-64x64 mx-4">
                    <img src="../assets/logo.png" style="max-height: 128px; max-width: 128px;">
                </figure>
                <h1 class="title mx-4">
                    BAIron
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
            </div>
        </div>

    </nav>
    <!-- <main>
        <div id="logo">
            <router-link to="/"><img src="../assets/logo.png" alt="" ></router-link>
        </div>
        <div>
            <h2> BAIron </h2>
        </div>
        <div id="nav">
            <router-link to="/">Home</router-link>
            <router-link to="/about">About</router-link>
            <router-link to="/generate">Generator</router-link>
            <router-link to="/poems">Poems</router-link>
        </div>
    </main> -->
</template>

<script>
export default {
    mounted() {
        const burgerIcon = document.querySelector('#burger')
        const navbarMenu = document.querySelector('#nav-links')
        const navbarItems = document.getElementsByClassName('navbar-item')


        burgerIcon.addEventListener('click', () => {
            navbarMenu.classList.toggle('is-active');
        });

        for(let navbarItem of navbarItems){
            console.log(navbarItem)
            navbarItem.addEventListener('click', () => {
                console.log("dupa")
                navbarMenu.classList.remove('is-active');
            })
        }


    }

}
</script>

<style scoped>
    img {
        border-radius: 25%;
    }
</style>