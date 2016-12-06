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
#include "heart.h"

char auto_home = 0;

void autoHome( char homing_bits)
{
    pulse_table_init();
    Timer_1_Wakeup();
    startHeartBeating();
    heartbeat_Wakeup();
    auto_home = homing_bits;
}

void autoHomeComplete()
{
    //tell GCode that we are done
    auto_home = 0;
}

char autoHoming()
{
    return auto_home;
}

/* [] END OF FILE */
