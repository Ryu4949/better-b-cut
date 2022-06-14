import router from '@/router'
import axios from 'axios'
import urls from '@/api/urls'
import _ from 'lodash'

export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    profile: {},
    authError: null,
    articleList: [],
    article: {},
    commentList: [],
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    articleList: state => state.articleList,
    article: state => state.article,
    commentList: state => state.commentList,
    isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_TOKEN: ( state, token ) => state.token = token ,
    SET_CURRENT_USER: (state, user) => state.currentUser = user, 
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_ARTICLE_LIST: (state, articleList) => state.articleList = articleList,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_COMMENT_LIST: (state, commentList) => state.commentList = commentList,
  },

  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      // 토큰 초기화
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    removeErrorMsg({commit}) {
      // 에러메시지 초기화
      commit('SET_AUTH_ERROR', {})
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        // signup url: http://localhost:8000/api/v1/accounts/signup/
        url: urls.accounts.signup(),
        method: 'post',
        // credentials 전송
        data: credentials
      })
        .then(res => {
          // 응답데이터의 key값에 토큰
          const token = res.data.key
          // 성공하면 토큰 저장
          dispatch('saveToken', token)
          // 로그인
          dispatch('fetchCurrentUser')
          // 메인 화면으로 이동
          router.push({ name: 'articleList' })
        })
        .catch(err => {
          // 에러 저장
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    login({ commit, dispatch }, credentials) {
      axios({
        url: urls.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'articleList' })
        })
        .catch(err => {
          commit('SET_AUTH_ERROR', err.response.data)
        })
      },

      logout({ getters, dispatch }) {
        axios({
          url: urls.accounts.logout(),
          method: 'post',
          headers: getters.authHeader
        })
          .then(() => {
            dispatch('removeToken')
            alert('성공적으로 로그아웃되었습니다.')
            router.push({ name: 'articleList'})
          })
          .error(err => {
            console.error(err.response)
          })
      },

    fetchCurrentUser({ commit, getters, dispatch }) {
      // 로그인했다면 (토큰 있다면)
      if (getters.isLoggedIn) {
        axios({
          url: urls.accounts.currentUserInfo(),
          method: 'get',
          // 토큰을 담아 보내기
          headers: getters.authHeader
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            // 401 에러라면 토큰 삭제하고 로그인 페이지로
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchArticleList({ commit }, criteria) {
      axios({
        url: urls.articles.articleList(),
        method: 'get',
        params: {criteria: criteria}
      })
        .then(res => commit('SET_ARTICLE_LIST', res.data))
        .catch(err => {console.log(err)})
    },

    articleNew({ getters, commit }, articleData) {
      axios({
        url: urls.articles.articleNew(),
        method: 'post',
        data: articleData,
        headers: getters.authHeader
      })
        // .then(res => router.push(`/articles/${res.data.pk}`))
        .then(res => {
          console.log(res.data)
          commit('SET_ARTICLE', res.data)
          router.push({ 
            name: 'articleDetail',
            params: { articlePk: getters.article.pk }
          })
        })
        .catch(err => console.log(err))
    },

    editArticle({ getters, commit }, article) {
      axios({
        url: urls.articles.articleUpdate(article.pk),
        method: 'put',
        data: { movie_pk: article.movie_pk, title: article.title, choices: article.choices },
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({ 
          name: 'articleDetail',
          params: { articlePk: article.pk }
        })
      })
      .catch(err => console.log(err))
    },

    fetchCommentList({ getters, commit }, articlePk) {
      axios({
        url: urls.articles.commentList(articlePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => commit('SET_COMMENT_LIST', res.data))
        .catch(err => console.log(err))
    },

    fetchArticle({ commit, getters }, articlePk) {
      axios({
        url: urls.articles.articleDetail(articlePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => commit('SET_ARTICLE', res.data))

        .catch(err => console.log(err))
    },


    fetchProfile({ commit, getters }, username ) {
      if (getters.isLoggedIn) {
        axios({
          url: urls.accounts.profile(username),
          method: 'get',
          headers: getters.authHeader
        })
          .then(res => commit('SET_PROFILE', res.data))
          .catch(err => console.log(err))
      }
    },
  },
  modules: {
  }
}