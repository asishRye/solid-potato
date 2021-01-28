import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.5

ApplicationWindow {
    visible:true
    width:320
    height:450

    property bool portrait: width<height
    ColumnLayout{
        anchors.fill: parent
        spacing:0

        Rectangle {
            id: answer_sheet
            Layout.fillWidth:true
            Layout.preferredHeight:128
        

            Rectangle {
                anchors.bottom:parent.bottom
                width:parent.width
                height:1
                color:"lightgrey"
            }
        }

        Rectangle {
            
            Layout.fillWidth:true
            Layout.fillHeight:true
            color:"transparent"

            Rectangle{
                anchors.fill:parent
                color:"#ccc"

                GridLayout {
                    anchors.fill:parent
                    columns:4
                    columnSpacing: 1
                    rowSpacing: 1

                    Button{
                        text:"mc"
                        Layout.fillWidth:true
                        Layout.fillHeight:true
                        Layout.rowSpan:1
                        Layout.columnSpan:1

                        background:Rectangle{
                            color:parent.pressed?Qt.darker("white",1.25):"white"
                        }

                        contentItem:Text{
                            text:parent.text
                            padding:parent.padding
                            horizontalAlignment:Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.family:"Segoe MDL2 Assets"
                            font.pixelSize:18
                        }
                    }
                    
                    Button{
                        text:"mc"
                        Layout.fillWidth:true
                        Layout.fillHeight:true
                        Layout.rowSpan:1
                        Layout.columnSpan:1

                        background:Rectangle{
                            color:parent.pressed?Qt.darker("white",1.25):"white"
                        }

                        contentItem:Text{
                            text:parent.text
                            padding:parent.padding
                            horizontalAlignment:Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.family:"Segoe MDL2 Assets"
                            font.pixelSize:18
                        }
                    }

                    Button{
                        text:"mc"
                        Layout.fillWidth:true
                        Layout.fillHeight:true
                        Layout.rowSpan:1
                        Layout.columnSpan:1

                        background:Rectangle{
                            color:parent.pressed?Qt.darker("white",1.25):"white"
                        }

                        contentItem:Text{
                            text:parent.text
                            padding:parent.padding
                            horizontalAlignment:Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.family:"Segoe MDL2 Assets"
                            font.pixelSize:18
                        }
                    }

                    Button{
                        text:"mc"
                        Layout.fillWidth:true
                        Layout.fillHeight:true
                        Layout.rowSpan:1
                        Layout.columnSpan:1

                        background:Rectangle{
                            color:parent.pressed?Qt.darker("white",1.25):"white"
                        }

                        contentItem:Text{
                            text:parent.text
                            padding:parent.padding
                            horizontalAlignment:Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.family:"Segoe MDL2 Assets"
                            font.pixelSize:18
                        }
                    }

                    Button{
                        text:"mc"
                        Layout.fillWidth:true
                        Layout.fillHeight:true
                        Layout.rowSpan:1
                        Layout.columnSpan:1

                        background:Rectangle{
                            color:parent.pressed?Qt.darker("white",1.25):"white"
                        }

                        contentItem:Text{
                            text:parent.text
                            padding:parent.padding
                            horizontalAlignment:Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            font.family:"Segoe MDL2 Assets"
                            font.pixelSize:18
                        }
                    }
                    


                }
            }

            Rectangle { //fullSize
                anchors.fill:parent
                anchors.rightMargin: parent
                visible:!portrait
                color:'lime'
            }
        }
    }
    
    
    

}
