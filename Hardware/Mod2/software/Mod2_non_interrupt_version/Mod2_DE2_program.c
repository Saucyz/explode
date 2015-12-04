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
#include "io.h"

#define switches (volatile char *) 0x0002010
#define leds (char *) 0x0002000
#define keys (volatile char *) 0x0002040
#define freq 50000000

void av_config_setup();
void timer_isr(void*, alt_u32);
void audio_isr(void*, alt_u32);

volatile char *isComplete = "F";
volatile int ans = 0;
volatile int global_count;
int audio_buf[64];

alt_up_character_lcd_dev * char_lcd_dev;
int amp = 5000;

alt_up_audio_dev* audio_dev;

int main() {
  printf("Hello from Nios II!\n");
  printf("Confirming the program is loaded and working...\n");


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

	int i;
	for(i = 0; i < 32; i++){
		audio_buf[i] = amp;
	}
	for(i = 32; i < 64; i++){
		audio_buf[i] = -amp;
	}

  //set the period for the interrupt
  //1 time per second
  IOWR_16DIRECT(TIMER_0_BASE, 8, freq & 0x0000ffff);
  IOWR_16DIRECT(TIMER_0_BASE, 12, (freq & 0xffff0000) >> 16);

  //enable interrupts for timer
  IOWR_16DIRECT(TIMER_0_BASE, 0x4, 0x7);

  //setup timer interrupt
  alt_irq_register(TIMER_0_IRQ, (void*)TIMER_0_BASE, timer_isr);
  alt_irq_register(AUDIO_0_IRQ, (void*)audio_dev, audio_isr);

  alt_up_audio_disable_write_interrupt(audio_dev);
  alt_irq_enable(TIMER_0_IRQ);
  alt_irq_enable(AUDIO_0_IRQ);

  global_count = 0;

  int expecting = 1;
  int gotc;
  char* cstring = "U";
  int prev_ans = -1;
  int change = 0;

  while(1){
	ans = IORD(SWITCHES_BASE, 0);
	if(prev_ans != ans){
		change = 1;
		if(ans == 0x1){
			isComplete = "T";
			write(fp, isComplete, strlen(isComplete));
		} else if (ans != 0x0){
			isComplete = "S";
			write(fp, isComplete, strlen(isComplete));
			//isComplete = "F";
		} else {
			isComplete = "F";
			write(fp, isComplete, strlen(isComplete));
		}
	}


/*
	while(expecting){
		gotc = read(fp, cstring, expecting);
		if(gotc > 0){
			expecting -= gotc;
		}
	}
	expecting = 1;
*/
	gotc = read(fp, cstring, expecting);

	if (strcmp(cstring,  "L") == 0){
		alt_irq_disable(TIMER_0_IRQ);
		alt_up_audio_disable_write_interrupt(audio_dev);
		alt_up_character_lcd_init(char_lcd_dev);
		alt_up_character_lcd_string(char_lcd_dev, "You Lose...");
		return 0;
	}

	if (strcmp(cstring, "W") == 0){
		alt_irq_disable(TIMER_0_IRQ);
		alt_up_audio_disable_write_interrupt(audio_dev);
		alt_up_character_lcd_init(char_lcd_dev);
		alt_up_character_lcd_string(char_lcd_dev, "You Win!!!");
		return 0;
	}

	if(change == 1){
		alt_up_character_lcd_init(char_lcd_dev);
		alt_up_character_lcd_string(char_lcd_dev, "Getting: ");
		alt_up_character_lcd_string(char_lcd_dev, cstring);
		alt_up_character_lcd_set_cursor_pos(char_lcd_dev, 0, 1);
		alt_up_character_lcd_string(char_lcd_dev, "Mod ");
		alt_up_character_lcd_string(char_lcd_dev, isComplete);
		alt_up_character_lcd_string(char_lcd_dev, " Ans ");
		char istring[2];
		istring[0]=ans + '0';
		istring[1]='\0';
		alt_up_character_lcd_string(char_lcd_dev, istring);
		change = 0;
  	}
	prev_ans = ans;
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

void timer_isr(void *context, alt_u32 isr){
	alt_up_audio_enable_write_interrupt(audio_dev);
	global_count = 0;
	IOWR(context, 0,0);
}

#define TONE_LENGTH 8000

void audio_isr(void *context, alt_u32 isr){
	alt_up_audio_write_fifo(audio_dev, audio_buf, 64, ALT_UP_AUDIO_LEFT);
	alt_up_audio_write_fifo(audio_dev, audio_buf, 64, ALT_UP_AUDIO_RIGHT);

	global_count += 64;
	if(global_count >= TONE_LENGTH){
		alt_up_audio_disable_write_interrupt(audio_dev);
	}
}
