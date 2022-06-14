const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
// const COMMUNITY = 'community/'
const MOVIES = 'movies/'
const ARTICLE = 'community/article/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username + '/',
    myArticles: username => HOST + ACCOUNTS + 'profile/' + username + '/my_articles/',
    myComments: username => HOST + ACCOUNTS + 'profile/' + username + '/my_comments/',
  },
  articles: {
    articleList: () => HOST + ARTICLE,
    articleDetail: articleId => HOST + ARTICLE + articleId + '/',
    articleNew: () => HOST + ARTICLE + 'create_article/',
    articleUpdate: articleId => HOST + ARTICLE + articleId +'/',
    articleLike: articleId => HOST + ARTICLE + articleId + '/like/',
    commentNew: articleId => HOST + ARTICLE + articleId + '/comments/',
    commentList: articleId => HOST + ARTICLE + articleId + '/comments/comment_list/',
    commentDetail: (articleId, commentId) => HOST + ARTICLE + articleId + '/comments/' + commentId + '/',
    commentLike: (articleId, commentId) => HOST + ARTICLE + articleId + '/comments/' + commentId + '/like/',
    voteArticle: (articleId) => HOST + ARTICLE + articleId + '/vote/'
  },
  movies: {
    movieList: () => HOST + MOVIES,
    movieRecommendation: () => HOST + MOVIES + 'recommend/',
    searchResult: (movieId) => HOST + MOVIES + movieId + '/search/',
  },
}