import json
import requests

genre_data = {
    '28': '액션',
    '12': '모험',
    '16': '애니메이션',
    '35': '코미디',
    '80': '범죄',
    '99': '다큐멘터리',
    '18': '드라마',
    '10751': '가족',
    '14': '판타지',
    '36': '역사',
    '27': '공포',
    '10402': '음악',
    '9648': '미스터리',
    '10749': '로맨스',
    '878': 'SF',
    '10770': 'TV 영화',
    '53': '스릴러',
    '10752': '전쟁',
    '37': '서부'
}

def genreid_to_genre(genre_ids):
    genre_name = ''
    for i in genre_ids:
        #print(i)
        genre_name += (genre_data[str(i)]+ ' ') 
    return genre_name.rstrip()


def release_date_confirm(date):
    if date:
        return date
    else:
        return "1900-01-01"

# movie 정보
result = []
url = "https://api.themoviedb.org/3/movie/popular"
key = "e53010cbbbc91dcb3b26e8894f6a8116"
for page in range(1, 6):
    URL = f'{url}?api_key={key}&language=ko-Kr&page={page}'

    raw_data = requests.get(URL).json()
    data = raw_data.get('results')
    for movie in data:
        #print(movie.get("genre_ids"))
        movie_dict = {
            "model" : "movies.movie",
            "pk" : movie.get("id"),
            "fields" : {
                "title" : movie.get("title"),
                "overview" : movie.get("overview"),
                "release_date" : release_date_confirm(movie.get("release_date")),
                "vote_average" : movie.get("vote_average"),
                "poster_path" : movie.get("poster_path"),
                "genre" : genreid_to_genre(movie.get("genre_ids"))
            }
        }
        result.append(movie_dict)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))
