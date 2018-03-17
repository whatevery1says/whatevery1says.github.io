import os
from bs4 import BeautifulSoup

# Path to site folder
path = 'C:/Users/Scott/Documents/GitHub/whatevery1says/whatevery1says.github.io/'

# Files to be Modified
files = ['index.html', 'data.html', 'repositories.html', 'resources.html', 'slideshows.html', 'workshops.html']

# Menu Configuration
new_menu = """
<li><a href="index.html">Homepage</a></li>
<li>
<span class="opener">Workshops</span>
<ul>
<li><a href="workshops.html">Index</a></li>
<li><a href="slideshows.html">Slideshows</a></li>
<li><a href="repositories.html">Repositories</a></li>
<li><a href="data.html">Data</a></li>
<li><a href="resources.html">Resources</a></li>
<li><a href="newitem.html">New Item</a></li>
</ul>
</li>
<li><a href="https://we1s.ucsb.edu">WE1S Homepage</a></li>
<li><a href="http://4humanites.org">4Humanities</a></li>
"""

# Miniposts Configuration
new_miniposts = """
<article>
    <a href="workshops/topic-modeling/index.html" class="image"><img src="images/MarkdownGitHub.jpg" alt="Markdown and GitHub" /></a>
    <p><strong>Topic Modeling</strong>: How to do it and how not to do it.</p>
</article>
<article>
    <a href="workshops/markdown-and-github/index.html" class="image"><img src="images/MarkdownGitHub.jpg" alt="Markdown and GitHub" /></a>
    <p><strong>Markdown and GitHub</strong>: First Steps Toward learning Modern Digital Practices for Sustainable and Shareable Research.</p>
</article>
"""

def get_soup(path, file):
    filepath = os.path.join(path, file)
    with open(filepath, 'r') as f:
        doc = f.read()
    soup = BeautifulSoup(doc, 'html.parser')
    return soup

def rebuild_menu(soup, new_menu):
    snippet = BeautifulSoup(new_menu, 'html.parser')
    try:
        ul = soup.find('ul', id='menu-list')
        for li in ul('li'):
            li.decompose()
        ul.append(snippet)
    except:
        pass
    return soup

def rebuild_miniposts(soup, new_miniposts):
    snippet = BeautifulSoup(new_miniposts, 'html.parser')
    try:
        div = soup.find('div', class_="mini-posts")        
        for article in div('article'):
            article.decompose()
        div.append(snippet)
    except:
        pass
    return soup

def save(file, path, soup):
    filepath = os.path.join(path, file)
    with open(filepath, 'w') as f:
        f.write(soup.prettify())

# Execute (strict order is required)
for file in files:
    soup = get_soup(path, file)
    soup = rebuild_miniposts(soup, new_miniposts) # 1. Update miniposts
    soup = rebuild_menu(soup, new_menu) # 2. Update menu
    save(file, path, soup)
#     print(soup.prettify())
    print('Done!')