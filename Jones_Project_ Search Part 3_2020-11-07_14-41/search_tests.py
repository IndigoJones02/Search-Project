from search import title_to_info, keyword_to_titles, search, article_info, article_length, title_timestamp, favorite_author, multiple_keywords, display_result
from search_tests_helper import print_basic, print_advanced, print_advanced_option, get_print
from wiki import article_metadata, title_to_info_map, keyword_to_titles_map
from unittest.mock import patch
from copy import deepcopy

# List of all available article titles for this search engine
# The benefit of using this is faster code - these functions will execute
# every time it gets called, but if the return value of it gets stored it into
# a variable, the function will not need to run every time the list of available
# articles is needed.
METADATA = article_metadata()
TITLE_TO_INFO = title_to_info_map()
KEYWORD_TO_TITLES = keyword_to_titles_map()

# Storing into a variable so don't need to copy and paste long list every time
DOG = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']

TRAVEL = ['Time travel']

MUSIC = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Rock music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Tony Kaye (musician)', 'Texture (music)', '2007 in music', '2008 in music']

PROGRAMMING = ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']

SOCCER = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']

PHOTO = ['Digital photography']

SCHOOL = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)']

PLACE = ['2009 in music', 'List of dystopian music, TV programs, and games', '2006 in music', '2007 in music', '2008 in music']

DANCE = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music']

def test_example_title_to_info_tests():
    ''' Tests for title_to_info(), function #1. '''
    # Example tests, these do not count as your tests
    assert title_to_info(METADATA) == TITLE_TO_INFO

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of title_to_info with fake_metadata
    expected = {'an article title': {'author': 'andrea', 'timestamp': 1234567890, 'length': 103}, 
                'another article title': {'author': 'helloworld', 'timestamp': 987123456, 'length': 8029}}
    assert title_to_info(deepcopy(fake_metadata)) == expected

def test_example_keyword_to_titles_tests():
    ''' Tests for keyword_to_titles(), function #2. '''
    # Function #2
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES

    # Create fake metadata to test
    fake_metadata = [['an article title', 'andrea', 1234567890, 103, ['some', 'words', 'that', 'make', 'up', 'sentence']],
                     ['another article title', 'helloworld', 987123456, 8029, ['more', 'words', 'could', 'make', 'sentences']]]

    # Expected value of keyword_to_titles with fake_metadata
    expected = {'some': ['an article title'], 'words': ['an article title', 'another article title'], 'that': ['an article title'], 'make': ['an article title', 'another article title'], 'up': ['an article title'], 'sentence': ['an article title'], 'more': ['another article title'], 'could': ['another article title'], 'sentences': ['another article title']}

    assert keyword_to_titles(deepcopy(fake_metadata)) == expected

