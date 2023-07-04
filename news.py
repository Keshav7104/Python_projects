from argparse import ArgumentParser
from requests import get
from json import loads
from time import sleep

#function to fetch news from news api and print it
def news(query:str)->None:
    url=f"https://newsapi.org/v2/everything?q={query}&from=2023-06-04&sortBy=publishedAt&apiKey=d54e5225461f43868e33f2441f041acf"
    r= get(url)
    news=loads(r.text)
    for article in news["articles"]:
        print('\n')
        print(article["title"])
        print(article["description"])
        print("-------------------------------------")
        sleep(3)

#driver code
if __name__ == "__main__":
    #makes a command line argument
    parser=ArgumentParser()
    parser.add_argument("query",help="About which topic you want news")
    args=parser.parse_args()

    #calls news function according to query
    print(f"\nHere are Some News about {args.query} around the globe \n\n")
    news(args.query)
