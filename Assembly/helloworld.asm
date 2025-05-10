extern _GetStdHandle@4
extern _WriteConsoleA@20
extern _ExitProcess@4
import _GetStdHandle@4 kernel32.dll
import _WriteConsoleA@20 kernel32.dll
import _ExitProcess@4 kernel32.dll

section .data
    message db 'Hello, World!', 0xA
    message_len equ $ - message

section .bss
    written resd 1

section .text
    global _start
    _start:
        ; Get stdout handle
        push -11
        call _GetStdHandle@4
        mov ebx, eax

        ; WriteConsoleA
        push 0
        push written
        push message_len
        push message
        push ebx
        call _WriteConsoleA@20

        ; ExitProcess(0)
        push 0
        call _ExitProcess@4