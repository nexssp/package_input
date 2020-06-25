; Nexss PROGRAMMER 2.x - Auto Hot Ke
; SETUP
EnvGet, NEXSS_PACKAGES_PATH, NEXSS_PACKAGES_PATH
#Include %A_AppData%/../../.nexss/packages/Nexss/Lib/NexssIn.ahk
#Include %A_AppData%/../../.nexss/packages/Nexss/Lib/NexssLog.ahk
; ======================================================

; Modify Data
NexssStdout.test := "test"

; InputBox, OutputVar [, Title, Prompt, HIDE, Width, Height, X, Y, Locale, Timeout, Default]
xTitle := "Enter Value"
try xTitle:=NexssStdout["_title"]
catch e { 

}

; nxsInfo(xTitle)
InputBox, ReturnValue, %xTitle%

if (ErrorLevel){
    nxsError("Cancelled.")
    Exit 1
}   
else{

    NexssStdout[NexssStdout.resultField_1]:=ReturnValue
}

; NexssStdout.Delete("start")

; ======================================================
#Include %A_AppData%/../../.nexss/packages/Nexss/Lib/NexssOut.ahk