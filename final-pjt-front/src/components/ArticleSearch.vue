<template>
  <div class="text-right">
    <div class="container p-3 mt-3 deco-container mb-5">
      <form @submit.prevent="onSubmit">
        <div class="d-flex justify-content-end">
          <div class="mr-2">
            <input type="text" v-model="searchKeyword" placeholder="게시글을 검색해주세요." required />
          </div>
          <div class="">
            <button class="btn-sm btn-outline-primary btn-border">
              search
            </button>
          </div>
        </div>
        
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'ArticleSearch',
  data() {
    return { 
      searchKeyword: '',
      result: [],
    }
  },
  methods: {
    onSubmit () {
      this.$emit('search', this.searchKeyword)
    },
  },
  computed: {
    ...mapGetters(['authHeader'])
  }
}
</script>

<style scoped>
  .block {
    height: 12vh;
  }
  input {
    font-family: IM_Hyemin-Bold;
    color : black;
    border-radius: 20px;
    width: 680px;
    padding: 7px;
  }

  .btn-border {
    font-family: IM_Hyemin-Bold;
    border-radius: 20px;
    height: 42px;
    width: 80px;
  }
  .deco-container {
    width: 800px; 
    margin: 0 auto; /* 가로로 중앙에 배치 */ 
    background-color: rgba(141, 141, 141, 0.315);
    border: none;
    border-radius: 20px;
    box-shadow: 0 9px 45px rgba(49, 49, 49, 0.6);
    opacity: 0.9;
    color : black;
  }
</style>