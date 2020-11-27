/****************************************************************************
**
** Copyright (C) 2017 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.0
import QtQuick.Window 2.14
import QtLocation 5.6
import QtPositioning 5.6

Window {
    width: Qt.platform.os == "android" ? Screen.width : 512
    height: Qt.platform.os == "android" ? Screen.height : 512
    visible: true

    Plugin {
        id: mapPlugin
        name: "osm" // "mapboxgl", "esri", ...
        // specify plugin parameters if necessary
        // PluginParameter {
        //     name:
        //     value:
        // }
    }

property variant startCoordinate: QtPositioning.coordinate(37.2296, -80.4139)
property variant endCoordinate: QtPositioning.coordinate(37.141030, -80.401950)


    Map {
        id: map
        anchors.fill: parent
        anchors.topMargin: -10
        anchors.rightMargin: -113
        anchors.bottomMargin: -10
        anchors.leftMargin: -113
        plugin: mapPlugin
        center: QtPositioning.coordinate(37.2296, -80.4139) // Oslo
        zoomLevel: 20

        /*MapItemView {
            model: searchModel
            delegate: MapQuickItem {
                coordinate: place.location.coordinate

                anchorPoint.x: image.width * 0.5
                anchorPoint.y: image.height

                sourceItem: Column {
                    //Image { id: image; source: "marker.png" }
                    Text { text: title; font.bold: true }
                }
            }
        }*/
	    MapCircle {
        	center {
           	 latitude: 37.2296 
           	 longitude: -80.4139
        	}
        	radius: 5.0
        	color: 'green'
        	border.width: 3
    	}

RouteModel {
    id: routeModel
    plugin : map.plugin
    query:  RouteQuery {
        id: routeQuery
    }
    onStatusChanged: {
        if (status == RouteModel.Ready) {
            switch (count) {
            case 0:
                // technically not an error
                map.routeError()
                break
            case 1:
                map.showRouteList()
                break
            }
        } else if (status == RouteModel.Error) {
            map.routeError()
        }
    }
}



MapItemView {
    model: routeModel
    delegate: routeDelegate
}

Component {
    id: routeDelegate

    MapRoute {
        id: route
        route: routeData
        line.color: "#46a2da"
        line.width: 5
        smooth: true
        opacity: 0.8
    }
}

MouseArea{
anchors.fill: parent
onClicked: {// clear away any old data in the query
routeQuery.clearWaypoints();

// add the start and end coords as waypoints on the route
routeQuery.addWaypoint(startCoordinate)
routeQuery.addWaypoint(endCoordinate)
routeQuery.travelModes = RouteQuery.CarTravel
routeQuery.routeOptimizations = RouteQuery.FastestRoute

routeModel.update();

// center the map on the start coord
map.center = startCoordinate;
}
}
    }

}
