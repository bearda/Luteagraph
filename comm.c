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
//The purpose of this file is SPI communications with the Raspberry Pi.
#include <project.h>

#include "comm.h"
#include "cmd.h"

const uint8 dummyBuffer[PACKET_SIZE] = {'a','b','c'};
const uint8 zeroBuffer[64] = {0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0,
                              0,0,0,0,0,0,0,0};
const uint8 gcode_complete_msg[2] = {cmd_gcode, 0};

uint8 gcodeBuffer[256];
uint8 gcodeLoc;
uint32 read_size = HEADER_SIZE;
uint32 transmit_size = HEADER_SIZE;

uint8 bigBuf[255];
uint8 bigBufLoc = 0;
uint8 remaining_packets = 0;

uint32 SPIS_WaitForCommand(uint8 *buf, uint32 read_size)
{
    //uint8 headBuffer[HEADER_SIZE];    
    
    uint32 cmd;
    uint32 i;
    //uint32 packet_length;

    //wait for header
    /* Wait for the end of the transfer */
    if (read_size >= HEADER_SIZE)
    {
        while (HEADER_SIZE > SPIS_SpiUartGetRxBufferSize())
        {
        }
    }
    else
    {
        return CMD_SET_UNKNOWN;
    }

    //read header
    i = 0;
    while (i < HEADER_SIZE)
    {
        buf[i] = SPIS_SpiUartReadRxData();
        i++;
    }
    
    cmd = buf[PACKET_TYPE_LOC];
    //packet_length = buf[PACKET_LENGTH_LOC];
    
    
    
    
    //wait for body
//    if (read_size >= HEADER_SIZE + packet_length)
//    {
//        while (packet_length > SPIS_SpiUartGetRxBufferSize())
//        {
//        }
//    }
//    else
//    {
//        return CMD_SET_UNKNOWN;
//    }
//    
//    //read body.
//    while (0 != SPIS_SpiUartGetRxBufferSize() && i < packet_length + HEADER_SIZE)
//    {
//        buf[i] = SPIS_SpiUartReadRxData();
//        i++;
//    }

    return (cmd);
}

/*******************************************************************************
* Function Name: SPIS_CleanupAfterRead
********************************************************************************
* Summary:
*  SPIS waits for completion of the read transfer initiated by the SPIM. The
*  received packet is discarded as it contains only dummy data. Then the SPIS
*  prepares for the following command packet by putting dummy bytes into the
*  TX buffer.
*
* Parameters:
*  None
*
* Return:
*  None
*
*******************************************************************************/
void SPIS_CleanupAfterRead(void)
{
    /* Wait for the end of the transfer */
    //while (transmit_size != SPIS_SpiUartGetRxBufferSize())
    //{
    //}

    /* Clear RX buffer from dummy bytes */
    SPIS_SpiUartClearRxBuffer();

    /* Put dummy data into TX buffer to be transmitted to SPIM */
    uint8 tmpBuf[8] = {'h','e','l','l','o','!','!','1'};
    SPIS_SpiUartPutArray(tmpBuf, 8u);
}


void SPIS_SendReply(uint8 *buffer, uint32 read_size)
{
    SPIS_SpiUartClearTxBuffer();
    SPIS_SpiUartPutArray(buffer, read_size);
    
    int i = SPIS_SpiUartGetTxBufferSize();
    while (0 != SPIS_SpiUartGetTxBufferSize())
    {
    }
    
    /* Clear RX buffer from dummy bytes */
    SPIS_SpiUartClearRxBuffer();
}

/* [] END OF FILE */
