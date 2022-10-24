#include <sender.hpp>

int main() {
	generateSamples(tempSensorSample);
	generateSamples(SOCSensorSample);
	printSenderSamples(tempSensorSample, SOCSensorSample);
	return 0;
}