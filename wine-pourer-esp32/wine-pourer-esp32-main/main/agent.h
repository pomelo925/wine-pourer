#ifndef AGENT_H
#define AGENT_H

#include <Arduino.h>
#include "motor.h"

class AGENT{
  public:
    AGENT();
    void subscribe();
    void subscribe_test();

  private:
    void _processMessage(String data);
    void _processServoMessage(String data);
    void _processTempMessage(String data);
    void _processWeightMessage(String data);
};

extern AGENT Agent;

#endif