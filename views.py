#!/usr/bin/env python
# 
# Copyright (c) 2008-2012 University of Dundee.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.shortcuts import render_to_response
from django.http import Http404

from omeroweb.webclient import webclient_gateway
from omeroweb.decorators import login_required


def index(request):
    return Http404("Index page not supported")


@login_required()    # wrapper handles login (or redirects to webclient login). Connection passed in **kwargs
def dataset(request, datasetId, conn=None, **kwargs):
    """ 'Hello World' example from tutorial on http://trac.openmicroscopy.org.uk/ome/wiki/OmeroWeb """
    ds = conn.getObject("Dataset", datasetId)     # before OMERO 4.3 this was conn.getDataset(datasetId)

    if ds is None:
        return Http404("Dataset not found")

    return render_to_response('webtemplate/dataset.html', {'dataset': ds})    # generate html from template
