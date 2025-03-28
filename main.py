##################################
# RUN THIS FILE TO START THE APP #
##################################

# import everything necessary
import subprocess
from tmag import Tecmag
from maingui import NMR_GUI



if __name__ == "__main__":
    tecmag = Tecmag()
    tecmag.Parameter_setup()
    gui = NMR_GUI(tecmag)
    gui.mainloop()
    tecmag.app.Abort
    tecmag.app.CloseActiveFile
    tecmag.app.CloseActiveFile
    subprocess.call("TASKKILL /F /IM TNMR.exe", shell=True)
