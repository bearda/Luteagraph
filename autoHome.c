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
#include "interp.h"
#include "comm.h"

int auto_home = 0;

void autoHome()
{
    pulse_table_init();
    auto_home = 1;
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
