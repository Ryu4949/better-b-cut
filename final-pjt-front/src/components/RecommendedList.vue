<template>
<div>
  <div class="recommended-list mt-5 mb-1">
    <div>
      <div>
        <div class="container px-1 mb-5 w-100">
          <h1 class="p-3"> 추천 영화 </h1>
          <div class="p-3 container mr-1" v-if="recommendedList[0]">
            <div class="row">
              <!--onclick: 클릭시 해당 영화 검색으로 이동 (추후 변경)-->
              <div class="col ml-4">
                <router-link :to="`/movies/${recommendedList[0].id}/result`" class="text-decoration-none text-white">
                  <img class="main-poster img-size" :src="getImgUrl(recommendedList[0].poster_path)" alt="Image 1">
                </router-link>
              </div>
              <div class="col ml-4">
                <router-link :to="`/movies/${recommendedList[1].id}/result`" class="text-decoration-none text-white">
              
                  <img class="main-poster img-size" :src="getImgUrl(recommendedList[1].poster_path)" alt="Image 2">
                </router-link>
              </div>
              <div class="col ml-4">
                <router-link :to="`/movies/${recommendedList[2].id}/result`" class="text-decoration-none text-white">
                  <img class="main-poster img-size" :src="getImgUrl(recommendedList[2].poster_path)" alt="Image 3">
                </router-link>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  </div>  
  <ArticleList />
</div>
</template>
        <!-- 캐로셀 
        {{recommendedList}}
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner col-6 ">
            <div class="carousel-item active">
              <img :src="getImgUrl(recommendedList[0].poster_path)" alt="`${recommendedList[0].title}`" 
              class="d-block w-100">
            </div>



            <div class="carousel-item">
              <img :src="getImgUrl(recommendedList[1].poster_path)" alt="`${recommendedList[1].title}`" class="d-block w-100">
            </div>
            <div class="carousel-item">
              <img :src="getImgUrl(recommendedList[2].poster_path)" alt="`${recommendedList[2].title}`" class="d-block w-100">
            </div>
          </div>
          <div class="carousel-inner col-6 ">
            <div class="carousel-item active">
              <img :src="getImgUrl(recommendedList[0].poster_path)" alt="`${recommendedList[0].title}`" class="d-block w-100">
            </div>



            <div class="carousel-item">
              <img :src="getImgUrl(recommendedList[1].poster_path)" alt="`${recommendedList[1].title}`" class="d-block w-100">
            </div>
            <div class="carousel-item">
              <img :src="getImgUrl(recommendedList[2].poster_path)" alt="`${recommendedList[2].title}`" class="d-block w-100">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-target="#carouselExampleIndicators" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-target="#carouselExampleIndicators" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </button>
        </div>
        -->


        

<script>
import ArticleList from './ArticleList.vue'
import urls from '@/api/urls'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'RecommendedList',
  data() {
    return {
      recommendedList : [],
    }
  },
  components:{
    ArticleList
  },
  mounted() {
    axios({
      url: urls.movies.movieRecommendation(),
      method: 'get',
      headers: this.authHeader
    })
      .then(res => this.recommendedList = res.data)
      .catch(err => console.log(err))
  },
  computed: {
    ...mapGetters(['authHeader'])
  },
  methods: {
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
      return imgUrl
    },
  },
}
</script>

<style scoped>
.recommended-list {
  color: white;
  font-family: IM_Hyemin-Bold;
  text-align: center;
}
h1 {
    margin : 10px;
}
hr {
    background-color: black;
    margin-top: 10px;
    margin-bottom: 10px;
  }
.deco-container {
    width: 1400px; 
    margin: 0 auto; /* 가로로 중앙에 배치 */ 
    background-color: rgba(31, 31, 31, 0.315);
    border: none;
    border-radius: 20px;
    box-shadow: 0 9px 45px rgba(49, 49, 49, 0.6);
    opacity: 0.9;
    color : black;
  }
  div {
    font-family: IM_Hyemin-Bold;
    color : white;
  }
  .carousel-inner > .item > img {
    top: 0;
    left: 0;
    min-width: 1500px;
    min-height: 400px;
  } 
  .img-size {
    width: 350px;
    height: 450px;
    border-radius: 15px;
  }
  .col {
    padding : 0;
  }

</style>