import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleListView from '../views/ArticleListView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import NotFound404 from '../views/NotFound404.vue'
import ArticleDetailView from '../views/ArticleDetailView.vue'
import ArticleNewView from '../views/ArticleNewView.vue'
import ProfileView from '../views/ProfileView.vue'
import ArticleEditView from '../views/ArticleEditView.vue'
import SearchResultView from '../views/SearchResultView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'articleList',
    component: ArticleListView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/articles/:articlePk',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/movies/:moviePk/result',
    name: 'searchResult',
    component: SearchResultView,
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  // 등록되지 않은 URL은 404로 redirect시키도록 지정
  // 반드시 가장 하위에 위치
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
