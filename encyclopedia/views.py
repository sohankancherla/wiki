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
    search = request.GET.get('q', '')
    if search in entries:
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
