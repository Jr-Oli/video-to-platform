//Cycle Yaw
void preset4(){
  if (state == 4){
    if(sequence ==0){
    yawvalue = yawvalue + factor;
    if (yawvalue >= 140){
      yawvalue = 140;
      sequence = sequence + 1;
    }
  }
  if(sequence ==1){
    yawvalue = yawvalue - factor;
    if (yawvalue <= 40){
      yawvalue = 40;
      sequence = sequence +1;
    }
  }
  if(sequence ==2){
    yawvalue = yawvalue + factor;
    if (yawvalue >= 90){
      yawvalue = 90;
      sequence = 0;
    }
  }
}
  XY.setValue(xvalue, yvalue);
  RollPitch.setValue(rollvalue, pitchvalue);
  Yaw.setValue(180 - yawvalue);
  Z.setValue(180 - zvalue);
}
