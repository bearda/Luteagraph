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
#include <math.h>

#include "interp.h"
#include "bit_offsets.h"


//we only want to go 1000 pulses in one second.
#define MAX_SPEED 100

int prev_x = 0;
int prev_y = 0;
int prev_z = 0;
int prev_t = 0;

extern struct pulse_entry_t pulse_table[PULSE_TABLE_SIZE];
extern int pulse_table_loc;
extern int pulse_table_size;

int linear_interp(int stop_x, int stop_y, int stop_z)
{
    int D_x; //the total change between prev_x and stop_x
    int D_y;
    int D_z;
    int d_x; //are we sending positive or negative pulses?
    int d_y;
    int d_z;
    int err_x; //the amount of error in X. accumulates every time we move our parameter forward.
    int d_err_x; //the amount by which err_x increments.
    int err_y;
    int d_err_y;
    int err_z;
    int d_err_z;
    int r; //the length from the start position to the stop position
    int r_2; //r^2
    int i; //the number of pulses we queued
    
    char keepGoing = 0; //we will just add all the motors we are using
    char pulse_char; //the pulse bits (4 use bits, 4 dir bits)
    char x_dir_mask; //equals X_DIR_MASK if we are incrementing X, 0 otherwise
    char y_dir_mask;
    char z_dir_mask;
    
    //I know my start point. I know my end point. I know how fast I want to go.
    if (stop_x != -1)
    {
        D_x = stop_x - prev_x;
        if (D_x > 0)
        {
            d_x = 1;
            keepGoing += X_USE_MASK;
            x_dir_mask = X_DIR_MASK;
        }
        else if (D_x < 0)
        {
            d_x = -1;
            keepGoing += X_USE_MASK;
            x_dir_mask = 0;
        }
    }
    else
    {
        D_x = 0;
        
    }   
    if (stop_y != -1)
    {
        D_y = stop_y - prev_y;
        
        if (D_y > 0)
        {
            d_y = 1;
            keepGoing += Y_USE_MASK;
            y_dir_mask = Y_DIR_MASK;
        }
        else if (D_y < 0)
        {
            d_y = -1;
            keepGoing += Y_USE_MASK;
            y_dir_mask = 0;
        }
    }
    else
    {
        D_y = 0;
    }   
    if (stop_z != -1)
    {
        D_z = stop_z - prev_z;
        
        if (D_z > 0)
        {
            d_z = 1;
            keepGoing += Z_USE_MASK;
            z_dir_mask = Z_DIR_MASK;
        }
        else if (D_z < 0)
        {
            d_z = -1;
            keepGoing += Z_USE_MASK;
            z_dir_mask = 0;
        }
    }
    else
    {
        D_z = 0;
    }
    
    r_2 = D_x*D_x + D_y*D_y + D_z*D_z;
    r = (int) sqrt(r_2);
    
    d_err_x = (int) 1000 * (D_x / (1.0 * r));
    d_err_y = (int) 1000 * (D_y / (1.0 * r));
    d_err_z = (int) 1000 * (D_z / (1.0 * r));
    
    d_err_x = (d_err_x > 0) ? d_err_x : d_err_x * (-1);
    d_err_y = (d_err_y > 0) ? d_err_y : d_err_y * (-1);
    d_err_z = (d_err_z > 0) ? d_err_z : d_err_z * (-1);

    i = 0;
    err_x = 0;
    err_y = 0;
    err_z = 0;
    
    while (keepGoing)
    {
        i += 1;
        err_x += d_err_x;
        err_y += d_err_y;
        err_z += d_err_z;
        pulse_char = 0;


        if (err_x > 1000 && (keepGoing & X_USE_MASK))
        {
            err_x -= 1000;
            prev_x += d_x;
            pulse_char += X_USE_MASK + x_dir_mask;
            if (prev_x == stop_x)
            {
                keepGoing -= X_USE_MASK;
            }
        }
        if (err_y > 1000 && (keepGoing & Y_USE_MASK))
        {
            err_y -= 1000;
            prev_y += d_y;
            pulse_char += Y_USE_MASK + y_dir_mask;
            if (prev_y == stop_y)
            {
                keepGoing -= Y_USE_MASK;
            }
        }
        if (err_z > 1000 && (keepGoing & Z_USE_MASK))
        {
            err_z -= 1000;
            prev_z += d_z;
            pulse_char += Z_USE_MASK + z_dir_mask;
            if (prev_z == stop_z)
            {
                keepGoing -= Z_USE_MASK;
            }
        }
        pulse_table[pulse_table_size].pulse_bits = pulse_char;
        pulse_table[pulse_table_size].delta_t = 55; //(char) (100.0 * sqrt(r_2) / cur_pri);
        pulse_table_size++;
        if (pulse_table_size >= PULSE_TABLE_SIZE)
        {
            keepGoing = 0; //we ran out of room. we give up.
        }
        
    }
    return i;
}


//dequeues all the pulses, and writes a zero to the first pulse
int pulse_table_init()
{
    pulse_table_loc = 0;
    pulse_table_size = 0;
    pulse_table[pulse_table_loc].delta_t = 0;
    pulse_table[pulse_table_loc].pulse_bits = 0;
    return 0;
}

//getters and setters
int getPrevX()
{
    return prev_x;
}

/* [] END OF FILE */
