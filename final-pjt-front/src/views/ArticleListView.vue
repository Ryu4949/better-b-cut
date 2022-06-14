<template>
  <div class="article-list">
    <div class="block">
      <div>
        <recommended-list></recommended-list>
      </div>
      <!--<div>
        <h1 class="text-center"></h1>
      </div>
      <div>
        <article-list></article-list>
      </div> -->
    </div>
  </div>
</template>

<script>
import RecommendedList from '@/components/RecommendedList.vue'
//import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleListView',
  components: {
    RecommendedList,
    //ArticleList,
  }
}
</script>

<style scoped>
  h1 {
    font-family: IM_Hyemin-Bold;
    color : white;
  }
  /* .block {
    height: 12vh;
  } */
  div {
    font-family: IM_Hyemin-Bold;
    color : black;
  }
</style>