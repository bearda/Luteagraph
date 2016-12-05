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
#ifndef COMM_H
#define COMM_H
    
#include <project.h>
     
/* Packet size */
#define PACKET_SIZE      (3u)
#define HEADER_SIZE      (2u)

/* Byte position within the packet */
#define PACKET_SOP_POS  (0u)

#define PACKET_TYPE_LOC     (0u)
#define PACKET_DATA_LOC  (1u)
    
/* Command and status share the same offset */
#define PACKET_EOP_POS  (2u)

/* Start and end of the packet markers */
#define PACKET_SOP      (0x01u)
#define PACKET_EOP      (0x17u)

/* Command execution status */
#define STS_CMD_DONE    (0x00u)
#define STS_CMD_FAIL    (0xFFu)

/* Commands */
#define CMD_SET_OFF     (0u)
#define CMD_SET_RED     (1u)
#define CMD_SET_GREEN   (2u)
#define CMD_SET_BLUE    (3u)
#define CMD_SET_UNKNOWN (0xFFu)

/* Delay between commands in milliseconds */
#define CMD_TO_CMD_DELAY  (500u)
 
uint32 SPIS_WaitForCommand(uint8 *buf, uint32 read_size);
void SPIS_CleanupAfterRead(void);
void SPIS_UpdateStatus(uint32 status);
void SPIS_SendReply(uint8 *buffer, uint32 read_size);

    
#endif
/* [] END OF FILE */
