# import requests
# import json

# result = requests.get("https://jsonplaceholder.typicode.com/todos")
# result = json.loads(result.text)

# for i in result:
#     print(i["title"])



                  #####UYGULAMA#####


# import requests

# import json

# api_url= "https://api.exchangetesapi.io/latest?base="
# bozulan_doviz= input("Bozulan döviz türü: ")
# alinan_doviz= input("Alınan döviz türü: ")
# miktar= int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))


# result= requests.get(api_url+bozulan_doviz)

# result= json.loads(result.text)

# print("1 {0} = {1} {2}" . format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
# print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["rates"][alinan_doviz], alinan_doviz))



import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "e8a9d5f82d78ca210c8076d648685c12"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movieApi = theMovieDb()

while True:
    secim = input("1-Popular Movies\n2- Search Movies\n3-Exit\nSeçim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])

        if secim == "2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie["name"])




