# -*- coding: utf-8 -*-

__author__ = "Austin Hurst"

import random

import klibs
from klibs import P
from klibs.KLText import add_text_style
from klibs.KLGraphics import fill, blit, flip
from klibs.KLTime import CountDown
from klibs.KLCommunication import message
from klibs.KLResponseListeners import KeypressListener
from klibs.KLUserInterface import ui_request, any_key



class PVT(klibs.Experiment):

    def setup(self):

        # Add large font size style for PVT counter
        add_text_style('PVT', '1.0deg')

        # Set up keypress listener
        self.key_listener = KeypressListener(
            {"space": "detection"}, timeout=10, loop_callback=self.pvt_callback
        )


    def block(self):
        
        # Show block start message and wait for input before starting block
        start_msg = message("Press any key to start.")
        fill()
        blit(start_msg, 5, P.screen_c)
        flip()

        any_key() # wait for keypress before continuing


    def trial_prep(self):
        
        # Randomly generate inter-target interval and add event to EventManager
        self.interstim_interval = random.uniform(2.0, 10.0) * 1000
        self.evm.add_event('target_on', self.interstim_interval)


    def trial(self):
        
        # Clear screen and wait for target onset
        fill()
        flip()
        while self.evm.before('target_on'):
            ui_request()

        # Start timer and collect response
        self.pvt_callback() # Draw timer with 0000 to screen
        response, rt = self.key_listener.collect()
        
        # Stop timer and show reaction time for 1 sec after response is made
        feedback = str(int(rt)) if response else "XXXX"
        elapsed_msg = message(feedback.zfill(4), style='PVT')
        fill()
        blit(elapsed_msg, 5, P.screen_c)
        flip()
        feedback_timer = CountDown(1)
        while feedback_timer.counting():
            ui_request()
        
        # Log trial data to database
        return {
            "block_num": P.block_number,
            "trial_num": P.trial_number,
            "isi": self.interstim_interval,
            "rt": rt,
        }

        
    def pvt_callback(self):
        # Pad time elapsed with zeroes and render to text
        elapsed = str(int(self.key_listener.elapsed)).zfill(4)
        elapsed_msg = message(elapsed, style='PVT')

        # Draw time elapsed to screen
        fill()
        blit(elapsed_msg, 5, P.screen_c)
        flip()
