//Cycle ROLL PITCH
void preset2(){
  if (state == 2){
  if (sequence == 0){
    pitchvalue = pitchvalue + factor;
    if (pitchvalue >=160){
      pitchvalue = 160;
      rollvalue = rollvalue - factor;
      if (rollvalue <=20){
        rollvalue = 20;
        sequence = sequence + 1;
      }
    }
  }
  if (sequence == 1){
    rollvalue = rollvalue - factor;
      if (rollvalue <=20){
        rollvalue = 20;
        sequence = sequence + 1;
      }
    }
    
     if (sequence == 2){
    pitchvalue = pitchvalue - factor;
    if (pitchvalue <=20){
      pitchvalue = 20;
      rollvalue = rollvalue + factor;
      if (rollvalue >=160){
        rollvalue = 160;
        sequence = sequence + 1;
      }
    }
  }
  if (sequence == 3){
    pitchvalue = pitchvalue + factor;
      if (pitchvalue >=160){
        pitchvalue = 160;
        sequence = sequence + 1;
      }
    }
  if (sequence == 4){
    rollvalue = rollvalue - factor;
    if (rollvalue <= 90){
      rollvalue = 90;
      sequence = sequence +1;
    }
  }
    if (sequence == 5){
    pitchvalue = pitchvalue - factor;
      if (pitchvalue <=90){
        pitchvalue = 90;
        sequence = 0;
      }
    }
}
  XY.setValue(xvalue, pitchvalue);
  RollPitch.setValue(rollvalue, pitchvalue);
  Yaw.setValue(180 - yawvalue);
  Z.setValue(180 - zvalue);
}
