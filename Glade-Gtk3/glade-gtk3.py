#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class NomePrograma(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("glade.glade")
        self.window = builder.get_object("window1")
        self.window.show()
        self.objeto = builder.get_object("nomeObjeto")
        self.about = builder.get_object("aboutdialog1")
        builder.connect_signals({
            "gtk_main_quit": Gtk.main_quit,
            "on_about_activate": self.about_window,
            "on_nomeObjeto_clicked": self.def_sinal,
            })
        
    def def_sinal(self, widget):
        print("on_nomeObjeto_clicked")

    def about_window(self, widget):
        self.about.run()
        self.about.hide()

if __name__ == "__main__":
    app = NomePrograma()
    Gtk.main()
