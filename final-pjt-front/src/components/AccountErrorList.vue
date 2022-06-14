<template>
  <div class="account-error-list">
    <div v-for="(errors,field) in authError" :key="field">
      <div v-for="(error, idx) in errors" :key="idx" class="error">{{ error }}</div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AccountErrorList',
  computed: {
    ...mapGetters(['authError'])
  },
}
</script>

<style>
  .error {
    height: 40px;
    line-height: 40px;
    color: white;
  }
</style>