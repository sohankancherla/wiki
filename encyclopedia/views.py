from django.http import HttpResponse
from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    content = util.get_entry(name)
    entries = util.list_entries()
    if content == None:
        return render(request, "encyclopedia/page_not_found.html", {
            "title": name
        })
    for entry in entries:
        if name.lower() == entry.lower():
            name = entry
    return render(request, "encyclopedia/entry.html", {
        "title": name,
        "content": markdown(content),
        "text_content": content
    })

def search(request):
    entries = util.list_entries()
    entries_lower = [entry.lower() for entry in entries]
    search = request.GET.get('q', '')
    if search.lower() in entries_lower:
        return redirect("/"+search)
    entries_matched = [entry for entry in entries if search.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "entries": entries_matched,
        "search" : search
    })

def new(request):
    return render(request, "encyclopedia/new.html")

def add(request):
    entries = util.list_entries()
    entries_lower = [entry.lower() for entry in entries]
    title = request.GET.get('title', '')
    print(title)
    content = request.GET.get('content', '')
    if title.lower() in entries_lower:
        return render(request, "encyclopedia/page_exists.html", {
            "title":title
        })
    util.save_entry(title, content)
    return redirect("/"+title)

def edit(request):
    pass