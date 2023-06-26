
import sys
import math
import numpy as np
import plotly.graph_objects as go


def prior(success_rate):
    return 1.0 / 101


def likelihood(num_successes, success_rate, num_tests=10):
    answer = (math.comb(num_tests, num_successes) * success_rate**num_successes *
              (1 - success_rate)**(num_tests-num_successes))
    return answer


def main(argv):
    num_tests = 10
    true_success_rate = 0.7
    num_observations = 100
    num_bins_succeses = 101

    success_rates = [float(i)/num_bins_succeses
                     for i in range(num_bins_succeses)]
    obs_num_successes = np.random.binomial(n=num_tests, p=true_success_rate,
                                           size=num_observations)
    current_prior = np.array([prior(success_rate=success_rate)
                              for success_rate in success_rates])
    i = -1
    fig = go.Figure()
    trace = go.Bar(x=success_rates, y=current_prior)
    fig.add_trace(trace)
    fig.add_vline(x=true_success_rate, line_color="red")
    fig.update_layout(xaxis_title="Success Rate",
                      yaxis_title="Probability",
                      title=(f"Number Observations {i+1}, "
                             f"True Prob. Success {true_success_rate}"))
    fig.show()
    breakpoint()

    for i, an_obs_num_successes in enumerate(obs_num_successes):
        current_likelihood = np.array([likelihood(num_successes=an_obs_num_successes,
                                                  success_rate=success_rate)
                                       for success_rate in success_rates])
        current_posterior = current_prior * current_likelihood
        current_posterior /= np.sum(current_posterior)
        current_prior = current_posterior

        fig = go.Figure()
        trace = go.Bar(x=success_rates, y=current_posterior)
        fig.add_trace(trace)
        fig.add_vline(x=true_success_rate, line_color="red")
        fig.update_layout(xaxis_title="Success Rate",
                          yaxis_title="Probability",
                          title=(f"Number Observations {i+1}, "
                                 f"True Prob. Success {true_success_rate}"))
        fig.show()
        breakpoint()


if __name__ == "__main__":
   main(sys.argv)