def test_example_unit_tests():
    # Example tests, these do not count as your tests

    # Basic search, function #3
    assert search('dog', KEYWORD_TO_TITLES) == DOG

    # Advanced search option 1, function #4
    expected = {'Black dog (ghost)': {'author': 'SmackBot', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'AnomieBOT', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'J. Spencer', 'timestamp': 1207793294, 'length': 26582}, 'Guide dog': {'author': 'Sarranduin', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Hellbus', 'timestamp': 1208969289, 'length': 18050}}
    assert article_info(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 2, function #5
    expected = ['Mexican dog-faced bat', 'Guide dog']
    assert article_length(8000, deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 3, function #6
    expected = {'Black dog (ghost)': 1220471117, 'Mexican dog-faced bat': 1255316429, 'Dalmatian (dog)': 1207793294, 'Guide dog': 1165601603, 'Sun dog': 1208969289}
    assert title_timestamp(deepcopy(DOG), TITLE_TO_INFO) == expected

    # Advanced search option 4, function #7
    assert favorite_author('J. Spencer', deepcopy(DOG), TITLE_TO_INFO) == True
    assert favorite_author('Andrea', deepcopy(DOG), TITLE_TO_INFO) == False

    # Advanced search option 5, function #8
    expected = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(DOG)) == expected

# For all integration test functions, remember to put in patch so input() gets mocked out
@patch('builtins.input')
def test_example_integration_test(input_mock):
    keyword = 'dog'
    advanced_option = 2
    advanced_response = 8000

    # Output of calling display_results() with given user input
    output = get_print(input_mock, [keyword, advanced_option, advanced_response])

    # Expected print outs from running display_results() with above user input
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat', 'Guide dog']\n"

    # Test whether calling display_results() with given user input equals expected printout
    assert output == expected

# TODO Write tests below this line. Do not remove.
def test_title_to_info():
    assert title_to_info(METADATA) == TITLE_TO_INFO
    fake_metadata = [['an article title', 'indigo', 789510111214, 301, ['here', 'are', 'some', 'words', 'for', 'sentence']],
           ['another article title', 'applepie', 14567829024, 8457, ['more', 'words', 'in', 'a', 'sentence']]]
    expected = {'an article title': {'author': 'indigo', 'timestamp':  789510111214, 'length': 301}, 
                'another article title': {'author': 'applepie', 'timestamp': 14567829024, 'length': 8457}}
                
    assert title_to_info(fake_metadata) == expected
    
    fake_metadata = [['an article title', 'jimbo', 987510111214, 391, ['there', 'is', 'some', 'words', 'for', 'sentence']],
           ['another article title', 'applepie', 54167829024, 8377, ['more', 'words', 'from', 'a', 'text']]]
    expected = {'an article title': {'author': 'jimbo', 'timestamp':  987510111214, 'length': 391}, 
                'another article title': {'author': 'applepie', 'timestamp': 54167829024, 'length': 8377}}
                
    assert title_to_info(fake_metadata) == expected
    
    fake_metadata = [['an article title', 'MIchaelSCott', 789599991214, 981, ['here', 'we', 'got', 'words', 'from', 'sentences']],
           ['another article title', 'applepie', 14567829045, 8490, ['more', 'words', 'from', 'a', 'sentence']]]
    expected = {'an article title': {'author': 'MIchaelSCott', 'timestamp':  789599991214, 'length': 981}, 
                'another article title': {'author': 'applepie', 'timestamp': 14567829045, 'length': 8490}}
                
    assert title_to_info(fake_metadata) == expected

def test_keyword_to_titles():
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES
    fake_metadata = [['an article title', 'indigo', 789510111214, 301, ['here', 'are', 'some', 'words', 'for', 'sentence']],
                        ['another article title', 'applepie', 14567829024, 8457, ['more', 'words', 'in', 'a', 'sentence']]]
    expected = {'here': ['an article title'], 'are': ['an article title'], 'some': ['an article title'], 'words': ['an article title', 'another article title'], 'for': ['an article title'], 'sentence': ['an article title', 'another article title'], 'more': ['another article title'], 'in': ['another article title'], 'a': ['another article title']}
    assert keyword_to_titles(fake_metadata) == expected
    
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES
    fake_metadata = [['an article title', 'iCarly', 789510111990, 302, ['there', 'is', 'some', 'words', 'from', 'sentence']],
                        ['another article title', 'applepie', 145678291989, 8490, ['big', 'words', 'in', 'a', 'sentence']]]
    expected = {'there': ['an article title'], 'is': ['an article title'], 'some': ['an article title'], 'words': ['an article title', 'another article title'], 'from': ['an article title'], 'sentence': ['an article title', 'another article title'], 'big': ['another article title'], 'in': ['another article title'], 'a': ['another article title']}
    assert keyword_to_titles(fake_metadata) == expected
    
    assert keyword_to_titles(METADATA) == KEYWORD_TO_TITLES
    fake_metadata = [['an article title', 'Blake Lively', 598710111214, 961, ['there', 'you', 'go', 'words', 'for', 'sentence']],
                        ['another article title', 'applepie', 6547829024, 5657, ['many', 'words', 'in', 'the', 'sentence']]]
    expected = {'there': ['an article title'], 'you': ['an article title'], 'go': ['an article title'], 'words': ['an article title', 'another article title'], 'for': ['an article title'], 'sentence': ['an article title', 'another article title'], 'many': ['another article title'], 'in': ['another article title'], 'the': ['another article title']}
    assert keyword_to_titles(fake_metadata) == expected
    
def test_unit_test_1():
    assert search('soccer', KEYWORD_TO_TITLES
    ) == SOCCER
    
    expected = {'Spain national beach soccer team': {'author': 'Pegship', 'timestamp': 1233458894, 'length': 1526}, 'Will Johnson (soccer)': {'author': 'Mayumashu', 'timestamp': 1218489712, 'length': 3562}, 'Steven Cohen (soccer)': {'author': 'Scouselad10', 'timestamp': 1237669593, 'length': 2117}}
    assert article_info(deepcopy(SOCCER), TITLE_TO_INFO) == expected
    
    expected = ['Spain national beach soccer team']
    assert article_length(2000, deepcopy(SOCCER), TITLE_TO_INFO) == expected
    
    expected = {'Spain national beach soccer team': 1233458894, 'Will Johnson (soccer)': 1218489712, 'Steven Cohen (soccer)': 1237669593}
    assert title_timestamp(deepcopy(SOCCER), TITLE_TO_INFO) == expected
    
    assert favorite_author('steve co', deepcopy(SOCCER), TITLE_TO_INFO) == False
    
    expected = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Digital photography']
    assert multiple_keywords('photo', deepcopy(SOCCER)) == expected
    
def test_unit_test_2():
    assert search('school', KEYWORD_TO_TITLES) == SCHOOL
    
    expected = {'Edogawa, Tokyo': {'author': 'Ciphers', 'timestamp': 1222607041, 'length': 4526}, 'Fisk University': {'author': 'NerdyScienceDude', 'timestamp': 1263393671, 'length': 16246}, 'Annie (musical)': {'author': 'Piano non troppo', 'timestamp': 1223619626, 'length': 27558}, 'Alex Turner (musician)': {'author': 'CambridgeBayWeather', 'timestamp': 1187010135, 'length': 9718}}
    assert article_info(deepcopy(SCHOOL), TITLE_TO_INFO) == expected
    
    expected = ['Edogawa, Tokyo']
    assert article_length(5000, deepcopy(SCHOOL), TITLE_TO_INFO) == expected
    
    expected = {'Edogawa, Tokyo': 1222607041, 'Fisk University': 1263393671, 'Annie (musical)': 1223619626, 'Alex Turner (musician)': 1187010135}
    assert title_timestamp(deepcopy(SCHOOL), TITLE_TO_INFO) == expected
    
    assert favorite_author('Ciphers', deepcopy(SCHOOL), TITLE_TO_INFO) == True
    
    expected = ['Edogawa, Tokyo', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
    assert multiple_keywords('soccer', deepcopy(SCHOOL)) == expected
    
def test_unit_test_3():
    assert search('dance', KEYWORD_TO_TITLES) == DANCE
    
    expected = {'List of Canadian musicians': {'author': 'Bearcat', 'timestamp': 1181623340, 'length': 21023}, '2009 in music': {'author': 'SE KinG', 'timestamp': 1235133583, 'length': 69451}, 'Old-time music': {'author': 'Badagnani', 'timestamp': 1124771619, 'length': 12755}, '1936 in music': {'author': 'JohnRogers', 'timestamp': 1243745950, 'length': 23417}, 'Indian classical music': {'author': 'Davydog', 'timestamp': 1222543238, 'length': 9503}}
    assert article_info(deepcopy(DANCE), TITLE_TO_INFO) == expected
    
    expected = ['Old-time music', 'Indian classical music']
    assert article_length(20000, deepcopy(DANCE), TITLE_TO_INFO) == expected 
    
    expected = {'List of Canadian musicians': 1181623340, '2009 in music': 1235133583, 'Old-time music': 1124771619, '1936 in music': 1243745950, 'Indian classical music': 1222543238}
    assert title_timestamp(deepcopy(DANCE), TITLE_TO_INFO) == expected 
    
    assert favorite_author('SE KinG', deepcopy(DANCE), TITLE_TO_INFO) == True
    expected = ['List of Canadian musicians', '2009 in music', 'Old-time music', '1936 in music', 'Indian classical music', 'Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
    assert multiple_keywords('dog', deepcopy(DANCE)) == expected
    
def test_unit_test_4():
    assert search('', KEYWORD_TO_TITLES) == []
    assert article_info([], TITLE_TO_INFO) == {}
    assert article_length(1000, [], TITLE_TO_INFO) == []
    assert title_timestamp([], TITLE_TO_INFO) == {}
    assert favorite_author('J. Spencer', [], TITLE_TO_INFO) == False
    assert multiple_keywords('photo', []) == ['Digital photography']
    
    
    
@patch('builtins.input')
def test_integration_1(input_mock):
    keyword = 'programming'
    advanced_option = 2
    advanced_response = 10000

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Lua (programming language)', 'Covariance and contravariance (computer science)']\n"
    assert output == expected


@patch('builtins.input')
def test_integration_2(input_mock):
    keyword = 'programming'
    advanced_option = 6
    advanced_response = ''

    output = get_print(input_mock, [keyword, advanced_option, advanced_response])
    expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['C Sharp (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Covariance and contravariance (computer science)', 'Personal computer', 'Ruby (programming language)']\n"
    assert output == expected

# Write tests above this line. Do not remove.

# This automatically gets called when this file runs - this is how Python works.
# To make all tests run, call all test functions inside the if statement.
if __name__ == "__main__":
    # TODO Call all your test functions here
    # Follow the correct indentation as these two examples
    # As you're done with each function, uncomment the example test functions
    # and make sure they pass
    test_example_title_to_info_tests()
    test_example_keyword_to_titles_tests()
    test_example_unit_tests()
    test_example_integration_test()
    test_title_to_info()
    test_keyword_to_titles()
    test_unit_test_1()
    test_unit_test_2()
    test_unit_test_3()
    test_unit_test_4()
    test_integration_1()
    test_integration_2()
