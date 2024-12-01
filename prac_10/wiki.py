"""
CP1404/CP5632 Practical
Testing Wikipedia API
"""
import wikipedia

page_title = input('Enter page title: ')
while page_title != '':
    try:
        summary = wikipedia.summary(page_title, 4)
        print(page_title)
        print(summary)
        print(wikipedia.page(page_title).url)
    except wikipedia.exceptions.DisambiguationError:
        print('We need a more specific title. Try one of the following, or a new search:')
        print('(BeautifulSoup warning)')
        print(wikipedia.search(page_title))
    except wikipedia.exceptions.PageError:
        print(f'Page id "{page_title}" does not match any pages. Try another id!')
    page_title = input('Enter page title: ')
