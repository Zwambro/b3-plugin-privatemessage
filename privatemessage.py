#
# ################################################################### #
#                                                                     #
#  Private message Plugin for BigBrotherBot(B3)                       #
#  Copyright (c) 2018 Ouchekkir Abdelmouaine                          #
#                                                                     #
#  This program is free software; you can redistribute it and/or      #
#  modify it under the terms of the GNU General Public License        #
#  as published by the Free Software Foundation; either version 2     #
#  of the License, or (at your option) any later version.             #
#                                                                     #
#  This program is distributed in the hope that it will be useful,    #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the       #
#  GNU General Public License for more details.                       #
#                                                                     #
#  You should have received a copy of the GNU General Public License  #
#  along with this program; if not, write to the Free Software        #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA      #
#  02110-1301, USA.                                                   #
#                                                                     #
# ################################################################### #
#
#
#  CHANGELOG:
#  02.11.2018 - v1.0 - ZOMBIE
#  - first release.
#

__author__ = 'ZOMBIE'
__version__ = '1.0'


import b3
import b3.events
import b3.plugin
from b3 import functions


class PrivatemessagePlugin(b3.plugin.Plugin):
    requiresConfigFile = False

    def onStartup(self):

        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.debug('Could not find admin plugin')
            return False
        else:
            self.debug('Plugin loaded normal')

        self._adminPlugin.registerCommand(self, 'pm', 0, self.cmd_pm)
        self.debug('Pm Command registered in admin plugin')

    def cmd_pm(self, data, client, cmd=None):

        #!pm <player> <message>

        if data:

            input = self._adminPlugin.parseUserCmd(data)

        else:

            client.message('^1Incorrect syntax. !pm <playername> <message>^7')
            return False

        sclient = self._adminPlugin.findClientPrompt(input[0], client)

        message = input[1]

        if not sclient:

            return False

        if not message:

            client.message('^1Incorrect syntax. !pm <playername> <message>^7')
            return False

        if sclient:

            sclient.message('%s^7[^3PM^7]: %s' % (client.exactName, message))
            return True

        else:
            return False
