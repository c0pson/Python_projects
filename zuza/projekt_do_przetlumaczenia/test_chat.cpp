#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <sstream>

struct Decision {
    std::string attribute;
    std::string sign;
    std::string value;
    std::string discipline;
};

std::vector<Decision> open_decision_file() {
    std::vector<Decision> decisions;
    std::ifstream decision_data("decision.txt");

    if (!decision_data.is_open()) {
        std::cerr << "Unable to open the file decision.txt" << std::endl;
        // Handle the error accordingly
        return decisions;
    }

    int amount_of_decision_args;
    decision_data >> amount_of_decision_args;

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
                                       const std::vector<std::string>& sign) {
    std::vector<std::string> output;
    std::vector<std::vector<std::string>> vector_of_inp_file;

    std::ifstream input_file("input.txt");
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

    for (int i = 0; i < amount_of_decision_args; ++i) {
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

void save_to_file(const std::vector<std::string>& output) {
    std::ofstream output_file("output.txt");

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


int main() {
    check_file("input.txt", "decision.txt", "output.txt");
    // Call open_decision_file to get decision parameters
    std::vector<Decision> decision_params = open_decision_file();

    // Extract data from decision_params to pass to make_decision
    int amount_of_decision_args = decision_params.size();
    std::vector<std::string> discipline, attribute, value, sign;

    for (const auto& decision : decision_params) {
        discipline.push_back(decision.discipline);
        attribute.push_back(decision.attribute);
        value.push_back(decision.value);
        sign.push_back(decision.sign);
    }

    // Call make_decision with extracted parameters
    std::vector<std::string> result = make_decision(amount_of_decision_args, discipline, attribute, value, sign);

    // Print the results
    for (const std::string& line : result) {
        std::cout << line << std::endl;
    }
    save_to_file(result);

    return 0;
}
