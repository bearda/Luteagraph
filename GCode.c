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
*/

#include <project.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "GCode.h"
#include "interp.h"
#include "autoHome.h"

//For internal use only
char current_GCode = NO_GCODE; //what mode are we currently in?
char GCode_buffer[256];
unsigned int GCode_loc = 0;




int mm_to_pulses(float mm)
{
    //This function is just a stub.
    return (int) (10 * mm);
}

void initGCode()
{
    GCode_loc = 0;
    GCode_buffer[GCode_loc] = 0;
}

int saveGCodeToFlash(const char *buffer, uint32 length)
{
    //this is jsut a stub at the moment.
    //Can we store this much stuff?
    if (length > 256)
    {
        return -1;
    }
    
    return snprintf(GCode_buffer, 256, "%s", buffer);
}

int readGcodeLine(char *GCode, unsigned int *GCodeLoc, int GCodeLen, char *line, uint8 lineLength)
{   
    char keepGoing = 1; // keep going until we find a space
    uint8 lineLoc = 0;
    
    //input validation
    if (GCode == NULL ||
        GCodeLoc == NULL ||
        line == NULL)
    {
        return -1;
    }
    
    
    while (keepGoing)
    {
        line[lineLoc] = GCode[*GCodeLoc + lineLoc];
        if (line[lineLoc] == '\n')
        {
            line[lineLoc] = '\0';
            keepGoing = 0;
        }
        
        lineLoc++;
        if (lineLoc + *GCodeLoc >= GCodeLen ||
            lineLoc >= lineLength)
        {
            keepGoing = 0;
            line[lineLoc] = '\0';
        }
        
    }
    *GCodeLoc += lineLoc;

    
    
    return (int) lineLoc;
}

#define WORD_BUF_LEN 64
int deGCode(char * command, float * X_G, float * Y_G, float * Z_G)
{
    int retval = -1;
    char wordsLeft = 1; //Are there still words we haven't read?
    char wordBuf[WORD_BUF_LEN]; // a buffer to store words in.
    uint8 commandLoc = 0; //where we are in the command buffer
    uint8 commandLen; // how long is the command string?
    float *cur_axis; //which axis did we just read?
    
    //input validation
    if (command == NULL ||
        X_G == NULL ||
        Y_G == NULL ||
        Z_G == NULL)
    {
        return -1;
    }
    
    commandLen = strlen(command);
    *X_G = -1;
    *Y_G = -1;
    *Z_G = -1;
    
    //look at the first character. If it is a space, we are using the previous GCode.
    if (command[0] == ' ')
    {
        retval = current_GCode;
        commandLoc += 1;
    }
    else
    {
        readGCodeWord( command, &commandLoc, wordBuf, WORD_BUF_LEN);
        if (strncmp(wordBuf, "G00", strlen(wordBuf)) == 0 || strncmp(wordBuf, "G0", strlen(wordBuf)) == 0)
        {
            retval = GCODE_00;
            current_GCode = GCODE_00;
        }
        else if (strncmp(wordBuf, "G01", strlen(wordBuf)) == 0 || strncmp(wordBuf, "G1", strlen(wordBuf)) == 0)
        {
            retval = GCODE_01;
            current_GCode = GCODE_01;

        }
        else
        {
            current_GCode = GCODE_UNKNOWN;
            return GCODE_UNKNOWN;
        }

    }
    
    //loop through all remaining words
    while (wordsLeft)
    {
        readGCodeWord( command, &commandLoc, wordBuf, WORD_BUF_LEN);
        //what letter is this?
        if (wordBuf[0] == 'X' || wordBuf[0] == 'x')
        {
            cur_axis = X_G;
        }
        else if (wordBuf[0] == 'Y' || wordBuf[0] == 'y')
        {
            cur_axis = Y_G;
        }
        else if (wordBuf[0] == 'Z' || wordBuf[0] == 'z')
        {
            cur_axis = Z_G;
        }
        else
        {
            //whelp, I'm confused. error out.
            return -1;
        }
        
        //read the float.
        *cur_axis = atof(wordBuf + 1);
        if (commandLoc >= commandLen)
        {
            wordsLeft = 0;
        }

    }
    
    return retval;
}


int readGCodeWord(char *line, uint8 *offset, char *word, uint8 wordLength)
{
    char keepGoing = 1; // keep going until we find a space
    uint8 lineLength;
    uint8 lineLoc = 0;
    
    //input validation
    if (line == NULL ||
        offset == NULL ||
        word == NULL)
    {
        return -1;
    }
    
    lineLength = strlen(line);
    
    while (keepGoing)
    {
        word[lineLoc] = line[*offset + lineLoc];
        if (word[lineLoc] == ' ')
        {
            word[lineLoc] = '\0';
            keepGoing = 0;
        }
        
        lineLoc++;
        if (lineLoc + *offset >= lineLength ||
            lineLoc >= wordLength)
        {
            keepGoing = 0;
            word[lineLoc] = '\0';
        }
        
    }
    *offset += lineLoc;

    
    
    return (int) lineLoc;
}

int executeGCode(char command, float X_G, float Y_G, float Z_G)
{
    int num_pulses = 0;// how many pulses have we queued.
    if (command == GCODE_UNKNOWN)
    {
        return 0; //we queued no pulses.
    }
    return num_pulses;
}

int runNextGCodeCommand( float *tar_x, float *tar_y, float *tar_z)
{
    char line[64];
    char code;
    
    pulse_table_init();
    if (autoHoming())
    {
        //so we are autohoming. Is the limit switch active?
        if (x_limit_Read())
        {
            //we have voltage! stop autohoming.
            autoHomeComplete();
            //we will now begin processing GCode as normal
        }
        else
        {
            //just keep swimming.
            *tar_x += 0.1;
            return linear_interp(getPrevX() + 1,-1,-1);

        }
    }
    if (GCode_loc < strlen(GCode_buffer))
    {
        readGcodeLine(GCode_buffer, &GCode_loc, strlen(GCode_buffer), line, 64);
        code = deGCode(line, tar_x, tar_y, tar_z);
        if (code == GCODE_UNKNOWN)
        {
            return 0;
        }
        else
        {
            return linear_interp(mm_to_pulses(*tar_x), mm_to_pulses(*tar_y), mm_to_pulses(*tar_z));
        }
    }
    return -1;
    
}

/* [] END OF FILE */
