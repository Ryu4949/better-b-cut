<template>
  <div class="profile-view mt-3">
    <div class="block mt-3">
      <div class="container p-3 mt-5 deco-container">
        <div class="d-flex p-center mt-3 mr-3">
          <img class="ml-2"
          src="@/assets/icons8-male-user-96.png" alt="profile-img">
          <h1 class="d-flex mt-4 mr-3"> {{username}} 님의 페이지 </h1>
          <br class="text-dark">
        </div>
        <hr class="mb-2">


        <!-- 내가 쓴 게시글 -->
        <div class="container bg-light d-flex justify-content-left mt-5 btn-border">
          <div class="row d-flex align-items-center"> 
            <div class="d-flex p-center mt-3 ml-3">
              <h3 class="mt-3">내가 쓴 게시글</h3>
              <div class="d-flex p-center mt-3 ml-3 ">
                <p v-if="!myArticles[0]">게시글이 없습니다</p>
                <div v-if="myArticles[0]">
                  <p> 총 [{{countMyArticles}}] 개의 게시글이 있습니다.</p>
                  <hr class="mb-3">
                  <div class="d-flex" v-for="(myArticle, idx) in myArticles" :key="idx">
                    <p>{{myArticle.movie_title}} - [{{ myArticle.title}}] 글을 썼습니다. </p>
                    <button class="btn-sm btn-outline-primary btn-border ml-2 mb-3">
                      <router-link 
                        :to="{ name: 'articleDetail', params: { articlePk: `${myArticle.pk}` }}" 
                        class="text-decoration-none"
                        > 이동 </router-link>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 내가 쓴 댓글 -->
        <div class="container bg-light d-flex justify-content-left mt-5 btn-border">
          <div class="row d-flex align-items-center"> 
            <div class="d-flex p-center mt-3 ml-3">
              <h3 class="mt-3">내가 쓴 댓글</h3>
              

              <div class="d-flex p-center mt-3 ml-5">
                
                <p v-if="!myComments[0]">댓글이 없습니다</p>
                <div v-if="myComments[0]">
                  <p> 총 [{{ myComments.length }}] 개의 댓글이 있습니다.</p>
                  <hr class="mb-3">
                  <div v-for="(myComment, idx) in myComments" :key="idx">
                    
                    <p> [{{ myComment.content }}] 댓글을 달았습니다. </p>
                  
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import axios from 'axios'
import urls from '@/api/urls'

export default {
  name: 'ProfileView',
  data() {
    return {
      myArticles: [],
      myComments: [],
    }
  },
  computed: {
    ...mapGetters(['authHeader']),
    username() {
      return this.$route.params.username
    },
    countMyArticles() {
      return this.myArticles.length
    },
    countMyCommments() {
      return this.myCommments.length
    },
  },
  methods: {
    ...mapActions(['fetchProfile']),
    fetchMyArticles(username) {
      axios({
        url: urls.accounts.myArticles(username),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => this.myArticles = res.data)
      .catch(err => console.log(err))
    },
    fetchMyComments(username) {
      axios({
        url: urls.accounts.myComments(username),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => this.myComments = res.data)
      .catch(err => console.log(err))
    }
  },
  mounted() {
    this.fetchProfile(this.username)
    this.fetchMyArticles(this.username)
    this.fetchMyComments(this.username)
  }


}
</script>

<style scoped>
  .block {
    height: 12vh;
  }
  div {
    font-family: IM_Hyemin-Bold;
    color : black;
  }
  .profile-view {
    color: rgb(0, 0, 0);
  }
  h1 {
    margin : 10px;
    text-align: left;
  }
  hr {
    background-color: black;
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .deco-container {
    width: 800px; 
    margin: 0 auto; /* 가로로 중앙에 배치 */ 
    background-color: rgba(151, 151, 151, 0.315);
    border: none;
    border-radius: 20px;
    box-shadow: 0 9px 45px rgba(49, 49, 49, 0.6);
    opacity: 0.9;
    color : black;
  }
  img {
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .btn-border {
    border-radius: 20px;
  }
</style>