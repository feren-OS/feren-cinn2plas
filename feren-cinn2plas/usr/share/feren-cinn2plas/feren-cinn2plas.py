#!/usr/bin/python3

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango
from os.path import expanduser

import apt
cache = apt.Cache()

class init():
    stepsdone = ""
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('feren-cinn2plas.glade')
        self.win = self.builder.get_object('MainWind')
        self.win.connect('delete-event', Gtk.main_quit)

        hbroobe = self.builder.get_object('hbr-oobe')
        self.win.set_titlebar(hbroobe)
        
        self.notebook = self.builder.get_object('MainSteps')
        
        #PangoFont = Pango.FontDescription("Tahoma 12")
        #self.win.modify_font(PangoFont)
        
        self.win.set_icon_name('distributor-logo')

        #Buttons
        self.startnextbtn = self.builder.get_object('StartNextBtn')
        self.startnextbtn.connect('clicked', self.btn_next_click)
        #self.startnextbtn.connect('draw', self.btn_focused)
        self.backbtn = self.builder.get_object('BackBtn')
        self.backbtn.connect('clicked', self.btn_back_click)
        self.backbtn.set_visible(False)
        self.nevershowagain = self.builder.get_object('NeverShowAgainBtn')
        self.nevershowagain.connect('clicked', self.btn_nevershowagain_click)
        self.screenshotsbtn = self.builder.get_object('ScreenshotsBtn')
        self.screenshotsbtn.connect('clicked', self.screenshots_click)
        self.bkupconfigsbtn = self.builder.get_object('BkupConfigsBtn')
        self.bkupconfigsbtn.connect('clicked', self.btn_bkupconfigs_click)
        self.switchtoplasmabtn = self.builder.get_object('SwitchToPlasmaBtn')
        self.switchtoplasmabtn.connect('clicked', self.btn_switchtoplasma_click)
        self.delayplasmaswitchbtn = self.builder.get_object('DelayPlasmaSwitchBtn')
        self.delayplasmaswitchbtn.connect('clicked', self.btn_dismiss_click)

        #Labels
        self.welcomelbl = self.builder.get_object('WelcomeLbl')
        self.welcomelbl2 = self.builder.get_object('WelcomeLbl2')
        self.welcomelbl3 = self.builder.get_object('WelcomeLbl3')

        self.themepreflbl = self.builder.get_object('ThemePrefLbl')
        self.themepreflbl2 = self.builder.get_object('ThemePrefLbl2')

        self.codecslbl1 = self.builder.get_object('CodecsLbl1')
        self.codecslbl2 = self.builder.get_object('CodecsLbl2')
        self.codecslbl4 = self.builder.get_object('CodecsLbl4')
        
    ### Buttons ###
    def btn_next_click(self, button):      
        self.notebook.next_page()
        if self.notebook.get_current_page() >= 1:
            self.backbtn.set_visible(True)
        else:
            self.backbtn.set_visible(False)
        if self.notebook.get_current_page() == 3:
            self.startnextbtn.set_visible(False)
        else:
            self.startnextbtn.set_visible(True)

    def btn_back_click(self, button):
        self.notebook.prev_page()
        if self.notebook.get_current_page() >= 1:
            self.backbtn.set_visible(True)
        else:
            self.backbtn.set_visible(False)
        if self.notebook.get_current_page() == 3:
            self.startnextbtn.set_visible(False)
        else:
            self.startnextbtn.set_visible(True)
            
    def btn_dismiss_click(self, button):
        Gtk.main_quit()
        
    def btn_nevershowagain_click(self, button):
        self.notebook.set_sensitive(False)
        os.system("/usr/bin/feren-cinn2plas goaway")
        self.notebook.set_sensitive(True)
        Gtk.main_quit()

    def screenshots_click(self, button):
        os.system("xdg-open https://ferenos.weebly.com/plasma-screenshots")
        
    def btn_bkupconfigs_click(self, button):
        self.notebook.set_sensitive(False)
        os.system("/usr/bin/pkexec /usr/bin/feren-cinnamon-backup")
        self.notebook.set_sensitive(True)

    def btn_switchtoplasma_click(self, button):
        self.notebook.set_sensitive(False)
        os.system("/usr/bin/feren-cinn2plas transition")
        self.notebook.set_sensitive(True)
        Gtk.main_quit()

    ### SHOW APP ###
    def run(self):
        self.win.set_auto_startup_notification(False)
        self.win.show_all()
        self.win.set_auto_startup_notification(True)
        self.startnextbtn.grab_focus()
        self.backbtn.set_visible(False)
        Gtk.main()

if __name__ == '__main__':
    usettings = init()
    usettings.run()
