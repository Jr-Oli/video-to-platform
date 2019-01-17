//Cycle X Y
void preset1(){
  if (state == 1){
  if (sequence == 0){
    yvalue = yvalue + factor;
    if (yvalue >=160){
      yvalue = 160;
      xvalue = xvalue - factor;
      if (xvalue <=20){
        xvalue = 20;
        sequence = sequence + 1;
      }
    }
  }
  if (sequence == 1){
    xvalue = xvalue - factor;
      if (xvalue <=20){
        xvalue = 20;
        sequence = sequence + 1;
      }
    }
    
     if (sequence == 2){
    yvalue = yvalue - factor;
    if (yvalue <=20){
      yvalue = 20;
      xvalue = xvalue + factor;
      if (xvalue >=160){
        xvalue = 160;
        sequence = sequence + 1;
      }
    }
  }
  if (sequence == 3){
    yvalue = yvalue + factor;
      if (yvalue >=160){
        yvalue = 160;
        sequence = sequence + 1;
      }
    }
  if (sequence == 4){
    xvalue = xvalue - factor;
    if (xvalue <= 90){
      xvalue = 90;
      sequence = sequence +1;
    }
  }
    if (sequence == 5){
    yvalue = yvalue - factor;
      if (yvalue <=90){
        yvalue = 90;
        sequence = 0;
      }
    }
}
  XY.setValue(xvalue, yvalue);
  RollPitch.setValue(rollvalue, pitchvalue);
  Yaw.setValue(180 - yawvalue);
  Z.setValue(180 - zvalue);
}
  //XY.setValue(yvalue, xvalue);
  //RollPitch.setValue(rollvalue, pitchvalue);
  //Yaw.setValue(yawvalue);
  //Z.setValue(zvalue);
