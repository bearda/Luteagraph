/*******************************************************************************
* File Name: main.c
*
* Version: 3.00
*
* Description:
*  This is the source code for the datasheet example of the TCPWM (Timer / 
*  Counter mode) component.
*
********************************************************************************
* Copyright 2013-2015, Cypress Semiconductor Corporation. All rights reserved.
* This software is owned by Cypress Semiconductor Corporation and is protected
* by and subject to worldwide patent and copyright laws and treaties.
* Therefore, you may use this software only as provided in the license agreement
* accompanying the software package from which you obtained this software.
* CYPRESS AND ITS SUPPLIERS MAKE NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
* WITH REGARD TO THIS SOFTWARE, INCLUDING, BUT NOT LIMITED TO, NONINFRINGEMENT,
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
*******************************************************************************/

#include <project.h>
#include <cypins.h>

#include <math.h>

#include "GCode.h"
#include "interp.h"
#include "autoHome.h"
#include "comm.h"
#include "cmd.h"
#include "bit_offsets.h"
#include "heart.h"

/* LED control defines (active low)*/
#define LIGHT_OFF                       (1u)
#define LIGHT_ON                        (0u)

/* Selects the active blinking LED */
uint8 activeLed;

#define PI 3.141592

char* sampGCode =
    "G01 X249.5000\n"
    " X0.5000\n";

struct pulse_entry_t pulse_table[PULSE_TABLE_SIZE];
int pulse_table_loc = 0;
int pulse_table_size = 0;

int x_cur_loc = 0; //represents the current location on the x axis. 18000 is the limit switch, zero is as far as we should go in the other direction.
int y_cur_loc = 0;
int z_cur_loc = 0;
int t_cur_loc = 0;


float tar_x;
float tar_y;
float tar_z;

extern int prev_x;
extern int prev_y;
extern int prev_z;
extern int prev_t;

extern uint8* gcode_complete_msg;


