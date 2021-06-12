'''------------------------------------- Problem Statement -----------------------------------'''
'''
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.
Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string
“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
'''

#Start

queryStringList = []
searchResultDict = {}

def searchEngine(listOfSearchableItems):
    queryString = input("Please enter search keywords")
    for word in queryString.split():
        queryStringList.append(word)

    print("Search Completed! Following are the results found")
    for items in listOfSearchableItems:
        searchRelevanceDegree = 0
        for keyword in queryStringList:
            if items.lower().__contains__(keyword.lower()):
                searchRelevanceDegree+=1
        searchResultDict[items]=searchRelevanceDegree
    for results in (sorted(searchResultDict.items(),key=lambda searchResultDict:searchResultDict[1],reverse=True)):
        if results[1]>0:
            print(results[0])



if __name__ == '__main__':
    searchEngine(["Python is cool", "python is good", "python is not python snake"])