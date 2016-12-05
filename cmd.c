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

#include "cmd.h"
#include "GCode.h"
#include "comm.h"
#include "autoHome.h"
#include "interp.h"

//This executes one of the commands in the enum.
//WARNING: this will overwrite any data in buf.
void executeCmd(char cmd, uint8 *buf, uint32 buflen)
{
    switch (cmd)
    {
        case cmd_gcode :
            execute_gcode(buf, buflen);
            break;
        case cmd_jog :
            execute_jog(buf, buflen);
            break;
        case cmd_home :
            execute_home(buf, buflen);
            break;
        case cmd_diag :
            execute_diag(buf, buflen);
            break;
        case cmd_pwr :
            execute_pwr(buf, buflen);
            break;
    }
}

//stores the gcode sent by the pi
//len is the number of bytes to expect, buflen is the length of buf
void execute_gcode(uint8 *buf, uint32 buflen)
{
    return;
}

//moves the motors a tiny amount.
void execute_jog(uint8* buf, uint32 buflen)
{
    return;
}

//homes motors
void execute_home(uint8* buf, uint32 buflen)
{
    //TODO: home axises independantly of each other.
    autoHome();
    return;
}

//sends back 20 bytes of diagnostics
void execute_diag(uint8* buf, uint32 buflen)
{
    return;
}

//turns motors on and off.
void execute_pwr(uint8* buf, uint32 buflen)
{
    return;
}

/* [] END OF FILE */
