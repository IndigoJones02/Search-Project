from wiki import article_titles, ask_search, ask_advanced_search

# # 1) 
# #
# # Function: search
# #
# # Parameters:
# #   keyword - search word to look for in article titles
# #
# # Returns: list of article titles containing given keyword. If the keyword
# # is empty, return an empty list.
# #
# # Hint: to get list of existing article titles, use article_titles()

# # TODO Write code for #1 here
def search(keyword):
    new_list = []
    if keyword == '':
        return []
    else:
        for word in article_titles():
            if keyword in word:
                new_list = new_list + [word]
    return new_list


        

# # 2) 
# #
# # Function: title_length
# #
# # Returns 
# #
# # Parameters:
# #   max_length - max character length of article titles
# #   titles - list of article titles to search through
# #
# # Returns: list of article titles from given titles with given max_length 
# # number of characters 

# # TODO Write code for #2 here
def title_length(max_length, titles):
    article_list = []
    for title in titles:
        if len(title) <= max_length:
            article_list = article_list + [title]
    return article_list
#print(title_length(35, 'soccer'))


# # 3) 
# #
# # Function: article_count
# #
# # Parameters:
# #   count - max number of returned articles
# #   titles - list of article titles to search through
# #
# # Returns: list of articles in given titles starting from the 
# # beginning that do not exceed given count in total. If there are no 
# # given article titles or the index exceeds the number of articles, 
# # return an empty list regardless of the count
# #
# # Warning: Python will not throw an error when the index goes beyond
# # the length of the list. Please take care of that case - if your code
# # gets the index beyond the length of the title, points will get taken
# # off.

# # TODO Write code for #3 here
def article_count(count, titles):
    if count > len(titles) or titles == '' or titles == []:
        return []
    return titles[:count]
# print(article_count(2, ''))   
# print(search('programming')[:7])

# # 4) 
# #
# # Function: random_article
# #
# # Parameters:
# #   index - index at which article title to return
# #   titles - list of article titles to search through
# #
# # Returns: article title in given titles at given index. If
# # index is not valid, return an empty string

# # TODO Write code for #4 here
def random_article(index, titles):
    if index > len(titles) or titles == '' or titles == []:
        return ''
    return titles[index]
# print(random_article(2, ''))      

# # 5) 
# #
# # Function: favorite_article
# #
# # Parameters:
# #   favorite - favorite article title
# #   titles - list of article titles to search through
# #
# # Returns: True if favorite article is in the given articles, 
# # False otherwise

# # TODO Write code for #4 here
def favorite_article(favorite, titles):
    for text in titles:
        if favorite == text:
          return True
    return False
# print(favorite_article('The Mandogs', 'dogs'))

# # 6) 
# #
# # Function: multiple_keywords
# #
# # Parameters:
# #   keyword - additional keyword to search
# #   titles - list article titles resulting from basic search
# #
# # Returns: searches for article titles from entire list of available
# # articles and adds those articles to list of article titles from basic 
# # search

# # TODO Write code for #4 here
def multiple_keywords(keyword, titles):
    return titles + search(keyword)
# print(multiple_keywords('soccer', 'volleyball'))

# # Prints out articles based on searched keyword and advanced options
def display_result():
#     # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

#     # advanced stores user's chosen advanced option (1-5)
#     # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
#         # value stores max article title length in number of characters
#         # Update article titles to contain only ones of the maximum length
#         # TODO uncomment following line after writing the function
        articles = title_length(value, articles)
    elif advanced == 2:
#         # value stores max number of articles
#         # Update article titles to contain only the max number of articles
#         # TODO uncomment following line after writing the function
        articles = article_count(value, articles)
    elif advanced == 3:
#         # value stores random number
#         # Update articles to only contain the article title at index of the random number
#         # TODO uncomment following line after writing the function
        articles = random_article(value, articles)
    elif advanced == 4:
#         # value stores article title
#         # Store whether article title is in the search results into a variable named has_favorite
#         # TODO uncomment following line after writing the function
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
#         # value stores keyword to search
#         # Updated article titles to contain article titles from the first search and the second search
#         # TODO uncomment following line after writing the function
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
