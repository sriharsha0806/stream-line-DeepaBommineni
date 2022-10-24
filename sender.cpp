#include "sender.hpp"
#include <iostream>

void printSenderSamples(int* tempSensSamples, int* SOCSensSamples) {
	std::cout << "Sensor Values" << std::endl;
  for (int index = 0; index < NO_OF_SAMPLES; index++) {
    std::cout << "Temperature Value: " << tempSensSamples[index]
         << " State Of Charge Value: " << SOCSensSamples[index] <<std::endl;
  }
}

void generateSamples(int * arr)
{
	for (int i = 0; i < NO_OF_SAMPLES; i++) {
    arr[i] = rand() % NO_OF_SAMPLES + 1;
  }
}