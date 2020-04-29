import os
import sys
import copy
import flask
from flask import request, jsonify
from flask_cors import CORS
from werkzeug.datastructures import ImmutableMultiDict
from bs4 import BeautifulSoup

name = "dev-server"
app = flask.Flask(name)
app.config["DEBUG"] = True

SYS_DIRS = ['templates','editor']

def HTMLtemplater(html_doc,parent_el_id,template_el_class,replacements):
    soup = BeautifulSoup(html_doc, 'html.parser')
    cat_section = soup.find(id=parent_el_id)
    cat_template = soup.find(class_=template_el_class)
    cat_el = copy.deepcopy(cat_template)
    print(cat_section)
    print(cat_el['class'])
    cat_el['class'] = cat_el['class'][:-2]
    cat_el = str(cat_el)
    for replacement in replacements:
        cat_el = cat_el.replace("{{"+replacement[0]+"}}",replacement[1])
    cat_el = BeautifulSoup(cat_el, 'html.parser')
    cat_section.append(cat_el)
    html = soup.prettify()
    return html

#### API Routes

@app.route('/', methods=['GET'])
def home():
    return "Server Works!!"

@app.route('/get_categories', methods=['GET'])
def get_categories():
    direx = os.listdir(os.getcwd())
    dirs = [d for d in direx if os.path.isdir(d) and d not in SYS_DIRS]
    return jsonify({'categories':dirs})

@app.route('/create_category', methods=['POST'])
def create_category():
    data = request.form.to_dict()
    cat = data['category']
    # Create category folder
    if cat in os.listdir(os.getcwd()): 
        return jsonify({'status': 'category already exists'}), 201

    os.mkdir(cat)

    # Create index page in new folder
    f = open("templates/category_index.html","r")
    template = f.read()
    f.close()
    #cat_templ = HTMLtemplater(template,"article-list","template-article",[("",)])
    template = template.replace('{{category_name}}',cat)
    f = open(cat+"/index.html","w")
    f.write(template)
    f.close()

    # Insert category in the homepage
    f = open('index.html','r')
    html_doc = f.read()
    f.close()
    html = HTMLtemplater(html_doc,"category-section","template-category",[("new_category",cat)])
    f = open('index.html','w')
    f.write(html)
    f.close()

    return jsonify({'status': 'saved'}), 201

@app.route('/save_md', methods=['POST'])
def save_md():
    data = request.form.to_dict()
    cat = data['category']
    filename = data['filename'].lower().replace(" ","_")
    md_file = open(cat+"/"+filename+".md","w")
    md_file.write(data['text'])
    md_file.close()
    return jsonify({'status': 'saved'}), 201

@app.route('/save_html', methods=['POST'])
def save_html():
    data = request.form.to_dict()
    print(data)
    cat = data['category']
    filename = data['filename'].lower().replace(" ","_")
    html_file = open(cat+"/"+filename+".html","w")
    html_file.write(data['text'])
    html_file.close()

    f = open(cat+"/index.html","r")
    html = f.read()
    f.close()
    title = filename.replace("_"," ")
    article_templ = HTMLtemplater(html,"article-list","template-article",[("article_link",filename),("article_title",title)])
    f = open(cat+"/index.html","w")
    f.write(article_templ)
    f.close()
    return jsonify({'status': 'saved'}), 201


# Run API server
cors = CORS(app)
app.run()