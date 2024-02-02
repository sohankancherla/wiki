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
    if content == None:
        return render(request, "encyclopedia/page_not_found.html", {
            "title":name
        })
    return render(request, "encyclopedia/entry.html", {
        "title": name.title(),
        "content": markdown(content)
    })

def search(request):
    entries = util.list_entries()
    entries_lower = [entry.lower() for entry in entries]
    print(entries_lower)
    search = request.GET.get('q', '')
    if search.lower() in entries_lower:
        return redirect("/"+search.lower())
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