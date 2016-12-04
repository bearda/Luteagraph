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

const uint8 dummyBuffer[PACKET_SIZE] = {'a','b','c'};
const uint8 zeroBuffer[PACKET_SIZE] = {0,0,0};

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
    uint32 packet_length;

    //wait for header
    /* Wait for the end of the transfer */
    while (read_size != SPIS_SpiUartGetRxBufferSize())
    {
    }

    //read header
    i = 0u;
    while (0u != SPIS_SpiUartGetRxBufferSize())
    {
        buf[i] = SPIS_SpiUartReadRxData();
        i++;
    }
    
    cmd = buf[PACKET_TYPE_LOC];
    packet_length = buf[PACKET_LENGTH_LOC];
    
    
    
    
    //wait for body
    //while (packet_length != SPIS_SpiUartGetRxBufferSize())
    //{
    //}
    //read body.
    /* Read packet from the buffer */
    //i = 0u;
    //while (0u != SPIS_SpiUartGetRxBufferSize())
    //{
    //    buf[i] = SPIS_SpiUartReadRxData();
    //    i++;
    //}

    /* Check start and end of packet markers */
    //if ((tmpBuffer[PACKET_SOP_POS] == PACKET_SOP) &&
    //    (tmpBuffer[PACKET_EOP_POS] == PACKET_EOP))
    //{
    //    /* Return command */
    //    cmd = tmpBuffer[PACKET_CMD_POS];
    //}
    //else
    //{
    //    /* Incorrect packet format, return unknown command */
    //    cmd = CMD_SET_UNKNOWN;
    //}

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

/*******************************************************************************
* Function Name: SPIS_UpdateStatus
********************************************************************************
* Summary:
*  SPIS copies packet with response into the buffer.
*
* Parameters:
*  status - status to insert into the response packet.
*
* Return:
*  None
*
*******************************************************************************/
void SPIS_UpdateStatus(uint32 status)
{
    static uint8 sTxBuffer[PACKET_SIZE] = {32, STS_CMD_FAIL, 32};

    sTxBuffer[PACKET_STS_POS] = (uint8) remaining_packets + 48;

    /* Put data into the slave TX buffer to be transferred while following
    * master access.
    */
    if (status == 111)
    {
        uint8 tmpBuf[8] = {'h','e','l','l','o','!','!','1'};
        SPIS_SpiUartPutArray(tmpBuf, 8u);
    }
    else
    {
        SPIS_SpiUartPutArray(sTxBuffer, PACKET_SIZE);
    }
}
/* [] END OF FILE */
