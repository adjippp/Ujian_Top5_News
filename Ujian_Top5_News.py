import requests

url={
    '1' : 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=47bada165e3b40bd9d778cf8c01da00e',
    '2' : 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=47bada165e3b40bd9d778cf8c01da00e',
    '3' : 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=47bada165e3b40bd9d778cf8c01da00e',
    '4' : 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=47bada165e3b40bd9d778cf8c01da00e',
    '5' : 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=47bada165e3b40bd9d778cf8c01da00e'
}

kategori={
    0 : "Teknologi",
    1 : "Bisnis",
    2 : "Olahraga",
    3 : "Kesehatan",
    4 : "Science",
}


def top5NewsAPIGenerator(kategori):
    return url[kategori]
while True:
    try:
        for i in range(len(kategori)):
            print("[",i+1,"] Berita Seputar ",kategori[i])
        user=input("Ketik Pilihan Anda [1/2/3/4/5] : ")
        data = requests.get(top5NewsAPIGenerator(user))
        isiData = data.json()
        for i in range(5):
            print(i+1," - ",isiData['articles'][i]['title'])
    except:
        print("Input Salah")
    print(" ")
    lagi=input("Cek Lagi? y / n ")
    if(lagi=="n" or lagi=="N"):
        break
