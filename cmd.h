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
#ifndef CMD_H
#define CMD_H
    
#include <project.h>
    
    
enum
{
    cmd_unknown = 0,
    cmd_gcode = 1,
    cmd_jog = 2,
    cmd_home = 3,
    cmd_diag = 4,
    cmd_pwr = 5
};

//public methods:

//This executes one of the commands in the enum.
//WARNING: this will overwrite any data in buf.
void executeCmd(char cmd, uint8 *buf, uint32 buflen);

//For internal use only.

//stores the gcode sent by the pi
//len is the number of bytes to expect, buflen is the length of buf
void execute_gcode(uint8 *buf, uint32 buflen);

//moves the motors a tiny amount.
void execute_jog(uint8* buf, uint32 buflen);

//homes motors
void execute_home(uint8* buf, uint32 buflen);

//turns motors on and off.
void execute_pwr(uint8* buf, uint32 buflen);


    
#endif
/* [] END OF FILE */
