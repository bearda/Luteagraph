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
#ifndef INTERP_HEADER_H
#define INTERP_HEADER_H
#include <project.h>

#define PULSE_TABLE_SIZE 1000    
    
struct pulse_entry_t {
    char delta_t; //the time until the next pulse
    char pulse_bits; //the bits determining which pulses to send.
} pulse_entry;


int linear_interp(int stop_x, int stop_y, int stop_z);

//dequeues all the pulses, and writes a zero to the first pulse
int pulse_table_init();

int getPrevX();

#endif
/* [] END OF FILE */
