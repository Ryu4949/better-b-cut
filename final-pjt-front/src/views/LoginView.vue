<template>
  <div class="login">
    <div class="block"></div>
    <logo-icon class="logo-in-login"></logo-icon>

    <div class="container bg-light p-3 mt-2 deco-container">
      <h1 class="text-align:right;">Login</h1>
      <hr class="mb-2">
      <!--로그인 폼-->
      <b-form class="login-form" @submit.prevent="login(credentials)">
        <div class="container">
          <div class="d-flex row align-content-center my-3">
            <div class="col-3">
              <label for="username" class="text-dark mt-3" >Username</label>
            </div>
            <div class="col-9">
              <b-form-input v-model="credentials.username" type="text"
                placeholder="Enter Username" id="username" required></b-form-input>
            </div>
          </div>

          <div class="d-flex row align-content-center my-3 ">
            <div class="col-3">
              <label for="password" class="text-dark mt-3" >Password</label>
            </div>
            <div class="col-9">
              <b-form-input v-model="credentials.password" type="password" 
              placeholder="Enter password" id="password"></b-form-input>
            </div>
            
          </div>
          
          <b-button type="submit" class="mt-4 btn btn-default">Login</b-button>
        </div>
      </b-form>
      
      <!--소셜 로그인-->
      <div class="container btn-box align-middle d-flex align-content-center">
        <div>
          <b-button type="button" class="row nbtn mt-4 btn btn-default">Naver Login</b-button>
        </div>
        <div>
          <b-button type="button" class="row gbtn mt-4 btn btn-default">Google Login</b-button>
        </div>
      </div>
    </div>
    <account-error-list></account-error-list>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import LogoIcon from '@/components/LogoIcon.vue'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
      LogoIcon,
      AccountErrorList,
    },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login', 'removeErrorMsg'])
  },
  // 페이지를 떠날 때, 에러메시지 제거
  beforeRouteLeave(to, from, next) {
    this.removeErrorMsg()
    next()
  }
}
</script>

<style scoped>
  div {
    font-family: IM_Hyemin-Bold;
  }

  .login {
    text-align: center;
  }

  .deco-container {
    width: 450px; 
    margin: 0 auto; /* 가로로 중앙에 배치 */ 
    background-color: rgba(151, 151, 151, 0.315);
    border: none;
    border-radius: 20px;
    box-shadow: 0 5px 45px rgba(49, 49, 49, 0.6);
    opacity: 0.9;
  }
  hr {
    background-color: black;
  }
  h1 {
    color : black;
  }
  input {
    border-radius: 10px;
    border : none;
    margin-top :10px;
  }
  input :after {
    display: block;
    width: 20px;
    border-bottom: 1px solid black;
  }
  .btn-box {
    display: flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: center;
    align-content: center;
  }
  .btn-default {
    width: 150px;
    margin-top :10px;
    background-color: navy;
    color:white;
    border:none;
  }
  .nbtn {
    background-color: #03C75A;
    
  }
  
  .gbtn {
    background-color: #E24939;
  
  }
  .block {
    height: 12vh;
    border:none;
  }

  .login-form {
    color: black;
  }

  .logo-in-login >>> .neon {
    font-family: neon;
    color: #FB4264;
    font-size: 4vh;
    line-height: 10vh;
    text-shadow: 0 0 3vh #F40A35;
  }

  .logo-in-login >>> .flux {
    font-family: neon;
    color: #426DFB;
    font-size: 4vh;
    line-height: 10vh;
    text-shadow: 0 0 3vh #2356FF;
  }

  .logo-in-login >>> .neon {
    animation: neon 3s ease infinite;
    -moz-animation: neon 3s ease infinite;
    -webkit-animation: neon 3s ease infinite;
    -o-animation: flux 3s linear infinite;
  }

  .logo-in-login >>> .flux {
    animation: flux 3s linear infinite;
    -moz-animation: flux 3s linear infinite;
    -webkit-animation: flux 3s linear infinite;
    -o-animation: flux 3s linear infinite;
  }

  @keyframes neon {
    0%,
    100% {
      /* text-shadow: 0 0 .5vw #FA1C16, 0 0 3vw #FA1C16, 0 0 10vw #FA1C16, 0 0 10vw #FA1C16, 0 0 .4vw #FED128, .5vw .5vw .1vw #806914; */
      color: #FED128;
    }
    50% {
      /* text-shadow: 0 0 .5vw #800E0B, 0 0 3vw #800E0B, 0 0 10vw #800E0B, 0 0 10vw #800E0B, 0 0 .4vw #800E0B, .5vw .5vw .1vw #40340A; */
      color: #806914;
    }
  }

  @keyframes flux {
    0%,
    100% {
      /* text-shadow: 0 0 1vw #1041FF, 0 0 3vw #1041FF, 0 0 10vw #1041FF, 0 0 10vw #1041FF, 0 0 .4vw #8BFDFE, .5vw .5vw .1vw #147280; */
      color: #28D7FE;
    }
    50% {
      /* text-shadow: 0 0 .5vw #082180, 0 0 1.5vw #082180, 0 0 5vw #082180, 0 0 5vw #082180, 0 0 .2vw #082180, .5vw .5vw .1vw #0A3940; */
      color: #146C80;
    }
  }
</style>