#include "iostream"
const int NO_OF_SAMPLES = 50;

extern int tempSensorSample[NO_OF_SAMPLES];
extern int SOCSensorSample[NO_OF_SAMPLES];

void generateSamples(int* tempSensorSample);
void generateSamples(int* SOCSensorSample);
void printSenderSamples(int *tempSensorSample,int *SOCSensorSample);