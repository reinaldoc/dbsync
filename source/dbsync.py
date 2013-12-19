#!/usr/bin/python
# -*- coding: utf-8 -*-
# dbsync 0.1 - A synchronization framework
# Copyright (c) 2013 - Reinaldo Gil Lima de Carvalho <reinaldoc@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License only
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

"""
dbsync - A synchronization framework

"""

__author__ =  'Reinaldo Gil Lima de Carvalho'
__version__=  '0.1'

from util.Message import Info
from controller.SyncBC import SyncBC

if __name__ == '__main__':
	for sync_section in SyncBC.get_sync_sections():

		Info("Synchronizing '%s'..." % sync_section)
		s_handle = SyncBC.get_source_handle(sync_section)
		d_handle = SyncBC.get_dest_handle(sync_section)

		for data in s_handle.load():
			data = SyncBC.convert(sync_section, data)
			d_handle.sync(sync_section, data)
		d_handle.flush()
