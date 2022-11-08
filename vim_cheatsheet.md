# VIM
## Table of Content

## Introduction

## Why you have to use VIM?

### Prelude
1. VIM has different modes:
	1. **NORMAL MODE**:
		- can be accessed from other modes by pressing 'ESC' 
		- this is the mode where you can move around in the file and execute most basic and advanced commands
		- when you are in normal mode VIM shows nothing at the bottom line.
	2. **INSERT MODE**:
		- can be accessed by different commands (see chapter Basic Commands)
		- this is the mode where you can typing just like in a regular text editor.
		- when you are in insert mode VIM shows "-- INSERT --" at the bottom line.
	3. **VISUAL MODE**:
		- can be accessed by different commands (see chapter Basic Commands)
		- this is the mode where you can select text (similar as selecting text with a mouse) and apply commands on the seleciton (see chapter Basic Commands)
		- when you are in visual mode VIM shows "-- VISUAL --" at the bottom line. But there are other visual modes too: "-- BLOCK-Visual --" and "-- LINEWISE-VISUAL --"
	4. **COMMAND MODE**: 
		- can be accessed by typing ':' from normal mode. The bottom line shows a ':' after which you can type in your command.
		- this is the mode where you can typ in commands
2. The syntax of the language is broken down into two parts: 1. **{operation}** and 2. **{target}** ^[^1]^ (e.g. the command 'dw' stands for delete:d and word:w --> delete the word under the cursor). After you have typed in an {operator} VIM will wait until you typed in the {target}.
3. Commands are **repeatable** (using '.' in command mode) and **undoable** (using 'u' in command mode)
4. Most commands can act also as motion command (e.g. the command 'w' stands for 'word'. But you can also use 'w' in normal mode to move one word forward).
5. You can combine different commands and extend those commands (see chapter Command Examples)

## Basic Commands
### Basic
. => {command} repeat last change
d => {operator} Delete
c => {operator} Change (delete and enter insert mode)
\> => {operator} Indent

### Moving around
h => {target} move one character backwards
j => {target} move one line down
k => {target} move one line up
l => {target} move one character forward
w => {target} Word (move one word foward)
b => {target} Back (move one word back)

### Different ways to enter INSERT MODE
c => {operator} Change (delete selection and enter insert mode)

### Text Objects
iw => {target} Inner Word (target is the word where the cursor is in)
i( => {target} Inner Parenthese
i[ => {target} Inner Brackets
i{ => {target} Innter Curly Brackets
it => {target} Inner Tag 
i" => {target} Innter Quotes
ip => {target} Inner Paragraph

### Find Objects
f => {target} find the next character forward
F => {target} find the next character backward
t => {target} go up to the next character forward
T => {target} go up to the next character backward
/ => {target} SEARCH (up to the next match) forward
? => {target} SEARCH (up to the next match) backward
### Visualising
v => visually select character

### Copy and Paste
y => Yank (copy visualised selection)

## Recommended Usage
- use "Find Objects" commands to change text. So it is easier to repeat those changes
- use relative number (see chapter How to create w vimrc file)

## How to create a vimrc file

## How to add addons

### Recommneded Plugins
- Surround
- Commentary
- ReplaceWithRegister
- System-copy

## Recommended Links
1. https://www.youtube.com/watch?v=wlR5gYd6um0&list=RDQMogWdmKuePOk&start_radio=1
2. https://benmccormick.org/learning-vim-in-2014
3. https://www.vim.org/

## Sources
[^1]: [Mastering the Vim Language](https://www.youtube.com/watch?v=wlR5gYd6um0&list=RDQMogWdmKuePOk&start_radio=1)
