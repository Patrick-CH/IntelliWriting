import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

let airouter = new Router({
  routes: [{
      path: '/',
      name: 'home',
      component: () => import('./views/Home.vue')
    },
    {
      path: '/news',
      name: 'news',
      component: () => import('./views/News.vue'),
    },
    {
      path: '/product',
      name: 'product',
      component: () => import('./views/Product.vue'),
    },
    {
      path: '/history',
      name: 'history',
      component: () => import('./views/History.vue')
    },
    {
      path: '/intro',
      name: 'intro',
      component: () => import('./views/GoIn.vue')
    },
    {
      path: '/users',
      name: 'users',
      component: () => import('./views/UserCenter.vue')
    },
    {
      path: '/contactus',
      name: 'contactus',
      component: () => import('./views/Download.vue')
    },
  ]
})

export default airouter