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

int auto_home = 0;

void autoHome()
{
    pulse_table_init();
    auto_home = 1;
}

void autoHomeComplete()
{
    //honestly, I don't know what this is for, but we might need something here
    auto_home = 0;
}

char autoHoming()
{
    return auto_home;
}

/* [] END OF FILE */
