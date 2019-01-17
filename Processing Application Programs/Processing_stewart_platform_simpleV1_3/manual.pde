void manual(){
  if (state == 0){
    if (stick.getButton("CCW").pressed()){
    yawvalue = yawvalue - factor;
    if (yawvalue <= 40){
      yawvalue = 40;
    }
  }
  if (stick.getButton("CW").pressed()){
    yawvalue = yawvalue + factor;
    if (yawvalue >= 140){
      yawvalue = 140;
    }
  }
  if(stick.getSlider("ZMINUS").getValue() >=0.5){
    zvalue = zvalue -factor;
    if (zvalue <=40) {
      zvalue = 40;
    }
  }
  
  if(stick.getSlider("ZPLUS").getValue() >=0.5){
    zvalue = zvalue +factor;
    if (zvalue >=140) {
      zvalue = 140;
    }
  }
    if(stick.getSlider("XPOS").getValue() <=-0.5){
    xvalue = xvalue - factor;
    if (xvalue <=20) {
      xvalue = 20;
    }
  }
  
  if(stick.getSlider("XPOS").getValue() >=0.5){
    xvalue = xvalue + factor;
    if (xvalue >=160) {
      xvalue = 160;
    }
  }
      if(stick.getSlider("YPOS").getValue() <=-0.5){
    yvalue = yvalue -factor;
    if (yvalue <=20) {
      yvalue = 20;
    }
  }
  
  if(stick.getSlider("YPOS").getValue() >=0.5){
    yvalue = yvalue +factor;
    if (yvalue >=160) {
      yvalue = 160;
    }
  }
  if(stick.getSlider("ROLLPOS").getValue() <=-0.5){
    rollvalue = rollvalue -factor;
    if (rollvalue <=20) {
      rollvalue = 20;
    }
  }
  
  if(stick.getSlider("ROLLPOS").getValue() >=0.5){
    rollvalue = rollvalue +factor;
    if (rollvalue >=160) {
      rollvalue = 160;
    }
  }
    if(stick.getSlider("PITCHPOS").getValue() <=-0.5){
    pitchvalue = pitchvalue -factor;
    if (pitchvalue <=20) {
      pitchvalue = 20;
    }
  }
  
  if(stick.getSlider("PITCHPOS").getValue() >=0.5){
    pitchvalue = pitchvalue +factor;
    if (pitchvalue >=160) {
      pitchvalue = 160;
    }
  }
  //yvalue = map(stick.getSlider("YPOS").getValue(), -1, 1, 0, 180);
//  rollvalue = map(stick.getSlider("ROLLPOS").getValue(), -1, 1, 0, 180);
//  pitchvalue = map(stick.getSlider("PITCHPOS").getValue(), -1, 1, 0, 180);
  XY.setValue(xvalue, yvalue);
  RollPitch.setValue(rollvalue, pitchvalue);
  Yaw.setValue(180 - yawvalue);
  Z.setValue(180 - zvalue);
  }
}
