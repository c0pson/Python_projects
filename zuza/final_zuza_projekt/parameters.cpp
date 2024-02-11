#include "parameters.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>

bool read_params(int count, const char** params, std::string& dataFileName, std::string& treeFileName, std::string& outputFileName) {
    for (int i = 1; i < count; i += 2) {
        std::string arg = params[i];
        if (arg == "-i") {
            dataFileName = params[i + 1];
        }
        else if (arg == "-t") {
            treeFileName = params[i + 1];
        }
        else if (arg == "-o") {
            outputFileName = params[i + 1];
        }
        else {
            std::cout << "Usage: " << params[0] << " -i <data_file> -t <tree_file> -o <output_file>" << std::endl;
            return false;
        }
    }

    if (dataFileName.empty() || treeFileName.empty() || outputFileName.empty()) {
        std::cout << "Usage: " << params[0] << " -i <data_file> -t <tree_file> -o <output_file>" << std::endl;
        return false;
    }

    return true;
}
