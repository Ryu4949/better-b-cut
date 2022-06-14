<template>
  <div class="search-result-view container">
    <div v-if="!articles[0]">
      <h1 class="text-white">해당 영화와 관련된 게시글은</h1>
      <h1 class="text-white">존재하지 않습니다</h1>
      <h1 class="text-white">첫번째 게시글을 작성해주세요</h1>
    </div>

    <div v-if="articles[0]">
      <div class="block"></div>
      <h1 class="neon text-center"> {{ articles[0].movie.title }}에 대한 게시글들</h1>
      <button @click="sortVotecount" class="btn btn-primary">투표순</button>
      <button @click="sortCommentcount" class="btn btn-primary">댓글순</button>
      <button @click="sortLikecount" class="btn btn-primary">좋아요순</button>
      <button @click="sortPk" class="btn btn-primary">최신순</button>
      <b-list-group>
        <b-list-group-item class="d-flex justify-content-between align-items-center" v-for="(article, idx) in articles" :key="idx">
          <router-link  :to="`/articles/${article.pk}`" class="text-decoration-none font-weight-normal">
          {{ article.title }}
          </router-link>
          <span>투표수 :<b-badge variant="primary" pill style="color: white">{{ article.vote_count }}</b-badge></span>
          <span>좋아요 :<b-badge variant="primary" pill style="color: white">{{ article.like_count }}</b-badge></span>
          <span>댓글수 :<b-badge variant="primary" pill style="color: white">{{ article.comment_count }}</b-badge></span>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import urls from '@/api/urls'
import axios from 'axios'

export default {
  name: 'SearchResult',
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      articles: ''
    }
  },
  methods: {
    getArticles: function (moviePk) {
      axios({
        url: urls.movies.searchResult(moviePk),
        method: 'get',
        headers: this.authHeader
      })
      .then(res => {
        this.articles = res.data
      })
    },
    sortVotecount() {
      this.articles.sort(function(a, b) {
        return b.vote_count - a.vote_count
      })
    },
    sortCommentcount() {
      this.articles.sort(function(a, b) {
        return b.comment_count - a.comment_count
      })
    },
    sortLikecount() {
      this.articles.sort(function(a, b) {
        return b.like_count - a.like_count
      })
    },
    sortPk() {
      this.articles.sort(function(a, b) {
        return b.pk - a.pk
      })
    }
  },
  created() {
    console.log(this.moviePk)
    this.getArticles(this.moviePk)
  }

}
</script>

<style scoped>
  .search-result-view {
    color: white;
  }
  span {
    color: black;
  }
  .neon {
  color: #fff;
  text-shadow:
    0 0 5px #fff,
    0 0 10px #fff,
    0 0 20px #fff,
    0 0 40px #0ff,
    0 0 150px #0ff;
}

.block {
  height:100px;
}
</style>