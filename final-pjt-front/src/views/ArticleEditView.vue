<template>
  <div>
    <h1>edit Article</h1>
    <article-form v-if="isArticle" :article="article" action="edit"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleEditView',
  components: { ArticleForm },
  computed: {
    ...mapGetters(['article', 'isArticle'])
  },
  methods: {
    ...mapActions(['editArticle', 'fetchArticle'])
  },
  created() {
    const articlePk = this.$route.params.articlePk
    this.fetchArticle(articlePk)
  }
}
</script>

<style>

</style>