/*******************************************************************************
* Defines the interrupt service routine and allocates a vector to the interrupt.
* We use one handler for both the Capture and Terminal Count interrupts
* We toggle the active LED upon each Terminal Count interrupt
* We toggle the color (active LED) between blue and green upon each Capture 
* interrupt
********************************************************************************/
CY_ISR(InterruptHandler)
{
    //cypress says this will clear the interrupt flag
    Timer_1_ReadStatusRegister();
    
    //do we need to get the next GCode command?
    if (pulse_table_loc >= pulse_table_size)
    {
        prev_x = x_cur_loc;
        prev_y = y_cur_loc;
        prev_z = z_cur_loc;
        prev_t = t_cur_loc;
        if (x_cur_loc != mm_to_pulses(tar_x))
        {
            pulse_table_init();
            linear_interp(mm_to_pulses(tar_x), mm_to_pulses(tar_y), mm_to_pulses(tar_z));   
        }
        else
        {
            if (runNextGCodeCommand(&tar_x,&tar_y,&tar_z) < 0)
            {
                //remember manual setting
                if (!autoHoming())
                {
                    SPIS_SendReply(gcode_complete_msg, sizeof(gcode_complete_msg));
                }
                Timer_1_Sleep();
                return;
            }
        }
    }
    
    //write one pulse for 50 micro seconds
    if (pulse_table[pulse_table_loc].pulse_bits & X_USE_MASK)
    //if (pulse_table_loc < pulse_table_size)
    {
        if (pulse_table[pulse_table_loc].pulse_bits & X_DIR_MASK && !x_limit_Read())
        //if(pulse_table_loc < pulse_table_size/2)
        {
            x_dir_output_pin_Write (1u);
            x_pulse_output_pin_Write(1u);
            x_cur_loc++;

        }
        else if ((pulse_table[pulse_table_loc].pulse_bits & X_DIR_MASK) == 0)
        {
            x_dir_output_pin_Write (0u);
            x_pulse_output_pin_Write(1u);
            x_cur_loc--;

        }

    }
    //write one pulse for 50 micro seconds
    if (pulse_table[pulse_table_loc].pulse_bits & Y_USE_MASK)
    //if (pulse_table_loc < pulse_table_size)
    {
        if (pulse_table[pulse_table_loc].pulse_bits & Y_DIR_MASK && !y_limit_Read())
        //if(pulse_table_loc < pulse_table_size/2)
        {
            y_dir_output_pin_Write (1u);
            y_pulse_output_pin_Write(1u);
            y_cur_loc++;

        }
        else if ((pulse_table[pulse_table_loc].pulse_bits & Y_DIR_MASK) == 0)
        {
            y_dir_output_pin_Write (0u);
            y_pulse_output_pin_Write(1u);
            y_cur_loc--;

        }

    }
        //write one pulse for 50 micro seconds
    if (pulse_table[pulse_table_loc].pulse_bits & Z_USE_MASK)
    //if (pulse_table_loc < pulse_table_size)
    {
        if (pulse_table[pulse_table_loc].pulse_bits & Z_DIR_MASK && !z_limit_Read())
        //if(pulse_table_loc < pulse_table_size/2)
        {
            z_dir_output_pin_Write (1u);
            z_pulse_output_pin_Write(1u);
            z_cur_loc++;

        }
        else if ((pulse_table[pulse_table_loc].pulse_bits & Z_DIR_MASK) == 0)
        {
            z_dir_output_pin_Write (0u);
            z_pulse_output_pin_Write(1u);
            z_cur_loc--;

        }

    }
    //LED_BLUE_Write(1u);
    CyDelayUs(50u);
    x_pulse_output_pin_Write(0u);
    x_dir_output_pin_Write (0u);
    y_pulse_output_pin_Write(0u);
    y_dir_output_pin_Write (0u);
    z_pulse_output_pin_Write(0u);
    z_dir_output_pin_Write (0u);

    
    //set the timer
    Timer_1_WritePeriod(pulse_table[pulse_table_loc].delta_t);
    pulse_table_loc = pulse_table_loc + 1;
    
    //check autohoming.
    char homing_bits = autoHoming(); //which axis are homing?
    if ((homing_bits & X_USE_MASK && !x_limit_Read()) ||
        (homing_bits & Y_USE_MASK && !y_limit_Read()) ||
        (homing_bits & Z_USE_MASK && !z_limit_Read()))
    {
        //do nothing. we are still homing
    }
    else
    {
        autoHomeComplete();
    }
}

//this has been multiplied by 1000. be warned.
#define ROOT_2_OVER_2 707

int main()
{   
    char cmd;
    uint8 buf[256];
    int buf_size = 256;
    
    #if (CY_PSOC4_4000)
        CySysWdtDisable();
    #endif /* (CY_PSOC4_4000) */
    

       
    x_on_Write(1u);

    /* Enable global interrupt */
    
    CyGlobalIntEnable;
    TC_CC_ISR_StartEx(InterruptHandler);
    spi_heart_StartEx(heart_beater);
    /* Start components */
    //Timer_1_Sleep();
    
    /* Enable interrupt component connected to interrupt */
    pulse_table_init();
    initGCode();
    SPIS_Start();
    //SPIS_CleanupAfterRead();
    //saveGCodeToFlash(sampGCode, strlen(sampGCode) + 1);
    //runNextGCodeCommand(&tar_x, &tar_y, &tar_z);
    
    Timer_1_Start();
    Timer_1_Sleep();
    
    heartbeat_Start();
    heartbeat_Sleep();

    for(;;)
    {
        if (!heartBeating())
        {
            cmd = SPIS_WaitForCommand(buf, buf_size);
            //execute command
            executeCmd(cmd, buf, buf_size);
            //reply to command
            
            //SPIS_UpdateStatus(0);
            //SPIS_CleanupAfterRead();
        }
    }
}


/* [] END OF FILE */
