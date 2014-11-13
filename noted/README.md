Noted is a note daemon that runs note-related helpers inside a Docker-container. There is a specific structure you should have on your notes, but it is fairly logical.
The only thing you haveto do is mount your note-folder, and let this container run...

Your notes should (just as an best practice thingy for now, but might be needed):
* Be written in Markdown (.md), or MultiMarkdown (.mdd)
* Have datestamp in the name, like `2014-11-09 note name.md`
* Be a folder, if you need several files inside you note, like `2014-11-09 testing abc/`
  * The main file in this folder should be `README.md`
* Using hashtags in filenames if wanted, like `2014-11-09 note name #project-xyz` (creates xyz as a subtag on project, read below about tagging)

What the container will provide
* Tag manager daemon
* iPython notebook notes
* Dropbox sync

Why?
* Because your note will be stored as plain files and you should be able to use tools like grep to search your notes (locally).
* Didnt want to run the daemons we run on my desktop
* Wanted something that could work as a helper, not something I absolutly had to run all the time..

# todo
* Dropbox
