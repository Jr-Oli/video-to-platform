//Cycle Z
void preset3(){
  if (state == 3){
  if(sequence ==0){
    zvalue = zvalue + factor;
    if (zvalue >= 140){
      zvalue = 140;
      sequence = sequence + 1;
    }
  }
  if(sequence ==1){
    zvalue = zvalue - factor;
    if (zvalue <= 40){
      zvalue = 40;
      sequence = sequence +1;
    }
  }
  if(sequence ==2){
    zvalue = zvalue + factor;
    if (zvalue >= 90){
      zvalue = 90;
      sequence = 0;
    }
  }
  }
  XY.setValue(xvalue, yvalue);
  RollPitch.setValue(rollvalue, pitchvalue);
  Yaw.setValue(180 - yawvalue);
  Z.setValue(180 - zvalue);
}
