#include "decision.h"
#include "file_operations.h"
#include "parameters.h"
#include <iostream>
#include <string>

/**
 * @brief The main function of the program.
 *
 * This function serves as the entry point of the program, responsible for reading parameters,
 * opening and processing decision files, making decisions, and saving the results to an output file.
 *
 * @param count The number of command line parameters.
 * @param params An array of C-style strings representing the command line parameters.
 * @return An integer indicating the exit status of the program.
 */

int main(int count, const char* params[]) {
    std::string input_file;
    std::string decision_file;
    std::string output_file;

    if (!read_params(count, params, input_file, decision_file, output_file)){
        exit(2);
    }

    std::vector<Decision> decision_params = open_decision_file(decision_file);

    int amount_of_decision_args = decision_params.size();
    std::vector<std::string> discipline, attribute, value, sign;

    for (const auto& decision : decision_params) {
        discipline.push_back(decision.discipline);
        attribute.push_back(decision.attribute);
        value.push_back(decision.value);
        sign.push_back(decision.sign);
    }
    std::vector<std::string> result = make_decision(amount_of_decision_args, discipline, attribute, value, sign, input_file);
    save_to_file(result, output_file);

    return 0;
}
