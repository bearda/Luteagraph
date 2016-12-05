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
#ifndef DIAG_H
#define DIAG_H
    
#include <project.h>
    
struct __attribute__((__packed__)) diagnosticMessage_t 
    {
        uint8 packet_type; //This should always be 0x04
        int32 x_pos;
        int32 y_pos;
        int32 z_pos;
        int32 t_pos;
        char homed; //x,y,z,t,-,-,-,-, have these axis been homed since we booted?
        char servo_on; //x,y,z,t,-,-,-,-, are these motors turned on?
        char limit_switches; //x,y,z,DOOR,-,-,-,-, are these switches currently being pressed?
    };
    
void execute_diag();

#endif
/* [] END OF FILE */
