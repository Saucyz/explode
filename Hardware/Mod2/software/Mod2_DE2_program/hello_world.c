#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "altera_up_avalon_character_lcd.h"
//#include "sys/alt_timestamp.h"
#include <altera_up_sd_card_avalon_interface.h>
#include "altera_up_avalon_audio.h"
#include "altera_up_avalon_audio_and_video_config.h"
#include <priv/alt_legacy_irq.h>
#include "system.h"
#include "altera_avalon_timer.h"
#include "fcntl.h"
#include "altera_avalon_pio_regs.h"

#define switches (volatile char *) 0x0002010
#define leds (char *) 0x0002000
#define keys (volatile char *) 0x0002040
#define freq 50000000

void av_config_setup();
void isr_timer(void*, alt_u32);

char state[2] = "c";
char *isComplete = "F";
int ans = 0;

alt_up_character_lcd_dev * char_lcd_dev;

int main() {
  printf("Hello from Nios II!\n");
  printf("Confirming the program is loaded and working...\n");

  alt_up_audio_dev* audio_dev;

  // open the Character LCD port
  char_lcd_dev = alt_up_character_lcd_open_dev ("/dev/character_lcd_0");
  if ( char_lcd_dev == NULL)
	printf ("Error: could not open character LCD device\n");
  else
	printf ("Opened character LCD device\n");
  // Initialize the character display
  alt_up_character_lcd_init (char_lcd_dev);

  // open the Audio port
  audio_dev = alt_up_audio_open_dev("/dev/audio_0");
  if(audio_dev == NULL)
	printf ("Error: could not open audio device\n");
  else
	printf ("Opened audio device\n");
  //Initialize Audio device
  av_config_setup();
  alt_up_audio_reset_audio_core(audio_dev);	//reset read write left and right buffers

  alt_up_character_lcd_string(char_lcd_dev, "SHIT BE WORKING");
  alt_up_character_lcd_set_cursor_pos(char_lcd_dev, 0, 1);

  //setup serial port comms
  int fp = open(UART_0_NAME, O_NONBLOCK | O_RDWR);

  //set the period for the interrupt
  //for now 1 time per second
  IOWR_16DIRECT(TIMER_0_BASE, 8, freq & 0x0000ffff);
  IOWR_16DIRECT(TIMER_0_BASE, 12, (freq & 0xffff0000) >> 16);

  //enable interrupts for timer
  IOWR_16DIRECT(TIMER_0_BASE, 0x4, 0x7);

  //setup timer interrupt
  alt_irq_register(TIMER_0_IRQ, (void*)fp, isr_timer);

  alt_irq_enable(TIMER_0_IRQ);

  while(1){
	  /*
	  ans = IORD_ALTERA_AVALON_PIO_DATA(KEYS_BASE);
	  if(ans == 1){
		  isComplete = "T";
	  }
	  */
	  //alt_up_character_lcd_init (char_lcd_dev);
	  //alt_up_character_lcd_string(char_lcd_dev, state);
  }

  return 0;
}

void av_config_setup(){
	alt_up_av_config_dev * audio_config = alt_up_av_config_open_dev("/dev/audio_config");
	while(!alt_up_av_config_read_ready(audio_config)){
		alt_printf("waiting");
	}
	return;
}

char *msg = "s";

void isr_timer(void* context, alt_u32 irq){
	int fp = (int)context;
	int expecting = 1;
	int gotc;
	unsigned char c;

	while(expecting){
		gotc = read(fp, &c, expecting);
		if(gotc > 0){
			expecting -= gotc;
		}
	}

	char * cstring[] = {c, '\0'};

	write(fp, msg, strlen(msg));

	alt_up_character_lcd_init(char_lcd_dev);
	alt_up_character_lcd_string(char_lcd_dev, "Getting: ");
	alt_up_character_lcd_string(char_lcd_dev, cstring);
	alt_up_character_lcd_set_cursor_pos(char_lcd_dev, 0, 1);
	alt_up_character_lcd_string(char_lcd_dev, "Mod ");
	alt_up_character_lcd_string(char_lcd_dev, isComplete);
	alt_up_character_lcd_string(char_lcd_dev, " Ans ");
	alt_up_character_lcd_string(char_lcd_dev, ans);
	//alt_up_character_lcd_string(char_lcd_dev, ".");
	//clear TO register of timer to return to normal operations
	IOWR_16DIRECT(TIMER_0_BASE, 0, 0x0);
}
