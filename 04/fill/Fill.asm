// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//init screen and positions
@SCREEN
D=A
@position
M=D
@8192
D=A
@SCREEN
D=D+A
@endposition
M=D

//if key is pressed jump to white or black
(LOOP)
@KBD
D=M
@WHITE
D;JEQ
@BLACK 
0;JMP

//paint white
(WHITE)
@position
A=M
M=0
@END
0;JMP

//paint black
(BLACK)
@position
A=M
M=-1
@END
0;JMP

//increment position
(END)
@position
D=M+1
M=D
//decrement from end
@endposition
D=D-M
@LOOP
D;JNE
@SCREEN
D=A
@position
M=D
@LOOP
0;JMP

