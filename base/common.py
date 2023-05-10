# Sigma16: common.js
# Copyright (C) 2023 John T. O'Donnell.  License: GNU GPL Version 3 or later
# See Sigma16/README, LICENSE, and https:#jtod.github.io/home/Sigma16

# This file is part of Sigma16.  Sigma16 is free software: you can
# redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
# Sigma16 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.  You should have received
# a copy of the GNU General Public License along with Sigma16.  If
# not, see <https:#www.gnu.org/licenses/>.

import sys

esc = "\x1b"

bold = bright = 1
dim = 2
underline = 4
blink = 5
reverse = invert = 7
hidden = 8

simple = 9
black  = 0
red = 1
green = 2
yellow = 3
blue = 4
magenta = 5
cyan = 6
light_gray = 7
dark_grey = 60
light_red = 61
light_green = 62
light_yellow = 63
light_blue = 64
light_magenta = 65
light_cyan = 66
white = 67

foreground = 30

background = 40




__gloabals__ = globals()
resetall = [ __gloabals__.setdefault(f"reset_{i}",__gloabals__[i]+20) for i in __gloabals__ if i in ("bold", "bright", "dim", "blink", "reverse", "invert", "hidden")]





#----------------------------------------------------------------------
# common.js
#----------------------------------------------------------------------

S16HOMEPAGEURL = 'https:#jtod.github.io/home/Sigma16'

# ES_thread_host indicates which thread this emulator instance is
# running in.  This is represented with an unsigned int, not a
# symbol, so it can be stored in the system state vector.

ES_gui_thread      = 0
ES_worker_thread   = 1

def showThread (x):
    if(x==0):
        return "main"
    elif(x==1):
        return "worker"
    return "?"

def stacktrace ():
    console.trace ()

#/*
#def showThread (x) {
#    return x==0 ? ES_gui_thread_sym
#        : x==1 ? ES_worker_thread_sym
#        : null
#}
#*/



class mode :
    trace =  False
    showErr = True
    def setTrace():
        mode.trace = True

    def clearTrace():
        mode.trace = False

    def showMode():
        sys.stdout.write(f"{mode.trace}")

    def devlog (xs):
        if (mode.trace):
            sys.stdout.write (f"{xs}")
    
    def errlog (xs):
        if (mode.showErr):
            sys.stdout.write (f"{xs}")


#----------------------------------------------------------------------
# Logging error message
#----------------------------------------------------------------------

def indicateError (xs):
    sys.stdout.write(f"{esc}{red}m{xs}")
    console.trace ()

#----------------------------------------------------------------------
# Dialogues with the user
#----------------------------------------------------------------------

export function modalWarning (msg) {
    alert (msg);
}

# The innerHTML
# string is <pre ...>text of example</pre>.  The pre and pre tags
# need to be removed: they would confuse the assembler.

export const openingPreTag = /^<[^>]*>/;   # <pre...> at beginning
export const closingPreTag = /<[^>]*>$/;   # ...</pre> at end

# Clear the display of the object code in the linker pane

export function clearObjectCode () {
    let listing = "<pre class='HighlightedTextAsHtml'>"
        + "</pre>"
#    document.getElementById('LinkerText').innerHTML = listing;
    document.getElementById('LP_Body').innerHTML = listing;
#    console.log ("clearObjectCode skipping clear LinkerText");
}

# Similar to highlightListingLine in emulator

export function highlightField (xs,highlight) {
    return "<span class='" + highlight + "'>" + xs + "</span>";
}


# scrolling doesn't work if it just uses <pre> but not <code>

export let editorBufferTextArea; #
export let textFile = null; #
export let create;  #
export let textbox; #

# Text

export function highlightText (txt,tag) {
    return "<span class='" + tag + "'>" + txt + "</span>";
}
