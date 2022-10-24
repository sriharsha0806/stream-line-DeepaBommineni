#include "sender.hpp"
int tempSensorSample[NO_OF_SAMPLES] = {0};
int SOCSensorSample[NO_OF_SAMPLES] = {0};
int main() {
	generateSamples(tempSensorSample);
	generateSamples(SOCSensorSample);
	printSenderSamples(tempSensorSample, SOCSensorSample);
	return 0;
}