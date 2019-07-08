# mPOT
mPOT stands for Music Processesing and Organization with Tagging and is used to tag and organize a music library.

## Current State
This aplication is currently in development, each module will be released as a seperate piece of code under GPL license incase someone would want to use just that part.

## Features
### Completed
  * Being able to read audio files metadata using [TinyTag](https://github.com/devsnd/tinytag)
  * Organizes and names files at an output folder based on the name configuration file
  
### TO-DO
 * Process music files to the NEST API to grab metadata
 * Write NEST metadata to audio files
 * Create a GUI for simple use
 
## Configuration

### Name
The name file included with mPOT_tagging.py is a configuration for the naming convention for your files when organizing them.

Example<br>
 For Brittney Spear's Toxic
 <br>
 <b>Input:</b> 
 <br>
 <code> $track - $title </code>
 <br>
 <b>Output</b>
 <br>
 <code> 6 - Toxic</code>  
 
