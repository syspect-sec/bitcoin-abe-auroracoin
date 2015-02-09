# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .Sha256Chain import Sha256Chain

class Auroracoin(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Auroracoin'
        chain.code3 = 'AUR'
        chain.address_version = '\u0017'
        chain.script_addr_vers = '\u0017'
        chain.magic = 'u00fau00bfu00b5u00da'
        Sha256Chain.__init__(chain, **kwargs)
	datadir_conf_file_name = "AuroraCoin.conf"
	datadir_rpcport = 12341

#normal format for magic number
#\x70\x35\x22\x05

#Auroracoin majic number from main.cpp { 0xfd, 0xa4, 0xdc, 0x6c }
#u00fdu00a4u00dcu006c
# from chainparams in the Auroracoin-core: { 0xeb, 0xb0, 0xa6, 0xcb }
#u00ebu00b0u00a6u00cb

# also from chainparams in the Auroracoin-core { 0xfa, 0xbf, 0xb5, 0xda }



