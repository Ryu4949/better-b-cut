<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <!-- navbar 로고 -->
      <b-navbar-brand>
        <router-link :to="{ name: 'articleList'}" class="text-decoration-none"><logo-icon></logo-icon></router-link>
      </b-navbar-brand>

      <b-navbar-nav>
          <b-nav-form class="btn-border" @submit.prevent="[search(), $bvToast.show('router-link-toast')]">
            <b-form-input size="sm" class="mr-sm-2" v-model="searchKeyword" placeholder="영화를 검색해주세요" required></b-form-input>
            <img class="img-button" src="@/assets/icons8-search-50.png" alt="search-icon" @click.prevent="[search(), $bvToast.show('router-link-toast')]" width="35" height="35" />
          </b-nav-form>
      </b-navbar-nav>

      <!-- navbar 우측메뉴 -->
      <b-navbar-nav class="ml-auto">
        <!-- login 안되어 있을 때 노출 -->
        <b-nav-item v-if="!isLoggedIn">
          <router-link :to="{ name: 'login'}" class="text-decoration-none">Login</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn">
          <router-link :to="{ name: 'signup'}" class="text-decoration-none">Sign up</router-link>
        </b-nav-item>
        <!-- login 되어 있을 때 노출 -->
        <b-nav-item>
          <router-link :to="{ name: 'articleNew'}" v-if="isLoggedIn" class="text-decoration-none">ArticleNew</router-link>
        </b-nav-item>

        <b-nav-item-dropdown v-if="isLoggedIn" class="dropdown" right no-caret>
          <template #button-content>
            <img src="@/assets/icons8-male-user-64.png" alt="profile-img" height="25" width="25">
          </template>
          <b-dropdown-item :to="`/profile/${username}`" class=" text-decoration-none text-body font-weight-normal">Profile
          </b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider>
          <log-out></log-out>
        </b-nav-item-dropdown>

      </b-navbar-nav>
    </b-navbar>
    <b-toast id="router-link-toast" title="검색 결과" class="toast-position" static no-auto-hide>
      <router-link v-for="(movie, idx) in result" :key="idx" :to="`/movies/${movie.id}/result`" class="text-decoration-none">
      <img :src="getImgUrl(movie.poster_path)" alt="movie-img" width="20" height="20">
      {{ movie.title }}
      <br>
      </router-link>
    </b-toast>
  </div>
</template>

<script>
import axios from 'axios'
import urls from '@/api/urls'
import { mapGetters } from 'vuex'
import LogoIcon from '@/components/LogoIcon.vue'
import LogOut from '@/components/LogOut.vue'

export default {
  name: 'NavBar',
  data() {
    return {
      searchKeyword: '',
      result: [],
    }
  },
  methods: {
    search () {
      axios({
        url: urls.movies.movieList() + '?search=' + this.searchKeyword,
        method: 'get',
        headers: this.authHeader
      })
        .then(res => {
          this.result = res.data
          this.searchKeyword = ''
          })
        .catch(err => console.log(err))
    },
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
      return imgUrl
    },
  },
  components: {
    LogoIcon,
    LogOut,
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', 'authHeader']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'Anonymous'
    }
  }
}
</script>

<style scoped> 
  nav {
  padding: 2px;
  }

  nav a {
    font-weight: bold;
    color: gainsboro;
  }
  .btn-border {
    border-radius: 20px;
  }

  .img-button {
    cursor: pointer;
  }
</style>