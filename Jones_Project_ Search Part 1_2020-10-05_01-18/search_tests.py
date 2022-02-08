from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch

# List of all available article titles for this search engine
# The benefit of using this is faster code - article_titles() will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
ARTICLE_TITLES = article_titles()

def test_example_unit_tests():
    # Storing into a variable so don't need to copy and paste long list every time
    # If you want to store search results into a variable like this, make sure you pass a copy of it when
    # calling a function, otherwise the original list (ie the one stored in your variable) is going to be
    # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
    dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']

    # Example tests, these do not count as your tests

    # Basic search, function #1
    assert search('dog') == dog_search_results
    # Advanced search option 1, function #2
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']
    assert title_length(25, dog_search_results.copy()) == expected

    # Advanced search option 2, function #3
    assert article_count(3, dog_search_results.copy()) == ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid']

    # Advanced search option 3, function #4
    assert random_article(3, dog_search_results.copy()) == 'Black dog (ghost)'

    # Advanced search option 4, function #5
    assert favorite_article('Guide dog', dog_search_results.copy()) == True

    # Advanced search option 5, function #6
    expected = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'USC Trojans volleyball', 'Mets de Guaynabo (volleyball)']
    assert multiple_keywords('volleyball', dog_search_results.copy()) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 1
    advanced_response = 25

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Edogawa, Tokyo\', \'Kevin Cadogan\', \'Endogenous cannabinoid\', \'Black dog (ghost)\', \'2007 Bulldogs RLFC season\', \'Mexican dog-faced bat\', \'Dalmatian (dog)\', \'Guide dog\', \'Georgia Bulldogs football\', \'Endoglin\', \'Sun dog\', \'The Mandogs\', \'Landseer (dog)\']\n'

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_soccer_unit_test():
    soccer_search_results = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen(soccer)', 'Craig Martin (soccer)', "United States men's national soccer team2009 results", 'China national soccer team', "Wake Forest Demon Deacons men'ssoccer"]
    assert search('soccer') == soccer_search_results
    assert title_length(25, soccer_search_results.cop()) == ['Will Johnson (soccer)', 'Steven Cohen(soccer)', 'Craig Martin (soccer)']
    assert article_count(4, soccer_search_results.copy()) == ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen(soccer)', 'Craig Martin (soccer)']
    assert random_article(5, soccer_search_results.copy()) == 'China national soccer team'
    assert favorite_article('Craig Martin (soccer)', soccer_search_results.copy()) == True
    expected = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen(soccer)', 'Craig Martin (soccer)', "United States men's national soccer team2009 results", 'China national soccer team', "Wake Forest Demon Deacons men'ssoccer", 'Digital photography', 'Wildlife photography']
    assert multiple_keywords('photography', soccer_search_results.copy()) == expected

def test_photography_unit_test():
    photography_search_results = ['Digital photography', 'Wildlife photography']
    assert search('photography') == photography_search_results
    assert title_length(15, photography_search_results.copy()) == 'No articles found'
    assert article_count(1, photogrpahy_search_results.copy()) == 'Digital photography'
    assert random_article(1, photogrpahy_search_results.copy()) == 'Wildlife photography'
    assert favorite_article('Wildness', photogrpahy_search_results.copy()) == False 
    expected = ['Digital photography', 'Wildlife photography', 'C Sharp (programming language)', 'Reflection-oriented programming', 'B(programming language)', 'Python (programming language)', 'Lua (programminglanguage)', 'Comparison of programming languages (basic instructions)', 'Ruby(programming language)', 'Semaphore (programming)']
    assert multiple_keywords('programming', photogrpahy_search_results.copy()) == expected

def test_empty_unit_test():
    assert search('') == []
    assert title_length(1, []) == 'No articles found'
    assert article_count(0, []) == 'No articles found'
    assert random_article(7, []) == 'No articles found'
    assert favorite_article('The Goonies', []) == False
    assert multiple_keywords('programming', []) == ['C Sharp (programming language)', 'Reflection-oriented programming', 'B(programming language)', 'Python (programming language)', 'Lua (programminglanguage)', 'Comparison of programming languages (basic instructions)', 'Ruby(programming language)', 'Semaphore (programming)']
    
@patch('builtins.input')
def test_search_integration_test_1(input_mock):
    keyword = 'programming'
    advanced_option = 1
    advanced_response = 25  
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'B (programming language)\', \'Semaphore (programming)\']\n'
    assert output == expected
    
@patch('builtins.input')
def test_search_integration_test_1(input_mock):
    keyword = 'programming'
    advanced_option = 2
    advanced_response = 3  
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'C Sharp (programming language)\', \' Reflection-oriented programming\', \'B (programming language)\']\n'
    assert output == expected  
    
@patch('builtins.input')
def test_search_integration_test_1(input_mock):
    keyword = 'programming'
    advanced_option = 3
    advanced_response = 5 
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'Comparison of programming languages (basic instructions)\']\n'
    assert output == expected
    
@patch('builtins.input')
def test_search_integration_test_1(input_mock):
    keyword = 'programming'
    advanced_option = 4
    advanced_response = 'Semaphore (programming)'
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'C Sharp (programming language)\', \'Reflection-oriented programming\', \'B(programming language)\', \'Python (programming language)\', \'Lua (programminglanguage)\', \'Comparison of programming languages (basic instructions)\', \'Ruby(programming language)\', \'Semaphore (programming)\']\nYour favorite article is in the returned articles!'
    assert output == expected
    
@patch('builtins.input')
def test_search_integration_test_1(input_mock):
    keyword = 'programming'
    advanced_option = 5
    advanced_response = 'photography'
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + '\n\nHere are your articles: [\'C Sharp (programming language)\', \'Reflection-oriented programming\', \'B(programming language)\', \'Python (programming language)\', \'Lua (programminglanguage)\', \'Comparison of programming languages (basic instructions)\', \'Ruby(programming language)\', \'Semaphore (programming)\', \'Digital photography\', \'Wildlife photography\']\n' 
    assert output == expected
# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To actually make all your tests run, call all of your test functions here.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    test_example_unit_tests()
    test_example_integration_test()
