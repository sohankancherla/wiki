from django.shortcuts import render
from markdown import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    content = util.get_entry(name)
    return render(request, "encyclopedia/entry.html", {
        "title": name,
        "content": markdown(content)

    })

