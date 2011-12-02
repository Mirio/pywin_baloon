#                                    LICENSE BSD 2 CLAUSE                                       #
#   Copyright 2011 Mirio. All rights reserved.                                                  #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        #

__version__ = "1.0"

import sys
import time
import os
from PyQt4.QtGui import QMainWindow, QSystemTrayIcon, QSystemTrayIcon 
from PyQt4.QtGui import QApplication, QIcon
class sysBaloon(QMainWindow):
    def baloon(self, t, m, tm=50000):
        self.trayicon = QSystemTrayIcon(self)
        if self.trayicon.supportsMessages():
            icona = QIcon('py.ico')
            self.trayicon.setIcon(icona)
            self.trayicon.show()
            self.trayicon.showMessage(t, m, msecs=tm)
            time.sleep(10)
            self.trayicon.hide()
        else:
            print "This Function isn't supported."
            choose = raw_input("Would you enable it? Y/N \n --> ")
            if choose == "Y":
                shell = os.popen('enable_baloon.reg')
                print "Run again this program"
            elif choose == "N":
                print "You don't use this program without baloon enabled."
            else:
                print "You have insert wrong char."
            
app = QApplication(sys.argv)
get_baloon = sysBaloon()
