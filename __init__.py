# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LatlonDecimal
                                 A QGIS plugin
 This plugin converts the Lat/Long to Decimal values
                             -------------------
        begin                : 2020-01-05
        copyright            : (C) 2020 by Dr.K. Ilayaraja
        email                : ilayaraja22@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LatlonDecimal class from file LatlonDecimal.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .To_Decimal import LatlonDecimal
    return LatlonDecimal(iface)
