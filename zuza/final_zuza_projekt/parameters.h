#ifndef PARAMETERS_H
#define PARAMETERS_H

#include <string>

/**
 * @brief Reads parameters from the command line.
 *
 * This function reads command line parameters and extracts relevant information,
 * such as data file name, tree file name, and output file name.
 *
 * @param count The number of command line parameters.
 * @param params An array of C-style strings representing the command line parameters.
 * @param dataFileName Reference to store the extracted data file name.
 * @param treeFileName Reference to store the extracted tree file name.
 * @param outputFileName Reference to store the extracted output file name.
 * @return True if parameters are successfully read, false otherwise.
 */

bool read_params(int count, const char** params, std::string& dataFileName, std::string& treeFileName, std::string& outputFileName);

#endif