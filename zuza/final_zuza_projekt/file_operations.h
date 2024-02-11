#ifndef FILE_OPERATIONS_H
#define FILE_OPERATIONS_H

#include <vector>
#include <string>

/**
 * @brief Structure representing a decision template.
 *
 * This structure holds information about a decision template, including
 * attribute, sign, value, and discipline.
 */
struct DecisionTemplate {
    std::string attribute; /**< The attribute of the decision template. */
    std::string sign;      /**< The sign of the decision template. */
    std::string value;     /**< The value of the decision template. */
    std::string discipline;/**< The discipline of the decision template. */
};

/**
 * @brief Saves output to a file.
 *
 * This function takes a vector of strings and saves them to a file.
 *
 * @param output A vector of strings to be saved to the file.
 */
void save_to_file(const std::vector<std::string>& output, std::string outputfile);

/**
 * @brief Checks and processes input files.
 *
 * This function checks the validity of input files and performs processing
 * based on decision and output files.
 *
 * @param input_file The input file to be checked.
 * @param decision_file The decision file used for processing.
 * @param output_file The output file to store the results.
 */
void check_file(const std::string& input_file, const std::string& decision_file, const std::string& output_file);

/**
 * @brief Checks if the file scheme is valid.
 *
 * This function checks the validity of the file scheme based on the filename.
 *
 * @param filename The name of the file to check.
 * @return True if the file scheme is valid, false otherwise.
 */
bool isFileSchemeValid(const std::string& filename);

#endif // FILE_OPERATIONS_H
