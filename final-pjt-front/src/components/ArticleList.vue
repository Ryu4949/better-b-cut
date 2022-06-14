<template>
  <div class="articlelist">
    <article-search @search="search"></article-search>
    <div class="container bg-light mt-5 deco-container">
      
      <!-- 검색결과가 있을 때 보임 -->
      <div v-if="result[0]" class="accordion" role="tablist">
        <b-card id="card" v-for="(article, idx) in result" :key="idx" no-body class="mb-4">
          
          <b-card-header header-tag="header" class="p-0" role="tab">
            <div class="d-flex justify-content-end ml-5">
              <b-button id="accordion-btn" v-b-toggle="'accordion-' + idx" variant="secondary">
                [영화] {{article.movie["title"]}} - [게시글] {{ article.title }}
              </b-button>
              <div class="move-detail ml-auto">
                <div class="mr-0">
                  <button class="mb-3 bg-transparent">
                    <router-link :to="`/articles/${article.pk}`" class="text-decoration-none font-weight-normal">
                      <img src="@/assets/arrow.png" alt="link-img" height="40" width="40">      
                    </router-link>
                  </button>
                </div>
                
              </div>
            </div>
          
          </b-card-header>

          <b-collapse :id="'accordion-' + `${idx}`" visible accordion="my-accordion" role="tabpanel">
            <b-card-body>
              <p class="text-left ml-3">댓글   : {{ article.comment_count}} 개 </p>
              <p class="text-left ml-3">좋아요 : {{ article.like_count}} 개 </p>
              <p class="text-left ml-3">투표   : {{ article.vote_count}} 개 </p>
              
            </b-card-body>
          </b-collapse>
        </b-card>
      </div>

    
      <!-- 검색결과가 없을 때 보임 -->
      <div v-if="!result[0]" class="accordion" role="tablist">
        <b-card id="card" v-for="(article, idx) in articleList" :key="idx" no-body class="mb-4">
          <b-card-header header-tag="header" class="mt-3" role="tab">
            <div class="d-flex justify-content-end ml-5">
              <b-button class="bg-btn" id="accordion-btn" v-b-toggle="'accordion-' + idx" variant="secondary">
                <p class="text-left text-middle"> 
                  [영화] {{article.movie["title"]}} - [게시글] {{ article.title }}
                </p>
              </b-button>
              <div class="move-detail ml-auto">
                <div class="mr-0">
                  
                  <button class="mb-3 bg-transparent">
                    <router-link :to="`/articles/${article.pk}`" class="text-decoration-none font-weight-normal">
                      <img src="@/assets/arrow.png" alt="link-img" height="40" width="40">      
                    </router-link>
                  </button>
                </div>
              </div>
            </div>
          </b-card-header>

          <b-collapse :id="'accordion-' + `${idx}`" visible accordion="my-accordion" role="tabpanel" class="row">
            <b-card-body class="col">
              <p class="text-left ml-3">댓글   : {{ article.comment_count}} 개 </p>
              <p class="text-left ml-3">좋아요 : {{ article.like_count}} 개 </p>
              <p class="text-left ml-3">투표   : {{ article.vote_count}} 개 </p>
            </b-card-body>
          </b-collapse>
        </b-card>
      </div>

    </div>

      
  </div>


</template>

<script>
import axios from 'axios'
import urls from '@/api/urls'
import { mapActions, mapGetters } from 'vuex'
import ArticleSearch from '@/components/ArticleSearch.vue'

export default {
  name: 'ArticleList',
  data() {
    return {
      result: []
    }
  },
  components: {
    ArticleSearch,
  },
  created() {
    // like_count(좋아요), pk(생성순), vote_count(투표순)
    this.fetchArticleList('pk')
  },
  methods: {
    ...mapActions(['fetchArticleList']),
    search(searchKeyword) {
      axios({
        url: urls.articles.articleList() + '?search=' + searchKeyword,
        method: 'get',
        headers: this.authHeader
      })
        .then(res => this.result = res.data)
        .catch(err => console.log(err))
    }
  },
  computed: {
    ...mapGetters(['articleList'])
  }
}
</script>

<style>
#card {
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

#accordion-btn {
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  width: 800px;
  height: 45px;
}
#accordion- {
  height: 150%;
}
.block {
  height: 45vh;
}
div {
  font-family: IM_Hyemin-Bold;
  color : black;
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
.move-detail {
  width: 200px;
}
b-card-body {
  width: 800px;
  height: 200px;
}

h1 {
  height: 100px;
}
input {
  
  border-radius: 20px;
}
button {
  border: none;
}
.btn-border {
  border-radius: 20px;
}

</style>