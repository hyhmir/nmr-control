##################################
# RUN THIS FILE TO START THE APP #
##################################

# import everything necessary
import subprocess
import tmag
import maingui

# testing something


if __name__ == "__main__":
    tecmag = tmag.tecmag.Tecmag()
    tecmag.Parameter_setup()
    gui = maingui.main.NMR_GUI(tecmag)
    gui.mainloop()
    tecmag.app.Abort
    tecmag.app.CloseActiveFile
    tecmag.app.CloseActiveFile
    subprocess.call("TASKKILL /F /IM TNMR.exe", shell=True)
