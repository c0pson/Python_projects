#include "decision.h"
#include <iostream>
#include <fstream>

std::vector<Decision> open_decision_file(std::string decisionfile) {
    std::vector<Decision> decisions;
    std::ifstream decision_data(decisionfile);

    if (!decision_data.is_open()) {
        std::cerr << "Unable to open the file" << decisionfile << std::endl;
        // Handle the error accordingly
        return decisions;
    }

    int amount_of_decision_args;
    decision_data >> amount_of_decision_args; //czyta inta z pierwszej linijki z decision.txt

    for (int i = 0; i < amount_of_decision_args; ++i) {
        Decision decision;
        decision_data >> decision.attribute >> decision.sign >> decision.value >> decision.discipline;
        decisions.push_back(decision);
    }

    decision_data.close();
    return decisions;
}

std::vector<std::string> make_decision(int amount_of_decision_args, const std::vector<std::string>& discipline,
                                       const std::vector<std::string>& attribute, const std::vector<std::string>& value,
                                       const std::vector<std::string>& sign, std::string inputfile) {
    std::vector<std::string> output;
    std::vector<std::vector<std::string>> vector_of_inp_file;

    std::ifstream input_file(inputfile);
    if (!input_file.is_open()) {
        std::cerr << "Unable to open the file input.txt" << std::endl;
        // Handle the error accordingly
        return output;
    }

    int length_of_input_file;
    input_file >> length_of_input_file;

    for (int j = 0; j < length_of_input_file; ++j) {
        std::vector<std::string> line_data;
        for (int i = 0; i < amount_of_decision_args; ++i) {
            std::string word;
            input_file >> word;
            line_data.push_back(word);
        }
        vector_of_inp_file.push_back(line_data);
    }

    for (int i = 0; i < amount_of_decision_args; ++i) { //2
        output.push_back(discipline[i] + ":");

        if (sign[i] == ">") {
            for (int j = 0; j < length_of_input_file; ++j) {
                if (vector_of_inp_file[j][i] > value[i]) {
                    std::string formatted_data = "";
                    for (const auto& word : vector_of_inp_file[j]) {
                        formatted_data += word + ", ";
                    }
                    formatted_data.pop_back();  // Remove the trailing space
                    formatted_data.pop_back();  // Remove the trailing comma
                    output.push_back(formatted_data + ": " + attribute[i] + " " + sign[i] + " " + value[i]);
                }
            }
        } else if (sign[i] == "<") {
            for (int j = 0; j < length_of_input_file; ++j) {
                if (vector_of_inp_file[j][i] < value[i]) {
                    std::string formatted_data = "";
                    for (const auto& word : vector_of_inp_file[j]) {
                        formatted_data += word + ", ";
                    }
                    formatted_data.pop_back();  // Remove the trailing space
                    formatted_data.pop_back();  // Remove the trailing comma
                    output.push_back(formatted_data + ": " + attribute[i] + " " + sign[i] + " " + value[i]);
                }
            }
        } else if (sign[i] == "=<" || sign[i] == "<=") {
            for (int j = 0; j < length_of_input_file; ++j) {
                if (vector_of_inp_file[j][i] <= value[i]) {
                    std::string formatted_data = "";
                    for (const auto& word : vector_of_inp_file[j]) {
                        formatted_data += word + ", ";
                    }
                    formatted_data.pop_back();  // Remove the trailing space
                    formatted_data.pop_back();  // Remove the trailing comma
                    output.push_back(formatted_data + ": " + attribute[i] + " " + sign[i] + " " + value[i]);
                }
            }
        } else if (sign[i] == "=>" || sign[i] == ">=") {
            for (int j = 0; j < length_of_input_file; ++j) {
                if (vector_of_inp_file[j][i] >= value[i]) {
                    std::string formatted_data = "";
                    for (const auto& word : vector_of_inp_file[j]) {
                        formatted_data += word + ", ";
                    }
                    formatted_data.pop_back();  // Remove the trailing space
                    formatted_data.pop_back();  // Remove the trailing comma
                    output.push_back(formatted_data + ": " + attribute[i] + " " + sign[i] + " " + value[i]);
                }
            }
        }
    }

    input_file.close();
    return output;
}
