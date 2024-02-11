#ifndef DECISION_H
#define DECISION_H

#include <string>
#include <vector>

/**
 * @brief Structure representing a decision.
 *
 * This structure holds information about a decision, including
 * attribute, sign, value, and discipline.
 */

struct Decision {
    std::string attribute;  /**< The attribute of the decision. */
    std::string sign;       /**< The sign of the decision. */
    std::string value;      /**< The value of the decision. */
    std::string discipline; /**< The discipline of the decision. */
};

/**
 * @brief Opens and reads a decision file.
 *
 * This function opens and reads a decision file, returning a vector of Decision structures.
 *
 * @return A vector of Decision structures read from the decision file.
 */
std::vector<Decision> open_decision_file(std::string decisionfile);

/**
 * @brief Makes a decision based on input arguments.
 *
 * This function makes a decision based on the provided discipline, attribute, value, and sign vectors.
 *
 * @param amount_of_decision_args The number of arguments for making the decision.
 * @param discipline A vector of strings representing the discipline.
 * @param attribute A vector of strings representing the attribute.
 * @param value A vector of strings representing the value.
 * @param sign A vector of strings representing the sign.
 * @return A vector of strings representing the decision made.
 */
std::vector<std::string> make_decision(int amount_of_decision_args, const std::vector<std::string>& discipline,
                                       const std::vector<std::string>& attribute, const std::vector<std::string>& value,
                                       const std::vector<std::string>& sign, std::string inputfile);

#endif // DECISION_H
