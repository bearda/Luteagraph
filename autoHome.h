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
#ifndef AUTO_HOME_HEADER
#define AUTO_HOME_HEADER

//this will tell the runNextGCodeCommand that we are autohoming
void autoHome( char homing_bits);
void autoHomeComplete();

//are we currently trying to autohome?
char autoHoming();

#endif

/* [] END OF FILE */
