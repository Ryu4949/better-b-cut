<template>
  <div class="ArticleNewView">
    <div class="block"></div>
    <!-- 영화 타이틀로 검색 -->
    <div class="container bg-light deco-container p-5">
      <div class="d-flex flex-column align-items-center mb-3">
        <h1 class="text-dark text-center mb-5">CREATE ARTICLE</h1>
        <!-- 검색창 -->
        <p>어떤 영화에 대한 글인지 선택하세요</p>
        <form @submit.prevent="search()" class="text-center">
          <input id="search-movie-input" type="text" v-model="searchKeyword" placeholder="Enter MovieTitle" required />
          <img class="img-button" src="@/assets/icons8-search-60.png" alt="search-icon" @click.prevent="search()" width="30" height="30" />
          <img class="img-button" src="@/assets/icons8-refresh-60.png" alt="refersh-icon" @click.prevent="refresh()" width="30" height="30" />
        </form>
        <!-- 검색결과 -->
        <div class="search-result">
          <ul class="d-flex flex-column p-0">
            <li 
              v-for="(movie, idx) in result" 
              :key="idx" 
              @click.prevent="selectMovie(movie.id, movie.title)"
              class="d-flex justify-content-between">
              <div>
                <img :src="getImgUrl(movie.poster_path)" alt="movie-img" width="20" height="20">
                {{ movie.title }}
              </div>
              <div>click!</div>
            </li>
          </ul>
        </div>
      </div>

      <form @submit.prevent="articleNew(articleData)" >
        <!-- movieId 받기 -->
        <div class="text-center hidden">
          <br>
          <label for="movie-pk">movie pk: </label>
          <input v-model="articleData.movie_pk" type="number" id="movie-pk" />
        </div>
        <!-- 게시글 제목 입력 -->
        <div class="text-center mb-5">
          <label for="title">title: </label>
          <input v-model="articleData.title" type="text" id="title" />
        </div>
        <!-- 선택 1, 2 -->
        <div class="d-flex justify-content-around">
          <div>
            <h2 class="text-center">A 선택</h2>
            <div class="img-box mb-3 d-flex justify-content-center align-items-center" @click.prevent="onClick1()">
              <div v-if="articleData.choices[0].img === ''">A 선택에 관한 이미지를 넣어보세요</div>
              <img v-if="articleData.choices[0].img !== ''" :src="articleData.choices[0].img" :alt="articleData.choices[0].img" width="290" height="290">
            </div>
            <div class="hidden">
              <label for="choice1-img" class="form-label">choice1 img: </label>
              <input 
                id="choice1-img"
                type="file" 
                accept="image/*" 
                @change="changeImage1($event.target)">
            </div>
            <div>
              <textarea 
                class="input-box" 
                v-model="articleData.choices[0].content" 
                type="text" id="choice1-content" 
                cols="30" 
                rows="3"
                placeholder= "A 선택에 대한 설명을 작성해주세요"
                ></textarea>
            </div>
          </div>
      
          <div>
            <h2 class="text-center">B 선택</h2>
            <div class="img-box mb-3 d-flex justify-content-center align-items-center" @click.prevent="onClick2()">
              <div v-if="articleData.choices[1].img === ''">B 선택에 관한 이미지를 넣어보세요</div>
              <img v-if="articleData.choices[1].img !== ''" :src="articleData.choices[1].img" :alt="articleData.choices[1].img" width="290" height="290">
            </div>
            <div class="hidden">
              <label for="choice2-img" class="form-label">choice2 img: </label>
              <input 
                id="choice2-img"
                type="file" 
                accept="image/*" 
                @change="changeImage2($event.target)">
            </div>
            <div>
              <textarea 
                class="input-box" 
                v-model="articleData.choices[1].content" 
                type="text" id="choice2-content" 
                cols="30" 
                rows="3"
                placeholder= "B 선택에 대한 설명을 작성해주세요"
                ></textarea>
            </div>
          </div>
        </div>

        <div class="text-right mt-3">
          <button class="submit-button">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import urls from '@/api/urls'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleNewView',
  data() {
    return {
      searchKeyword: '',
      result: [],
      articleData: {
        "movie_pk": "",
        "title": "",
        "choices": [
          {
              "content": "",
              "img": ""
          },
          {
              "content": "",
              "img": ""
          }
        ]
      }
    } 
  },
  methods: {
    ...mapActions(['articleNew']),
    search () {
      axios({
        url: urls.movies.movieList() + '?search=' + this.searchKeyword,
        method: 'get',
        headers: this.authHeader
      })
        .then(res => this.result = res.data)
        .catch(err => console.error(err))
    },
    getImgUrl: function (url) {
      const imgUrl = `https://image.tmdb.org/t/p/w185${url}`
      return imgUrl
    },
    selectMovie(id, title) {
      const input = document.querySelector('#search-movie-input')

      this.articleData.movie_pk = id
      this.result = []
      this.searchKeyword = title
      input.setAttribute('disabled', 'disabled')
    },
    refresh() {
      const input = document.querySelector('#search-movie-input')
      this.searchKeyword = ''
      input.removeAttribute('disabled')
    },
    changeImage1(target) {
      let file = target.files[0]
      this.articleData.choices[0].img = URL.createObjectURL(file)
    },
    changeImage2(target) {
      let file = target.files[0]
      this.articleData.choices[1].img = URL.createObjectURL(file)
    },
    onClick1() {
      const inputImage1 = document.querySelector('#choice1-img')
      inputImage1.click()
    },
    onClick2() {
      const inputImage2 = document.querySelector('#choice2-img')
      inputImage2.click()
    },
  },
  computed: {
    ...mapGetters(['authHeader'])
  }
}
</script>

<style scoped>
.ArticleNewView {
  font-family: IM_Hyemin-Bold;
}

.deco-container {
  margin: 0 auto; /* 가로로 중앙에 배치 */ 
  background-color: rgba(151, 151, 151, 0.315);
  border: none;
  border-radius: 20px;
  box-shadow: 0 9px 45px rgba(49, 49, 49, 0.6);
  opacity: 0.9;
}

.img-box {
  width: 300px;
  height: 300px;
  border: solid;
  border-radius: 7px;
}

.input-box{
  width: 300px;
  height: 100px;
  font-size: 15px;
  border: 0;
  border-radius: 15px;
  outline: none;
  padding-top: 7px;
  padding-left: 15px;
  padding-right:10px;
  background-color: rgb(233, 233, 233);
}

.hidden {
  display: none;
}

.img-button {
  cursor: pointer;
}

#search-movie-input {
  width: 300px;
}

.block {
  height: 12vh;
}

.search-result {
  width: 360px;
}

.submit-button {
  border: none;
  width: 100px;
  height: 35px;
  border-radius: 15px;
  background-color: rgb(27, 17, 71);
  color: white;
}
</style>