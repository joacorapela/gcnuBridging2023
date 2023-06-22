
import sys
import math
import plotly.graph_objects as go


def prior(success_rate):
    return 1.0 / 101


def likelihood(num_successes, success_rate, num_tests=10):
    answer = (math.comb(num_tests, num_successes) * success_rate**num_successes *
              (1 - success_rate)**(num_tests-num_successes))
    return answer


def main(argv):
    num_bins_succeses = 101
    num_tests = 10
    obs_num_successes = 7
    success_rates = [float(i)/num_bins_succeses
                     for i in range(num_bins_succeses)]
    posterior_success_rates = [
        likelihood(num_successes=obs_num_successes, success_rate=success_rate) *
        prior(success_rate=success_rate) for success_rate in success_rates
    ]
    posterior_success_rates = [posterior_success_rate / 
                               sum(posterior_success_rates)
                               for posterior_success_rate
                               in posterior_success_rates]
    print(posterior_success_rates)

    fig = go.Figure()
    trace = go.Bar(x=success_rates, y=posterior_success_rates)
    fig.add_trace(trace)
    fig.update_layout(xaxis_title="Success Rate",
                      yaxis_title="Probability")
    fig.show()


if __name__ == "__main__":
   main(sys.argv)
