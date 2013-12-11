#!/usr/bin/python
# -*- coding: utf-8 -*-
# ldapsync v2013-alpha
# Copyright (c) 2013 - Reinaldo Gil Lima de Carvalho <reinaldoc@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


from util.Message import Info
from util.Message import Debug

from controller.SyncBC import SyncBC
from controller.ConnectionBC import ConnectionBC

for sync_section in SyncBC().get_sync_sections():

	Info("Synchronizing '%s'..." % sync_section)

	s_handle = ConnectionBC.get_source_handle(sync_section)
	d_handle = ConnectionBC.get_dest_handle(sync_section)

	for row in s_handle.load():
		d_handle.sync(sync_section, row)
