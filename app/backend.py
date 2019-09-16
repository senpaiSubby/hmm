from mongoengine import *
from datetime import datetime
from app.prettyDate import prettyDate

connect("hmm", host="localhost", port=27017)

class Notes(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    time = DateTimeField(required=True)

def addNote(note):
    currentTime = datetime.now()
    try:
        title = note.partition('\n')[0]
        post = Notes(title=title[:40], content=note, time=currentTime)
        post.save()
    except NotUniqueError:
        return f"Duplicate: {note}"


def delNote(noteId):
    results = Notes.objects(pk=noteId)
    note = results[0]
    note.delete()

def editNote(noteId, content):
    results = Notes.objects(pk=noteId)
    note = results[0]
    note.content = content
    note.title = content.partition('\n')[0][:40]
    note.save()

#editNote("5d7ce7bef73950df222c562a", "Updates")

def searchNotes(searchTerm):
    results = Notes.objects(content__icontains=searchTerm)
    if results:
        print(f"There are {len(results)} results for term: {searchTerm}")
        for note in results:
            time = prettyDate(note.time)
            Id = note.id
            print(f"{Id} - {time} - {note.content}")
    else:
        print(f"No results for term: {searchTerm}")

def listNotes():
    numNotes = Notes.objects.count()
    noteList = []
    for note in Notes.objects:
        time = prettyDate(note.time)
        payload = {"id": note.id, "time": time, "title": note.title, "content": note.content}
        noteList.append(payload)
    return noteList
