<template>
  <div class="signup">
    <div class="block"></div>
    <logo-icon class="logo-in-login"></logo-icon>

    <div class="container bg-light p-3 mt-2 deco-container">
      <h1 class="text-align:right;">Sign up</h1>
      <hr class="mb-2">
      <!--회원가입 폼-->
      <b-form class="login-form" @submit.prevent="signup(credentials)">
        <div class="container">
          <!--username-->
          <div class="d-flex row align-content-center my-3 ">
            <div class="col-3">
              <label for="username" class="text-dark mt-3 ">Username</label>
            </div>
            <div class="col-9">
              <b-form-input 
                  id="username" 
                  v-model="credentials.username" 
                  type="text" 
                  placeholder="Enter Username"
                  required>
              </b-form-input>
            </div>
          </div>

          <!--password-->
          <div class="d-flex row align-content-center my-3 ">
              <div class="col-3">
                <label for="password1" class="text-dark mt-3" >Password1</label>
              </div>
              <div class="col-9">
              <b-form-input 
                id="password" 
                v-model="credentials.password1" 
                type="password" 
                placeholder="Enter Password"
                required></b-form-input>
            </div>
          </div>

          <div class="d-flex row align-content-center my-3 ">
              <div class="col-3">
                <label for="password2" class="text-dark mt-3" >Password2</label>
              </div>
              <div class="col-9">
                <b-form-input 
                  id="password2" 
                  v-model="credentials.password2" 
                  type="password" 
                  placeholder="Password Confirm"
                  required></b-form-input>
              </div>
          </div>
        </div>
        <b-button type="submit" class="mt-4 btn btn-default">Sign up</b-button>
      </b-form>
    </div>
    <account-error-list v-if="authError"></account-error-list>
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
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup', 'removeErrorMsg'])
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

  .signup {
    text-align: center;
  }

  .deco-container {
    width: 450px; 
    margin: 0 auto; /* 가로로 중앙에 배치 */ 
    background-color: rgba(151, 151, 151, 0.315);
    border: none;
    border-radius: 20px;
    box-shadow: 0 9px 45px rgba(49, 49, 49, 0.6);
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
  .btn-default {
    width: 150px;
    margin-top :10px;
    background-color: navy;
    color:white;
    border:none;
  }

  .block {
    height: 12vh;
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