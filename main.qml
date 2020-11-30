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
import QtQuick.Controls 1.4

Window {
    width: Qt.platform.os == "android" ? Screen.width : 750
    height: Qt.platform.os == "android" ? Screen.height : 750
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
//    property variant endCoordinate: QtPositioning.coordinate(37.141030, -80.401950)

    Map {
            id: map
            anchors.fill: parent
            anchors.topMargin: -10
            anchors.rightMargin: -113
            anchors.bottomMargin: -10
            anchors.leftMargin: -113
            plugin: mapPlugin
            center: QtPositioning.coordinate(37.2296, -80.4139)
            zoomLevel: 20
            property var startCoordinate1: QtPositioning.coordinate(37.2296, -80.4139)
            property var endCoordinate1: QtPositioning.coordinate(37.2296, -80.4139)

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



            GeocodeModel {
                id: geocodeModel
                plugin: map.plugin
                autoUpdate: false
                property var f: 4
        //            onStatusChanged: {
        //                if ((status == GeocodeModel.Ready) || (status == GeocodeModel.Error))
        //                    mapgeocodeFinished()
        //            }
                onLocationsChanged:
                {
                    if (count == 1) {
                        map.center.latitude = get(0).coordinate.latitude
                        map.center.longitude = get(0).coordinate.longitude
                        //map.startCoordinate1 = QtPositioning.coordinate(get(0).coordinate.latitude, get(0).coordinate.longitude)
                        startCoordinate = get(0).coordinate
                        map.startCoordinate1 = (get(0).coordinate)
                        geocodeModel.f = map.startCoordinate1
                        console.log("GEOCODE: ", map.startCoordinate1)
                    }
                }
            }


        MapItemView {
            model: geocodeModel
            delegate: pointDelegate
        }

        Component {
            id: pointDelegate

            MapCircle {
                id: point
                radius: 100
                color: "#46a2da"
                border.color: "#190a33"
                border.width: 2
                smooth: true
                opacity: 0.25
                center: locationData.coordinate
            }
        }

        GeocodeModel {
            id: geocodeModel1
            plugin: map.plugin
//            onStatusChanged: {
//                if ((status == GeocodeModel.Ready) || (status == GeocodeModel.Error))
//                    map.geocodeFinished()
//            }
            onLocationsChanged:
            {
                if (count == 1) {
                    map.center.latitude = get(0).coordinate.latitude
                    map.center.longitude = get(0).coordinate.longitude
                    map.endCoordinate1 = QtPositioning.coordinate(get(0).coordinate.latitude, get(0).coordinate.longitude)
                }
            }
        }

        MapItemView {
            model: geocodeModel1
            delegate: pointDelegate1
        }

        Component {
            id: pointDelegate1

            MapCircle {
                id: point
                radius: 100
                color: "#46a2da"
                border.color: "#190a33"
                border.width: 2
                smooth: true
                opacity: 0.25
                center: locationData.coordinate
            }
        }

//        //Montogomery
//        MapCircle {
//            center {
//             latitude: 37.2296
//             longitude: -80.4139
//            }
//            radius: 2500.0
//            color: 'yellow'
//            border.width: 3
//            opacity: 0.1
//        }

        //Fairfax
        MapCircle {
            center {
             latitude: 38.847118
             longitude: -77.306320
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Prince William County
        MapCircle {
            center {
             latitude: 38.675011
             longitude: -77.314880
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Virginia Beach
        MapCircle {
            center {
             latitude: 36.852924
             longitude: -75.977982
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Loudon County
        MapCircle {
            center {
             latitude: 37.282250
             longitude: -79.968900
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Chester County
        MapCircle {
            center {
             latitude: 37.424252
             longitude: -77.515663
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Henrico County
        MapCircle {
            center {
             latitude: 37.677771
             longitude: -77.565623
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Richmond
        MapCircle {
            center {
             latitude: 37.540567
             longitude: -77.433378
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Chesapeake
        MapCircle {
            center {
             latitude: 36.715417
             longitude: -76.249764
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Norfolk
        MapCircle {
            center {
             latitude: 36.843884
             longitude: -76.286068
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Arlington County
        MapCircle {
            center {
             latitude: 38.889899
             longitude: -77.083275
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Alexandria
        MapCircle {
            center {
             latitude: 38.805496
             longitude: -77.043440
            }
            radius: 10000.0
            color: 'red'
            border.width: 3
            opacity: 0.5
        }

        //Roanoke
        MapCircle {
            center {
             latitude: 37.270675
             longitude: -79.944906
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.1
        }

        //Newport News
        MapCircle {
            center {
             latitude: 36.977708
             longitude: -76.430423
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Montgomery County
        MapCircle {
            center {
             latitude: 37.175534
             longitude: -80.387791
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.25
        }

        //Harrisonburg
        MapCircle {
            center {
             latitude: 38.446058
             longitude: -78.869449
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Stafford County
        MapCircle {
            center {
             latitude: 38.415386
             longitude: -77.454872
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Portsmouth
        MapCircle {
            center {
             latitude: 36.832802
             longitude: -76.297714
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Spotsylvania County
        MapCircle {
            center {
             latitude: 38.182431
             longitude: -77.657226
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Roanoke County
        MapCircle {
            center {
             latitude: 37.330792
             longitude: -80.191237
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Suffolk
        MapCircle {
            center {
             latitude: 36.729624
             longitude: -76.588917
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
        }

        //Lynchburg
        MapCircle {
            center {
             latitude: 37.413914
             longitude: -79.142817
            }
            radius: 10000.0
            color: 'yellow'
            border.width: 3
            opacity: 0.5
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

        Address {
            id :fromAddress
            street: "1370 Seneca Drive"
            city: "Blacksburg"
            country: "USA"
            state : "Virginia"
            postalCode: "24060"
        }

        Address {
            id :toAddress
            street: "1451 Seneca Drive"
            city: "Blacksburg"
            country: "USA"
            state : "Virginia"
            postalCode: "24060"
        }

        MouseArea{
        anchors.fill: parent
            onClicked: {
                geocodeModel.query = fromAddress
                geocodeModel.update()
                geocodeModel1.query = toAddress
                geocodeModel1.update()
            }
        }

        KeyNavigation.left: {
            // clear away any old data in the query
            routeQuery.clearWaypoints();

            // add the start and end coords as waypoints on the route
            routeQuery.addWaypoint(map.startCoordinate1)
            routeQuery.addWaypoint(map.endCoordinate1)
            routeQuery.travelModes = RouteQuery.CarTravel
            routeQuery.routeOptimizations = RouteQuery.FastestRoute
            routeModel.update();

            // center the map on the start coord
            map.center = startCoordinate;

        }

    }

}
