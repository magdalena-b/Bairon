<template>
    <main>
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
    </main>
</template>

<script>
export default {

}
</script>

<style scoped>
    main {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        height: 5vh;
        padding: 30px;
        background-color: #eee;
    }
    #logo {
        height: 100%;
    }
    img {
        max-height: 100%;
        border-radius: 10%;
    }
</style>