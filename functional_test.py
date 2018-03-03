from selenium import webdriver

browser = webdriver.Firefox()

# My cool new online to-do app. Check out its hormepage
browser.get('http://localhost:8000')

# The page title and header mention to-do list
assert 'To-Do' in browser.title

# I am invited to enter a to-do item stright away.

# I type "cumpleaños de Martinez" into the text box

# When I hit enter, the page updates, and now the page lists
# "1: cumpleaños de Martinez" as an item in the to-do list

# There is still a text box inviting me to add another item. I
# enter "buscar un regalo"

# The page updates again, an now shows both items on my list

# I wonder whether the site will remember my list. Then I see
# that the site has generated a unique URL for me -- there is 
# some explanatory text to that effect.

# I visit that URL - my to-do list is still there.

# Satisfied, I go back to sleep.

browser.quit()
