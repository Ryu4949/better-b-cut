<template>
  <div class="articledetail mt-3">
    <div class="block"></div>

    <div class="container bg-light p-3 deco-container">
      <h1 class="text-dark text-left">{{article.title}}</h1>
      <hr class="mb-2">
      <br>
      <!-- vote (voteresult)-->
      <div>
        <vote-result v-if="isArticle" :article="article"></vote-result>
      </div>
      
      <br><br><br><br><br>




      <!-- 좋아요 -->
      <div class="container bg-light mt-2 align-items-center">
        <div class="row d-flex align-items-center"> 
          <div class="d-flex p-center mt-3 mr-3">
            <p> 이 게시물이 마음에 드시나요? </p>
          </div>

          <div class="mr-2">
            <!-- <router-link class="text-decoration-none">Edit</router-link> -->

            <!--- 좋아요 하트 색 변경 -->
            <p class="p-center mt-3"
            v-if="article.now_like"> 
              {{ article.like_count }}
              <i class="fa fa-heart color-red"></i> 명이 좋아합니다. 
            </p>
            <p class="p-center mt-3" 
            v-else> 
              {{ article.like_count }}
              <i class="fa fa-heart"></i> 명이 좋아합니다. 
            </p>
          </div>
          
          <div>
            <button class="btn-sm btn-outline-primary btn-border" 
            v-if="article.now_like" @click.prevent="likeArticle(article.pk)">
              좋아요 취소
            </button>
            <button class="btn-sm btn-outline-primary btn-border"
            v-else @click.prevent="likeArticle(article.pk)">
              좋아요
            </button>
          </div>
          
        </div>

        <!--수정/삭제 버튼-->
        <div class="container bg-light d-flex justify-content-end mt-5">
          <button class="mt-4 btn-sm btn-outline-primary btn-border mr-" 
          @click.prevent="moveEditpage">
            Edit
          </button>
        
          <button class="mt-4 btn-sm btn-outline-primary btn-border" 
          @click.prevent="deleteArticle(article.pk)">
            Delete
          </button>
        </div>
      </div>
    </div>

    <!--댓글-->
    <div>
      <comment-form :article="article"></comment-form>
      <comment-list></comment-list>
    </div>
  </div>
</template>

<script>
import urls from '@/api/urls'
import axios from 'axios'
import router from '@/router'
import { mapGetters, mapActions } from 'vuex'
import VoteResult from '@/components/VoteResult.vue'
import CommentList from '@/components/CommentList.vue'
import CommentForm from '@/components/CommentForm.vue'

export default {
  name: 'ArticleDetailView',
  components: {
    VoteResult,
    CommentList,
    CommentForm,
  },
  methods: {
    ...mapActions(['fetchCommentList', 'fetchArticle']),
    deleteArticle: function (pk) {
      axios({
        url: urls.articles.articleDetail(pk),
        method: 'delete',
        headers: this.authHeader
      })
        .then(res => {
          console.log(res)
          alert(this.article.title + ' 이(가) 성공적으로 삭제되었습니다')
          router.push({name: 'articleList'})
          })
        .catch(err => console.log(err))
    },
    moveEditpage() {
      if (this.article.vote_count === 0) {
        router.push({ name: 'articleEdit', params: { articlePk: this.article.pk } })
        } else {
          alert('진행 중인 투표는 수정할 수 없습니다!')
        }
    },
    likeArticle: function(pk) {
      axios({
        url: urls.articles.articleLike(pk),
        method: 'post',
        headers: this.authHeader
      })
      .then(res => {
        console.log(res)
        this.fetchArticle(this.article.pk)
      })
      .catch(err => console.log(err))
    }
  },
  computed: {
    articlePk() {
      return this.$route.params.articlePk
    },
    ...mapGetters(['authHeader', 'article', 'isArticle']),
  },
  created() {
    this.fetchArticle(this.articlePk)
    this.fetchCommentList(this.articlePk)
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
  .articledetail {
    text-align: center;
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
  .movie-text-right {
    margin: 0 auto; 
    justify-content : right;
  }
  .color-red {
    color : red;
  }
  .p-center {
    text-align: center;
  }
</style>