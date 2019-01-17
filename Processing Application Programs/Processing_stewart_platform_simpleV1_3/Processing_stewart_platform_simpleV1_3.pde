/*
 * ----------------------------------------------------------------------------
 * Control interface for Stewart Platform
 * It sends servo data to the arduino that controls the servo's.
 * This program is ment to get you started to control a hexapod.
 
 * I'm a designer not a programmer, so if you see ways to improve this software
 * please let me know. I would be happy to update this software and keep on 
 * improving it in the future.
 
 * "THE BEER-WARE LICENSE" (Revision 42):
 * Felix Ros wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return.   
 * cheers, Felix
 
 * Eindhoven The Netherlands  2015
 * www.felixros.com
 * ----------------------------------------------------------------------------
 */
import org.gamecontrolplus.gui.*;
import org.gamecontrolplus.*;
import net.java.games.input.*;

ControlIO control;
ControlDevice stick;

import controlP5.*;  //sliders and buttons
ControlP5 cp5;
int myColor = color(0, 0, 0);  //color

int sliderValue;
float xvalue = 90.0;
float yvalue = 90.0;
float zvalue = 90.0;
float rollvalue = 90.0;
float pitchvalue = 90.0;
int yawvalue = 90;
int state = 7;
int sequence = 0;
int factor = 1;

Slider Yaw;
Slider Z;
Slider2D XY;
Slider2D RollPitch;
RadioButton r;

float n = 90.0; //neatral float for setting value


void setup() {
  size(500, 500, OPENGL);
  surface.setTitle("control panel");
  fill(0);
  noStroke();
  
  // Initialise the ControlIO
  control = ControlIO.getInstance(this);
  // Find a device that matches the configuration file
  stick = control.getMatchedDevice("gamepad_platform");
  if (stick == null) {
    println("No suitable device configured");
    System.exit(-1); // End the program NOW!
  }

  // get the first available port (use EITHER this OR the specific port code below)
  String portName = "COM10";

  // open the serial port
  port = new Serial(this, portName, 115200);

  //sliders and radio
  cp5 = new ControlP5(this);
  r = cp5.addRadioButton("radio", 400, 80);
  r.addItem("Manual", 1);
  r.addItem("XY Circle", 2);
  r.addItem("RollPitch Circle", 3);
  r.addItem("Continous Z", 4);
  r.addItem("Continous Yaw", 5);
  
  Yaw = cp5.addSlider("Yaw")
    .setPosition(270, 350)
      .setRange(0, 180)
        .setSize(180, 20)
          .setValue(n)
            ;
  Z = cp5.addSlider("Z axis")
    .setPosition(270, 50)
      .setRange(0, 180)
        .setSize(20, 180)
          .setValue(n)
            ;
  XY = cp5.addSlider2D("XY axis")
    .setPosition(50, 50)
      .setSize(180, 180)
        .setMaxX (180)
          .setMaxY (180)
            .setMinX (0)
              .setMinY (0)
              .setArrayValue(new float[] {
                n, n
              }
  
  )

    //.disableCrosshair()
    ;
  RollPitch = cp5.addSlider2D("Roll Pitch")
    .setPosition(50, 270)
      .setSize(180, 180)
        .setMaxX (180)
          .setMaxY (180)
            .setMinX (0)
              .setMinY (0)
              .setArrayValue(new float[] {
                n, n
              }
  )

    .setSize(180, 180)
      //.disableCrosshair()
      ;
      
}

void draw() {
  background(myColor);
 if (state == 0){
    manual();
  } 
  if (state ==1){
    preset1();
  }
  if (state ==2){
    preset2();
  }
  if (state == 3);{
    preset3();
  }
  if (state == 4);{
    preset4();
  }
  //calculate servo position
  fill(sliderValue);
  calcServo();
}
void controlEvent(ControlEvent theEvent) {
  if(theEvent.isGroup() && theEvent.name().equals("radio")) {
    
    if (theEvent.getArrayValue()[0] == 1.0){
      state = 0;
    }
    if (theEvent.getArrayValue()[1] == 1.0){
      state = 1;
      returnhome();
    }
    if (theEvent.getArrayValue()[2] == 1.0){
      state = 2;
      returnhome();
    }
    if (theEvent.getArrayValue()[3] == 1.0){
      state = 3;
      returnhome();
    }
    if (theEvent.getArrayValue()[4] == 1.0){
      state = 4;
      returnhome();
    }
  }
}
void returnhome(){
  while ((zvalue!=90)||(yawvalue!=90)||(xvalue!=90)||(yvalue!=90)||(rollvalue!=90)||(pitchvalue!=90)){
    //yawvalue
  if (yawvalue < 90){
    yawvalue = yawvalue + 1;
  }
  if (yawvalue > 90){
    yawvalue = yawvalue - 1;
  }
  //zvalue
  if (zvalue < 90){
    zvalue = zvalue + 1;
  }
  if (zvalue > 90){
    zvalue = zvalue - 1;
  }
  //pitchvalue
  if (pitchvalue < 90){
    pitchvalue = pitchvalue + 1;
  }
  if (pitchvalue > 90){
    pitchvalue = pitchvalue - 1;
  }
  //rollvalue
  if (rollvalue < 90){
    rollvalue = rollvalue + 1;
  }
  if (rollvalue > 90){
    rollvalue = rollvalue - 1;
  }
  //xvalue
  if (xvalue < 90){
    xvalue = xvalue + 1;
  }
  if (xvalue > 90){
    xvalue = xvalue - 1;
  }
  //yvalue
  if (yvalue < 90){
    yvalue = yvalue + 1;
  }
  if (yvalue > 90){
    yvalue = yvalue - 1;
  }
  calcServo();
  }
  sequence = 0;
}
