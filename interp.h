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
    
#define PBIT_USE 4
#define PBIT_DIR 0

#define PBIT_X_LOC 3
#define PBIT_Y_LOC 2
#define PBIT_Z_LOC 1
#define PBIT_T_LOC 0
    
#define X_USE_MASK (1 << (PBIT_USE + PBIT_X_LOC))
#define Y_USE_MASK (1 << (PBIT_USE + PBIT_Y_LOC))
#define Z_USE_MASK (1 << (PBIT_USE + PBIT_Z_LOC))
#define T_USE_MASK (1 << (PBIT_USE + PBIT_T_LOC))

#define X_DIR_MASK (1 << (PBIT_DIR + PBIT_X_LOC))
#define Y_DIR_MASK (1 << (PBIT_DIR + PBIT_Y_LOC))
#define Z_DIR_MASK (1 << (PBIT_DIR + PBIT_Z_LOC))
#define T_DIR_MASK (1 << (PBIT_DIR + PBIT_T_LOC))

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
