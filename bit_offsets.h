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

#ifndef BITS_H
#define BITS_H

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

#endif
/* [] END OF FILE */
