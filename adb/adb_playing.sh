#! /usr/bin/bash

# connect phone
function openADB(){
    adb connect $1:5555
    adb shell #open adb command prompt
}

#disconnect
function closeADB(){
    exit # exit adb command prompt
    adb disconnect $1:5555
}


openADB $*