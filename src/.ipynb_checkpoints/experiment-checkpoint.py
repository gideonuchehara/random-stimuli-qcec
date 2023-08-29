

from src.check_equivalence import are_circuits_equivalent
from src.classical_stimuli import classical_stimuli
from src.global_stimuli import global_stimuli
from src.local_stimuli import local_stimuli
from src.inject_error import inject_error

import pandas as pd
import numpy as np
import time


def single_qcec_experiment(original_circuit_list, transpiled_circuit_list, error_type, num_errors):

    stimuli_names_methods = {"classical": classical_stimuli,
                             "local": local_stimuli, "global": global_stimuli}
    stimuli_results = {"classical": [], "local": [], "global": []}
    # the probability that the error is detected
    error_detection_rate = {"classical": [], "local": [], "global": []}
                                                                      # by the generated set of stimuli
    # the runtime ∅t of the respective scheme in seconds
    runtime = {"classical": [], "local": [], "global": []}
    # num_stimuli = [] # the number of stimuli ∅s needed to detect the error

    for U, G in zip(original_circuit_list, transpiled_circuit_list):

        # For each error-injection option, 50 random seeds have been considered.
        for _ in range(50):
            # Step 4: Inject errors into the circuit
            G_with_error = inject_error(G, error_type, num_errors)

            # Step 5: Generate random stimuli
            for name, method in stimuli_names_methods.items():
                is_equivalent = True

                stimuli_detection = []  # add 1 to list if stimuli detects error and 0 otherwise
                start_time = time.time()
                # For each resulting instance, 5 random seeds have been used for
                # randomly picking stimuli according to the respective scheme.
                for _ in range(5):
                    G_with_stimuli = method(G_with_error)

                    # Step 6: Perform simulations
                    # Step 7: Detect the injected error
                    is_equivalent = are_circuits_equivalent(U, G_with_stimuli)

                    # if is_equivalent is False, error is detected and value=1, otherwise, value=0
                    value = int(not is_equivalent)
                    stimuli_detection.append(value)

                # Total number of stimuli that detected error
                num_stimuli_to_detect_error = sum(stimuli_detection)

                # The number of stimuli ∅s needed to detect the error.
                # The index of the first 1 (first time it was correctly detected)
                # plus 1 to account for zero indexing
                if 1 in stimuli_detection:
                    first_stimuli_to_detect_error = stimuli_detection.index(
                        1) + 1
                else:
                    first_stimuli_to_detect_error = 5+1  # more than 5 stimuli are needed

                stop_time = time.time()
                # Step 8: Collect the results
                stimuli_results[name].append(first_stimuli_to_detect_error)
                error_detection_rate[name].append(
                    (num_stimuli_to_detect_error/5))
                runtime[name].append((stop_time - start_time))

    return error_detection_rate, stimuli_results, runtime


def process_results(error_detection_rate, stimuli_results, runtime):
    """This function processes the output of `single_qcec_experiment` function"""
    average_num_stimuli = {}
    for name, results in stimuli_results.items():
        std = np.std(results)
        # mean = sum(results)/len(results)
        # average_num_stimuli[name] = f"{mean:.1f} " + u"\u00B1" f" {std:.1f}"
        mean = np.mean(results)
        average_num_stimuli[name] = [mean, std]

    average_error_detection_rate = {}
    for name, results in error_detection_rate.items():
        std = np.std(results)
        # mean = sum(results)/len(results)
        # average_error_detection_rate[name] = f"{mean*100:.1f} " + u"\u00B1" f" {std*100:.1f}"
        mean = np.mean(results)
        average_error_detection_rate[name] = [mean, std]

    average_runtime = {}
    for name, results in runtime.items():
        std = np.std(results)
        # mean = sum(results)/len(results)
        # average_runtime[name] = f"{mean:.1f} " + u"\u00B1" f" {std:.1f}"
        mean = np.mean(results)
        average_runtime[name] = [mean, std]

    return average_error_detection_rate, average_num_stimuli, average_runtime


