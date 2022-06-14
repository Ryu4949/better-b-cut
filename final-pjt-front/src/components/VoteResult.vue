<template>
  <div class="vote-result">
    
      <div class="container bg-light p-3 mt-2">
        <div class="card mb-3" style="max-width: 800px;">
          <div class="row no-gutters">
            <div class="col-md-4">
              <!-- 영화 포스터 -->
              <img class="vote-img" :src="getImgUrl(article.movie.poster_path)" alt="movie-img">
            </div>


            <div class="col-md-8 movie-info mt-4">
              <div class="card-body">
                <!-- 영화 제목 -->
                <h5 class="card-title" :src="getImgUrl(article.movie.title)">{{article.movie.title}}</h5>

                <!--개봉일, 평점-->
                <div class="row movie-text-right">
                  <p class="card-text" :src="getImgUrl(article.movie.release_date)">
                    <small class="text-dark mr-2"> 개봉일 : 
                      <span class="badge badge-pill badge-dark">{{article.movie.release_date}}</span>
                    </small>
                  </p>
                  <p class="card-text" :src="getImgUrl(article.movie.vote_average)">
                    <small class="text-dark mr-2"> 평점 : 
                      <span class="badge badge-pill badge-dark">{{article.movie.vote_average}}</span>
                    </small>
                  </p>
          
                </div>


                <!--줄거리-->
                <div>
                  <p class="card-text" :src="getImgUrl(article.movie.overview)"> {{article.movie.overview}}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 투표 선택지-->
      <div class="alert alert-primary">
        <h3 class="h3-center"> 당신의 선택은? </h3> 
      </div>

      <form @submit.prevent="voteArticle">
        <div class="card-deck">
            <div class="card align-items-center">
              <!--이미지선택지-->
              <img class="vote-img-2" :src="'blob:http://localhost:8080/'+article.choices[0].img.substr(39)" alt="movie-img">
              <!--글 선택지-->
              <div class="card-body align-items-center">
                <h5 class="card-title">
                  <label class="text-dark">
                    <input type="radio" :value="choice1" v-model="choice">
                      {{article.choices[0].content}}
                  </label>
                </h5>
              </div>
            </div>
            <div class="card align-items-center">
              <!--이미지선택지-->
              <img class="vote-img-2" :src="'blob:http://localhost:8080/'+article.choices[1].img.substr(39)" alt="movie-img">
              <!--글 선택지-->
              <div class="card-body align-items-center">
                <h5 class="card-title">
                  <label class="text-dark">
                    <input type="radio" :value="choice2" v-model="choice">
                      {{article.choices[1].content}}
                  </label>
                </h5>
              </div>
            </div>
        </div>
      
      <!-- 투표 버튼-->
        <div class="alert alert-primary mt-3">
          <h3 class="h3-center"> 투표를 진행해주세요. </h3> 
        </div>
        
        <button class="mt-4 btn-sm btn-outline-primary btn-border"> Vote! </button>
      </form>
      <br><hr><br>
      
    <!-- 선택 결과 -->
    <div> {{article.result[0]}}, {{article.result[1]}} </div>
    <div class="progress">
      <div class="progress-bar" role="progressbar" :style="'width: ' + `${article.result[0]}` + '%'" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
      <div class="progress-bar bg-success" role="progressbar" :style="'width: ' + `${article.result[1]}` + '%'" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import axios from 'axios'
import urls from '@/api/urls'

export default {
  name: 'VoteResult',
  props: ['article',],
  data() {
    return {
      choice1: this.article.choices[0].pk,
      choice2: this.article.choices[1].pk,
      choice: '',
    }
  },
  methods: {
    ...mapActions(['fetchArticle']),
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
      return imgUrl
    },
    voteArticle() {
      console.log(this.article)
      axios({
        url: urls.articles.voteArticle(this.article.pk),
        method: 'post',
        headers: this.authHeader,
        data: { choice: this.choice }
      })
      .then((res) => {
        if (res.status === 201) {
        alert('투표가 정상적으로 완료되었습니다!')
        this.fetchArticle(this.article.pk)
        } else { alert('이미 투표 하셨습니다!')}
        })
      .catch(err => console.log(err))
    }
  },
  computed: {
    ...mapGetters(['authHeader'])
  },
  created() {
    this.choice = ''
  }
}
</script>

<style scoped>

label {
  color: black;
}
.vote-result {
  color: black;
}
.vote-img {
    margin: 40px;
    width: 190px;
    align-content: center;
  }
.vote-img-2 {
  padding: 30px;
  width: 300px;
  height: 300px;
  justify-content : center;
  align-content: center;
}
.movie-info {
  text-align: left;
}
.movie-text-right {
  justify-content : right;
  margin-right: 10px;
}
.btn-border {
  border-radius: 20px;
}
.h3-center {
  text-align: center;
}
</style>