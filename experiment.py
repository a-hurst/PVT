# -*- coding: utf-8 -*-

__author__ = "Austin Hurst"

import klibs
from klibs import P
from klibs.KLGraphics import fill, blit, flip
from klibs.KLTime import CountDown
from klibs.KLCommunication import message
from klibs.KLResponseCollectors import KeyPressResponse
from klibs.KLUserInterface import ui_request, any_key

import random


class PVT(klibs.Experiment):

    def setup(self):

        # Add large font size style for PVT counter
        self.txtm.add_style('PVT', '1.0deg')
        
        # Set up and configure ResponseCollector for detection responses
        self.rc.uses(KeyPressResponse)
        self.rc.display_callback = self.response_callback
        self.rc.keypress_listener.key_map = {' ': 'detection'}
        self.rc.keypress_listener.interrupts = True


    def block(self):
        
        # Show block start message and wait for input before starting block
        start_msg = message("Press any key to start.", blit_txt=False)
        fill()
        blit(start_msg, 5, P.screen_c)
        flip()

        any_key() # wait for keypress before continuing


    def setup_response_collector(self):
        pass


    def trial_prep(self):
        
        # Randomly generate inter-target interval and add event to EventManager
        self.interstim_interval = random.uniform(2.0, 10.0) * 1000
        self.evm.register_ticket(['target_on', self.interstim_interval])
        

    def trial(self):
        
        # Clear screen and wait for target onset
        fill()
        flip()
        while self.evm.before('target_on'):
            ui_request()
        
        # Start timer and collect response
        self.rc.collect()
        response = self.rc.keypress_listener.response()
        
        # Stop timer and show for 1sec after response is made
        elapsed_msg = message(str(int(response.rt)).zfill(4), style='PVT', blit_txt=False)
        feedback_timer = CountDown(1)
        while feedback_timer.counting():
            fill()
            blit(elapsed_msg, 5, P.screen_c)
            flip()
        
        # Log trial data to database
        return {
            "block_num": P.block_number,
            "trial_num": P.trial_number,
            "isi": self.interstim_interval,
            "rt": response.rt
        }


    def trial_clean_up(self):
        pass

    def clean_up(self):
        pass
        
    def response_callback(self):
        # Get time elapsed since callback start
        try:
            elapsed = int(self.evm.trial_time_ms - self.rc.rc_start_time)
        except TypeError: # if on first flip, before rc_start_time set
            elapsed = 0
        
        # Pad time elapsed with zeroes and render to text
        elapsed_msg = message(str(elapsed).zfill(4), style='PVT', blit_txt=False)
        
        # Draw time elapsed to screen
        fill()
        blit(elapsed_msg, 5, P.screen_c)
        flip()
