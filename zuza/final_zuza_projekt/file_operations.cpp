#include "file_operations.h"
#include "decision.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

void save_to_file(const std::vector<std::string>& output, std::string outputfile) {
    std::ofstream output_file(outputfile);

    if (!output_file.is_open()) {
        std::cerr << "Unable to open the file output.txt for writing" << std::endl;
        // Handle the error accordingly
        return;
    }

    output_file << "Results: \n";

    for (const std::string& line : output) {
        output_file << line << "\n";
    }

    output_file.close();
}

bool isFileSchemeValid(const std::string& filename) {
    try {
        std::ifstream file(filename);

        if (!file.is_open()) {
            std::cerr << "Unable to open the file: " << filename << std::endl;
            return false;
        }

        // Read the first line to get the number of templates/data
        long long numLines;
        file >> numLines;

        std::string line;
        std::getline(file, line); // Consume the rest of the first line

        std::vector<DecisionTemplate> templates;

        // Read decision templates
        for (int i = 0; i < numLines; ++i) {
            std::getline(file, line);
            std::istringstream iss(line);

            DecisionTemplate templateData;
            iss >> templateData.attribute >> templateData.sign >> templateData.value >> templateData.discipline;

            templates.push_back(templateData);
        }

        // Check if the templates are valid
        for (const auto& templateData : templates) {
            if (templateData.sign != "<" && templateData.sign != ">" && templateData.sign != "<=" &&
                templateData.sign != "=<" && templateData.sign != ">=" && templateData.sign != "=>") {
                std::cerr << "Invalid operator in decision template: " << templateData.sign << std::endl;
                return false;
            }
        }

        // Read data lines
        int numDataLines;
        file >> numDataLines;

        std::getline(file, line); // Consume the rest of the second line

        // Check if the number of data lines matches the specified number
        int actualNumDataLines = std::count(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>(), '\n');
        if (numDataLines != actualNumDataLines) {
            std::cerr << "Incorrect number of data lines provided in the file: " << filename << std::endl;
            return false;
        }

        file.close();
        return true;
    } catch (const std::ifstream::failure& e) {
        std::cerr << "Exception opening/reading/closing file: " << e.what() << std::endl;
        return false;
    }
}

void print_instruction() {
    std::cout << "Instruction" << std::endl;
}
