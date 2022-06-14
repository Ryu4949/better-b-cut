<template>
  <div class="commentform mt-5">
    <div class="block">
      <div class="container p-3 deco-container">
        <form @submit.prevent="createComment(article.pk, commentData)">
          <div class="container d-flex justify-content-start  ml-2">
            <label for="comment"></label>
            <input class="mr-3" type="text" placeholder=" 댓글을 작성해주세요."
            id=comment v-model="commentData.content" />
            <button class="btn-sm btn-outline-primary btn-border" >댓글쓰기</button>
          </div>
        </form>
      </div> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import urls from '@/api/urls'
import { mapGetters, mapActions } from 'vuex'

export default {
name: 'CommentForm',
props: ['article',],
data() {
  return {
    commentData: {
      "content": ""
    }
  }
},
methods: {
  ...mapActions(['fetchCommentList']),
  createComment(articlePk, commentData) {
    axios({
      url: urls.articles.commentNew(articlePk),
      method: 'post',
      headers: this.authHeader,
      data: commentData
    })
      .then((res) => {
        if (res.data.now_vote === true) {
          this.fetchCommentList(articlePk)
          } else { alert('투표를 하신 분만 댓글을 작성할 수 있습니다!')}
        })
      .then(() => this.commentData.content = '')
      .catch(err => console.log(err))
  }
},
computed: {
  ...mapGetters(['authHeader']),
},
}
</script>

<style scoped>
  .block {
    height: 12vh;
  }
  div {
    font-family: IM_Hyemin-Bold;
    color : white;
  }
  hr {
    background-color: rgb(255, 255, 255);
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
    color : rgb(255, 255, 255);
  }
  .commenttext {
    color : white;
  }
  .btn-border {
    border-radius: 20px;
    justify-content : right;
  }
  input {
    display: block;
    width: 650px;
    border-bottom: 1px solid black;
    border-radius: 20px;
    border : none;
  }
</style>