def qcec_experiment(original_circuit_list, transpiled_circuit_list, experiments):

    # initialize an empty dataframe
    df = pd.DataFrame()
    df_main = pd.DataFrame()

    overall_mean_error_detection_rate = {
        "classical": 0, "local": 0, "global": 0}
    overall_std_error_detection_rate = {
        "classical": 0, "local": 0, "global": 0}

    overall_mean_num_stimuli = {"classical": 0, "local": 0, "global": 0}
    overall_std_num_stimuli = {"classical": 0, "local": 0, "global": 0}

    overall_mean_runtime = {"classical": 0, "local": 0, "global": 0}
    overall_std_runtime = {"classical": 0, "local": 0, "global": 0}

    n = 0

    # Begin Experiments
    for exprt, (error_type, num_errors) in experiments.items():
        # stimuli methods
        error_detection_rate, stimuli_results, runtime = \
            single_qcec_experiment(
                original_circuit_list, transpiled_circuit_list, error_type, num_errors)

		# process the results
        average_num_stimuli = {}
        for name, results in stimuli_results.items():
            std = np.std(results)
            mean = np.mean(results)
            average_num_stimuli[name] = f"{mean:.1f} " + u"\u00B1" + f" {std:.1f}"
				   # average_num_stimuli[name] = [mean, std]

            overall_mean_num_stimuli[name] += mean
            overall_std_num_stimuli[name] += std

        average_error_detection_rate = {}
        for name, results in error_detection_rate.items():
            std = np.std(results)
            mean = np.mean(results)
            average_error_detection_rate[name] = f"{mean*100:.1f} " + \
			    u"\u00B1" + f" {std*100:.1f}"
			# average_error_detection_rate[name] = [mean, std]
			
            overall_mean_error_detection_rate[name] += mean*100
            overall_std_error_detection_rate[name] += std*100
			
        average_runtime = {}
        for name, results in runtime.items():
            std = np.std(results)
            mean = np.mean(results)
            average_runtime[name] = f"{mean:.1f} " + u"\u00B1" + f" {std:.1f}"
			# average_runtime[name] = [mean, std]

            overall_mean_runtime[name] += mean
            overall_std_runtime[name] += std

        n += 1

        result_dict = {(exprt, "Ps"): average_error_detection_rate,
                       (exprt, "∅s"): average_num_stimuli,
                       (exprt, "∅t"): average_runtime}

        df = pd.concat([df, pd.DataFrame.from_dict(
            result_dict, orient='index')])  # update dataframe
		
		# for plotting purposes
        main_result_dict = {(exprt, "Ps"): error_detection_rate,
                       (exprt, "∅s"): stimuli_results,
                       (exprt, "∅t"): runtime}

        df_main = pd.concat([df_main, pd.DataFrame.from_dict(
            main_result_dict, orient='index')])  # update dataframe		

    # Compute overall data
    overall_error_detection = {}
    overall_num_stimuli = {}
    overall_runtime = {}
    for name, value in overall_mean_error_detection_rate.items():
        overall_error_detection[name] = f"{overall_mean_error_detection_rate[name]/n:.1f} " + u"\u00B1" + \
                                        f"{overall_std_error_detection_rate[name]/n:.1f}"

        overall_num_stimuli[name] = f"{overall_mean_num_stimuli[name]/n:.1f} " + u"\u00B1" + \
                                    f"{overall_std_num_stimuli[name]/n:.1f}"

        overall_runtime[name] = f"{overall_mean_runtime[name]/n:.1f} " + u"\u00B1" + \
                                f"{overall_std_runtime[name]/n:.1f}"

    overall_dict = {("Overall", "Ps"): overall_error_detection,
                    ("Overall", "∅s"): overall_num_stimuli,
                    ("Overall", "∅t"): overall_runtime}

    df = pd.concat([df, pd.DataFrame.from_dict(
        overall_dict, orient='index')])  # update dataframe

    return df, df_main


                                       # process the results
#         average_error_detection_rate, average_num_stimuli, average_runtime = \
#           process_results(error_detection_rate, stimuli_results, runtime)

#         overal_mean_error_detection_rate += average_error_detection_rate[0]
#         overal_std_error_detection_rate += average_error_detection_rate[1]

#         veral_mean_num_stimuli += average_num_stimuli[0]
#         overal_std_num_stimuli += average_num_stimuli[1]

#         overal_mean_runtime += average_runtime[0]
#         overal_std_runtime += average_runtime[1]

                                       # save results into a dictionary
       # result_dict = {(exprt, "Ps"): f"{100*average_error_detection_rate[0]:.1f} " + u"\u00B1" +
       # f"{100*average_error_detection_rate[1]:.1f}",
       #                (exprt, "∅s"): f"{average_num_stimuli[0]:.1f} " + u"\u00B1" +
       # f"{average_num_stimuli[1]:.1f}",
       #                (exprt, "∅t"): f"{average_runtime[0]:.1f} " + u"\u00B1" +
        # f"{average_runtime[1]:.1f}"}
