<template>
  <div class="commentlist">
    <div class="container bg-light p-3 mt-3 deco-container">
      <h1 class="text-dark text-left text-white">Comments</h1>
      <hr class="mb-2">
      <div v-if="commentList">
        <div v-for="(comment, idx) in commentList" :key="-idx" class="text-dark">
          <div class="row d-flex justify-content-between">

            
            <div class="row d-flex">
              <!-- 댓글 내용-->
              <div class="mr-3">
                <p class="text-left ml-3"> {{idx+1}} 번 댓글 : {{ comment.content }}</p>
                <p class="text-left ml-3" 
                v-if="comment==='아직 댓글이 없습니다. 댓글을 달아주세요.'">{{ comment }}</p>
              </div>
              
              <!-- 댓글 좋아요 -->
              <div class="mr-3">
                <button class="btn-sm btn-outline-primary btn-border" 
                v-if="comment.now_like" @click.prevent="likeComment(article.pk, comment.pk)">
                  좋아요 취소
                </button>
                <button class="btn-sm btn-outline-primary btn-border"
                v-else-if="comment!='아직 댓글이 없습니다.'" @click.prevent="likeComment(article.pk, comment.pk)">
                  좋아요
                </button>
              </div>
            </div>

            <!-- 댓글 삭제 -->
            <div class="mr-3">
              <button class="btn-sm btn-outline-primary btn-border" 
              @click.prevent="deleteComment(article.pk, comment.pk)" v-if="comment!='아직 댓글이 없습니다.'">Delete</button>
            </div>
          </div>          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import urls from '@/api/urls'
import axios from 'axios'

export default {
  name: 'CommentList',
  computed: {
    ...mapGetters(['commentList', 'article', 'authHeader']),
  },
    
  methods: {
    ...mapActions(['fetchCommentList',]),
    deleteComment: function (articlePk, commentPk) {
      axios({
        url: urls.articles.commentDetail(articlePk, commentPk),
        method: 'delete',
        headers: this.authHeader
      })
      .then(() => {
        this.fetchCommentList(articlePk)
        alert('댓글이 성공적으로 삭제되었습니다.')
      })
      .catch(err => console.log(err))
    },
    likeComment: function ( articlePk, commentPk) {
      axios({
        url: urls.articles.commentLike(articlePk, commentPk),
        method: 'post',
        headers: this.authHeader
      })
      .then(res => {
        console.log(res)
        this.fetchCommentList(this.article.pk)
      })
    }
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
  .text-white {
    color : white;
  }
  .btn-border {
    border-radius: 20px;
  }
</style>