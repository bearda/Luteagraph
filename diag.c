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

#include "diag.h"

extern int x_cur_loc; //represents the current location on the x axis. 18000 is the limit switch, zero is as far as we should go in the other direction.
extern int y_cur_loc;
extern int z_cur_loc;
extern int t_cur_loc;

//this reads information and sends it back to the PI
void execute_diag()
{
    //this is a stub
    struct diagnosticMessage_t msg;
    
    msg.packet_type = 0x04;
    
    msg.x_pos = (int32) x_cur_loc; 
    msg.y_pos = (int32) y_cur_loc; 
    msg.z_pos = (int32) z_cur_loc; 
    msg.t_pos = (int32) t_cur_loc; 
    
    msg.homed = 0;
    msg.limit_switches = 0xF0;
    msg.servo_on = 0xF0;
    
    
}

/* [] END OF FILE */
