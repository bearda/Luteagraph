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

#include "GCode.h"
#include "comm.h"

char auto_home = 0;

void autoHome( char homing_bits)
{
    pulse_table_init();
    Timer_1_Wakeup();
    auto_home = homing_bits;
}

void autoHomeComplete()
{
    //tell GCode that we are done
    auto_home = 0;
    
    //we need to tell the pi that we are done.
    uint8 reply[2] = {0x03, 0x0};
    SPIS_SendReply(reply, 2);    
}

char autoHoming()
{
    return auto_home;
}

/* [] END OF FILE */
