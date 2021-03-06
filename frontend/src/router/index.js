import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Poem from '../views/Poem.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/generate',
    name: 'Generate',
    component: () => import(/* webpackChunkName: "about" */ '../views/Generator.vue')
  },

  {
    path: '/generate-style-transfer',
    name: 'GenerateStyleTransfer',
    component: () => import(/* webpackChunkName: "about" */ '../views/Generator.vue')
  },
  {
    path: '/poems',
    name: 'Poems',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Poems.vue')
  },
  {
    path: '/poem/:id',
    name: 'Poem',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Poem,
    props: true,
  },
  {
    path: '/sentiment-analysis',
    name: 'SentimentAnalysis',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SentimentAnalysis.vue')
  },
  {
    path: '/turing-test',
    name: 'TuringTest',
    // route level code-splittin
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/TuringTest.vue')
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: () => import(/* webpackChunkName: "about" */ '../views/Statistics.vue')
  },
  {
    path: '/poetry-turing-test-statistics',
    name: 'PoetryTuringTestStatistics',
    component: () => import(/* webpackChunkName: "about" */ '../views/PoetryTuringTestStatistics.vue')
  },
  {
    path: '/ratings-statistics',
    name: 'RatingStatistics',
    component: () => import(/* webpackChunkName: "about" */ '../views/RatingStatistics.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
