<template>
    <div class="container d-flex justify-content-center">
      <div class="neon"> better </div>
      <div class="flux"> b-cut </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  @font-face {
    font-family: neon;
    src: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/707108/neon.ttf);
  }

  .container {
    display: inline-block;
    text-align: center;
    vertical-align: middle;
  }

  .neon {
    font-family: neon;
    font-weight: 400;
    color: #FED128;
    font-size: 24px;
    line-height: 50px;
    /* text-shadow: 0 0 2vh #FED128; */
  }

  .flux {
    font-family: neon;
    font-weight: 400;
    color: #28D7FE;
    font-size: 24px;
    line-height: 50px;
    /* text-shadow: 0 0 2vh #28D7FE; */
  }
  
</style>