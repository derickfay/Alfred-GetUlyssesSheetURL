# Alfred-GetUlyssesSheetURL
## An Alfred script filter for quick access to Ulysses sheet URLs

This is a python script which uses v. 2.8 of the [Ulysses x-callback-url scheme](https://ulyssesapp.com/kb/x-callback-url/) to populate a script filter for [Alfred 3](https://www.alfredapp.com).  It outputs Alfred-ready JSON but could probably be easily adapted for other launchers.

It replaces Ulysses' native process, which gets really tedious if you need to do it often:
* find the sheet you want to link from (thereby leaving the sheet you're currently working in and disrupting your writing flow)
* option right-click on the sheet
* Copy Callback URL
* go back to the sheet you were working in
* type the text for a new link
* mark it as a link
* when the pop-up appears, paste the URL
* hit enter to save the URL

With:
* launch the Alfred script filter
* find the title of the sheet you want to link to
* hit enter
* Paste From Markdown in Ulysses

## Setup

* install [xcall](https://github.com/martinfinke/xcall)
* In Alfred, create a new script filter, with language = python , and check "Alfred filters results"
* copy the script to the script filter
* Replace the access token in the code (see the authentication process on the Ulysses x-callback-url docs)

## &c 

Vaguely inspired by https://github.com/rovest/UlyssesReportAndMarkdown. (I initially implemented it in Workflow for iOS, but it's way too slow for regular use with a Ulysses library of 500+ sheets).

In my view, quick linking between sheets makes Ulysses much more viable as an NVAlt replacement.  
