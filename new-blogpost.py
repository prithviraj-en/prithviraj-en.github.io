import bs4

# create a new file copied from blog-base with new filename
title = input("Title of Blog Post?")
file_temp = title.split(" ")
file_name = "-".join(file_temp) + ".html"

# change titles of file_name 
with open("blog/blog-base.html") as inf:
	txt = inf.read()
	soup = bs4.BeautifulSoup(txt)

title_div = soup.find_all("div",class_="title-div")
soup.title.string = title
title_div[0].append(title)

with open("blog/"+file_name, "wb") as inf:
	inf.write(soup.prettify("utf-8"))


# adding blog listing to index.html
with open("index.html") as inf:
	txt = inf.read()
	soup_index = bs4.BeautifulSoup(txt)

blog_list_div = soup_index.find_all("ul",class_="blog-list")
el = "<li><a href='blog/"+file_name+"'>"+title+"</a></li>"
blog_list_div.append(el)

with open("index.html",'wb') as inf:
	inf.write(soup_index.prettify("utf-8"))
