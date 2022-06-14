<template>
  <b-dropdown-item href="#" @click.prevent="logout()" class="text-decoration-none">Sign out</b-dropdown-item>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LogOut',
  methods: {
    ...mapActions(['logout'])
  },
}
</script>