/* ========================================
 *
 * Copyright YOUR COMPANY, THE YEAR
 * All Rights Reserved
 * UNPUBLISHED, LICENSED SOFTWARE.
 *
 * CONFIDENTIAL AND PROPRIETARY INFORMATION
 * WHICH IS THE PROPERTY OF your company.
 *
 * ========================================
This header file contains the necessary functions for processing gcode.
*/
#ifndef GCODE_HEADER_H
#define GCODE_HEADER_H
#include <project.h>

//saveGCodeToFlash
//args:
//  const char* buffer, The buffer that you want to save
//  uint32 length, the number of bytes that you want to save
//return:
//  The number of bytes saved
int saveGCodeToFlash(const char *buffer, uint32 length);


//Stop storing the current gcode.
void eraseGCodeFlash();


//initialize GCode. Specifically, it sets the pointer to the gcode buffer.
void initGCode();

//will look into flash and run the next gcode comand.
//return:
//  The number of pulses queued by the command.
//  returns the target coordinates by address
//  -1 if there are no more gcode commands.
int runNextGCodeCommand( float *tar_x, float *tar_y, float *tar_z);

//an enum of recognized gcodes
enum {
    GCODE_UNKNOWN = 0,
    GCODE_00,
    GCODE_01,
    NO_GCODE
};

//converts milimeters to pulses
//returns the number of pulses it would take to move mm milimeters, rounded down.
int mm_to_pulses(float mm);






//read a line of gcode as a null terminated string.
//returns the string length.
//-1 in case of failure.
int readGcodeLine(char *GCode, unsigned int *GCodeLoc, int GCodeLen, char *line, uint8 lineLength);

int readGCodeWord(char *line, uint8 *offset, char *word, uint8 wordLength);

//decode the gcode. returns one of the gcode enum values.
int deGCode(char * command, float * X_G, float * Y_G, float * Z_G);

//queue the pulses. returns the number of pulses queued, negative for error.
//if any of the float values are negative, that motor doesn't move.
int executeGCode(char command, float X_G, float Y_G, float Z_G);

#endif
/* [] END OF FILE */
